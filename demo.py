"""demo."""

from datetime import datetime

from sqlalchemy import (
    JSON,
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    LargeBinary,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import declarative_base, relationship

from sqlalchemy_data_model_visualizer import add_web_font_and_interactivity, generate_data_model_diagram

Base = declarative_base()


class GenericUser(Base):
    """GenericUser."""

    __tablename__ = "generic_user"
    email = Column(String, primary_key=True, index=True)
    external_id = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    is_blocked = Column(Boolean, default=False)
    last_ip_address = Column(String, nullable=True)
    last_user_agent = Column(String, nullable=True)
    last_estimated_location = Column(JSON, nullable=True)
    preferences = Column(JSON)
    registered_at = Column(DateTime, default=datetime.utcnow, index=True)
    last_login = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, index=True)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)
    customer = relationship("Customer", uselist=False, back_populates="generic_user")
    content_creator = relationship("ContentCreator", uselist=False, back_populates="generic_user")
    user_sessions = relationship("UserSession", back_populates="generic_user")
    audit_logs = relationship("GenericAuditLog", back_populates="actor")
    notifications = relationship("GenericNotification", back_populates="recipient")


class Customer(Base):
    """Customer."""

    __tablename__ = "customer"
    email = Column(String, ForeignKey("generic_user.email"), primary_key=True, index=True)
    total_purchases = Column(Numeric(10, 10), default=0.0)
    generic_user = relationship("GenericUser", back_populates="customer")
    service_requests = relationship("ServiceRequest", back_populates="customer")
    subscriptions = relationship("GenericSubscription", back_populates="customer")
    subscription_usages = relationship("GenericSubscriptionUsage", back_populates="customer")
    billing_infos = relationship("GenericBillingInfo", back_populates="customer")
    feedbacks_provided = relationship("GenericFeedback", back_populates="customer")


class ContentCreator(Base):
    """ContentCreator."""

    __tablename__ = "content_creator"
    email = Column(String, ForeignKey("generic_user.email"), primary_key=True, index=True)
    projects_created = Column(Integer, default=0)
    revenue_share = Column(Numeric(10, 10), default=0.7)
    total_earned = Column(Numeric(10, 10), default=0.0)
    last_project_created_at = Column(DateTime, nullable=True)
    generic_user = relationship("GenericUser", back_populates="content_creator")
    api_credit_logs = relationship("GenericAPICreditLog", back_populates="content_creator")
    api_keys = relationship("GenericAPIKey", back_populates="content_creator")
    feedbacks_received = relationship("GenericFeedback", back_populates="content_creator")


