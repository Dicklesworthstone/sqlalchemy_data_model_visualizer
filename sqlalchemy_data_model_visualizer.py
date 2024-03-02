import os

import graphviz
from lxml import etree
from sqlalchemy import inspect


def generate_data_model_diagram(models, output_file="my_data_model_diagram", add_labels=True, view_diagram=True):
    # Initialize graph with more advanced visual settings
    dot = graphviz.Digraph(
        comment="Interactive Data Models",
        format="svg",
        graph_attr={"bgcolor": "#EEEEEE", "rankdir": "TB", "splines": "spline"},
        node_attr={"shape": "none", "fontsize": "12", "fontname": "Roboto"},
        edge_attr={"fontsize": "10", "fontname": "Roboto"},
    )

    # Iterate through each SQLAlchemy model
    for model in models:
        insp = inspect(model)
        name = insp.class_.__name__

        # Create an HTML-like label for each model as a rich table
        label = f"""<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="2" BGCOLOR="#3F51B5"><FONT COLOR="white">{name}</FONT></TD></TR>
        """

        for column in insp.columns:
            constraints = []
            if column.primary_key:
                constraints.append("PK")
            if column.unique:
                constraints.append("Unique")
            if column.index:
                constraints.append("Index")

            constraint_str = ",".join(constraints)
            color = "#BBDEFB"

            label += f"""<TR>
                         <TD BGCOLOR="{color}">{column.name}</TD>
                         <TD BGCOLOR="{color}">{column.type} ({constraint_str})</TD>
                         </TR>"""

        label += "</TABLE>>"

        # Create the node with added hyperlink to detailed documentation
        dot.node(name, label=label, URL=f"http://{name}_details.html")

        # Add relationships with tooltips and advanced styling
        for rel in insp.relationships:
            target_name = rel.mapper.class_.__name__
            tooltip = f"Relation between {name} and {target_name}"
            dot.edge(
                name,
                target_name,
                label=rel.key if add_labels else None,
                tooltip=tooltip,
                color="#1E88E5",
                style="dashed",
            )

    # Render the graph to a file and open it
    dot.render(output_file, view=view_diagram)


def add_web_font_and_interactivity(input_svg_file, output_svg_file):
    if not os.path.exists(input_svg_file):
        print(f"Error: {input_svg_file} does not exist.")
        return

    parser = etree.XMLParser(remove_blank_text=True)
    try:
        tree = etree.parse(input_svg_file, parser)
    except etree.XMLSyntaxError as e:
        print(f"Error parsing SVG: {e}")
        return

    root = tree.getroot()

    style_elem = etree.Element("style")
    style_elem.text = """
    @import url("https://fonts.googleapis.com/css?family=Roboto:400,400i,700,700i");
    """
    root.insert(0, style_elem)

    for elem in root.iter():
        if "node" in elem.attrib.get("class", ""):
            elem.attrib["class"] = "table-hover"
        if "edge" in elem.attrib.get("class", ""):
            source = elem.attrib.get("source")
            target = elem.attrib.get("target")
            elem.attrib["class"] = f"edge-hover edge-from-{source} edge-to-{target}"

    tree.write(output_svg_file, pretty_print=True, xml_declaration=True, encoding="utf-8")