class UserSession(Base):
    """UserSession."""

    __tablename__ = "user_session"
    id = Column(Integer, primary_key=True)
    user_email = Column(String, ForeignKey("generic_user.email"), nullable=False)
    session_token = Column(String, unique=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    generic_user = relationship("GenericUser", back_populates="user_sessions")


class FileStorage(Base):
    """FileStorage."""

    __tablename__ = "file_storage"
    id = Column(Integer, primary_key=True, index=True)
    file_data = Column(LargeBinary, nullable=False)
    file_type = Column(String, nullable=False)
    file_hash = Column(String, nullable=False, unique=True)
    upload_date = Column(DateTime, default=datetime.utcnow)


class ServiceRequest(Base):
    """ServiceRequest."""

    __tablename__ = "service_request"
    unique_id_for_sharing = Column(String, primary_key=True, index=True)
    status = Column(String, CheckConstraint("status IN ('pending', 'completed', 'failed')"), default="pending")
    ip_address = Column(String)
    request_time = Column(DateTime, default=datetime.utcnow, index=True)
    request_last_updated_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_input = Column(JSON)
    input_data_string = Column(Text)
    api_request = Column(JSON)
    api_response = Column(JSON)
    api_session_id = Column(String, nullable=True, unique=True)
    total_cost = Column(Numeric(10, 10), nullable=True)
    customer_email = Column(String, ForeignKey("customer.email"))
    customer = relationship("Customer", back_populates="service_requests")


# AuditLog
class GenericAuditLog(Base):
    """GenericAuditLog."""

    __tablename__ = "generic_audit_log"
    id = Column(Integer, primary_key=True, index=True)
    action_type = Column(String, nullable=False, index=True)
    outcome = Column(String, nullable=True)
    field_affected = Column(String, nullable=True)
    prev_value = Column(JSON, nullable=True)
    new_value = Column(JSON, nullable=True)
    actor_email = Column(String, ForeignKey("generic_user.email"), index=True)
    related_request_id = Column(Integer, ForeignKey("generic_user_request.unique_id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    actor = relationship("GenericUser", back_populates="audit_logs")


# Feedback
class GenericFeedback(Base):
    """GenericFeedback."""

    __tablename__ = "generic_feedback"
    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, nullable=False)
    commentary = Column(Text, nullable=True)
    customer_email = Column(String, ForeignKey("customer.email"), index=True)
    content_creator_email = Column(String, ForeignKey("content_creator.email"), index=True)
    request_id = Column(Integer, ForeignKey("generic_user_request.unique_id"))
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_removed = Column(Boolean, default=False)
    removed_at = Column(DateTime, nullable=True)
    customer = relationship("Customer", back_populates="feedbacks_provided")
    content_creator = relationship("ContentCreator", back_populates="feedbacks_received")


# APIKeys
class GenericAPIKey(Base):
    """GenericAPIKey."""

    __tablename__ = "generic_api_key"
    id = Column(Integer, primary_key=True, index=True)
    api_key = Column(String, unique=True, nullable=False)
    content_creator_email = Column(String, ForeignKey("content_creator.email"), index=True)
    is_active = Column(Boolean, default=True)
    is_revoked = Column(Boolean, default=False)
    expires_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    content_creator = relationship("ContentCreator", back_populates="api_keys")


# Notification
class GenericNotification(Base):
    """GenericNotification."""

    __tablename__ = "generic_notification"
    id = Column(Integer, primary_key=True, index=True)
    recipient_email = Column(String, ForeignKey("generic_user.email"), index=True)
    notification_kind = Column(String, nullable=False)
    is_read = Column(Boolean, default=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    read_at = Column(DateTime, nullable=True)
    recipient = relationship("GenericUser", back_populates="notifications")


# APICreditLog
class GenericAPICreditLog(Base):
    """GenericAPICreditLog."""

    __tablename__ = "generic_api_credit_log"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    is_paid = Column(Boolean, default=False)
    status = Column(String, default="pending")
    expense = Column(Numeric(10, 10), nullable=False)
    request_id = Column(Integer, ForeignKey("generic_user_request.unique_id"))
    token_count = Column(Integer, nullable=False)
    content_creator_email = Column(String, ForeignKey("content_creator.email"))
    content_creator = relationship("ContentCreator", back_populates="api_credit_logs")


# SubscriptionType
class GenericSubscriptionType(Base):
    """GenericSubscriptionType."""

    __tablename__ = "generic_subscription_type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    monthly_fee = Column(Numeric(10, 10), nullable=False)
    monthly_cap = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_removed = Column(Boolean, default=False)
    removed_at = Column(DateTime, nullable=True)
    subscriptions = relationship("GenericSubscription", back_populates="subscription_type")


# Subscription
class GenericSubscription(Base):
    """GenericSubscription."""

    __tablename__ = "generic_subscription"
    id = Column(Integer, primary_key=True, index=True)
    customer_email = Column(String, ForeignKey("customer.email"), index=True)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    current_use = Column(Integer, default=0)
    subscription_type_id = Column(Integer, ForeignKey("generic_subscription_type.id"))
    customer = relationship("Customer", back_populates="subscriptions")
    subscription_type = relationship("GenericSubscriptionType", back_populates="subscriptions")
    subscription_usages = relationship("GenericSubscriptionUsage", back_populates="subscription")


# SubscriptionUsage
class GenericSubscriptionUsage(Base):
    """GenericSubscriptionUsage."""

    __tablename__ = "generic_subscription_usage"
    id = Column(Integer, primary_key=True, index=True)
    customer_email = Column(String, ForeignKey("customer.email"), index=True)
    use_count = Column(Integer, default=0)
    last_use = Column(DateTime, nullable=True)
    subscription_id = Column(Integer, ForeignKey("generic_subscription.id"))
    subscription_type_id = Column(Integer, ForeignKey("generic_subscription_type.id"))
    customer = relationship("Customer", back_populates="subscription_usages")
    subscription = relationship("GenericSubscription", back_populates="subscription_usages")
    subscription_type = relationship("GenericSubscriptionType", backref="subscription_usages")


# BillingInfo
class GenericBillingInfo(Base):
    """GenericBillingInfo."""

    __tablename__ = "generic_billing_info"
    id = Column(Integer, primary_key=True, index=True)
    customer_email = Column(String, ForeignKey("customer.email"), index=True)
    payment_type = Column(String, nullable=False)
    payment_data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_removed = Column(Boolean, default=False)
    removed_at = Column(DateTime, nullable=True)
    customer = relationship("Customer", back_populates="billing_infos")


def main() -> None:
    """Main."""
    models = [
        GenericUser,
        Customer,
        ContentCreator,
        UserSession,
        FileStorage,
        ServiceRequest,
        GenericAuditLog,
        GenericFeedback,
        GenericAPIKey,
        GenericNotification,
        GenericAPICreditLog,
        GenericSubscriptionType,
        GenericSubscription,
        GenericSubscriptionUsage,
        GenericBillingInfo,
    ]

    # Generate the diagram and add interactivity
    generate_data_model_diagram(models, "my_data_model_diagram", add_labels=True)
    add_web_font_and_interactivity("my_data_model_diagram.svg", "my_interactive_data_model_diagram.svg")


if __name__ == "__main__":
    pass
