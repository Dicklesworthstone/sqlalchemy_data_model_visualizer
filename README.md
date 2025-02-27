# SQLAlchemy Data Model Visualizer

## Overview

This Python-based utility generates high-quality, readable visualizations of your SQLAlchemy ORM models with almost no effort. With a focus on clarity and detail, it uses Graphviz to render each model as a directed graph, making it easier to understand the relationships between tables in your database schema.

![Example Data Model Diagram](https://raw.githubusercontent.com/Dicklesworthstone/sqlalchemy_data_model_visualizer/main/my_interactive_data_model_diagram.svg)

## Try it Out Easily in Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1np5kPvDtdhq138eLHOGINYuTUMJo_wrj?usp=sharing)

## Features

- Automatically maps SQLAlchemy ORM models to a directed graph.
- Table-like representation of each model with fields, types, and constraints.
- Export diagrams to SVG format for high-quality viewing and printing using Roboto font. 

## Installation with pip and Usage:

```bash
pip install sqlalchemy-data-model-visualizer

# Suppose these are your SQLAlchemy data models defined above in the usual way, or imported from another file:
models = [GenericUser, Customer, ContentCreator, UserSession, FileStorage, ServiceRequest, GenericAuditLog, GenericFeedback, GenericAPIKey, GenericNotification, GenericAPICreditLog, GenericSubscriptionType, GenericSubscription, GenericSubscriptionUsage, GenericBillingInfo]
output_file_name = 'my_data_model_diagram'
generate_data_model_diagram(models, output_file_name)
add_web_font_and_interactivity('my_data_model_diagram.svg', 'my_interactive_data_model_diagram.svg')
```

## Installation from Source

To get started, clone the repository and install the required packages.

```bash
git clone https://github.com/Dicklesworthstone/sqlalchemy_data_model_visualizer.git
cd sqlalchemy_data_model_visualizer
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install wheel
pip install -r requirements.txt
```

## Requirements

- Python 3.x
- SQLAlchemy
- Graphviz
- lxml

## Usage

### Generate Data Model Diagram

First, paste in your SQLAlchemy models. A set of fairly complex data models are provided in the code directly as an example-- just replace these with your own from your application.

Then, simply call the `generate_data_model_diagram` function. This will generate an SVG file with the name `my_data_model_diagram.svg`.

## API Documentation

### `generate_data_model_diagram(models, output_file='my_data_model_diagram', add_labels=True)`

- `models`: List of SQLAlchemy models you want to visualize.
- `output_file`: Name of the output SVG file.
- `add_labels`: Set to False to hide labels on the edges between tables

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

Thanks for your interest in my open-source project! I hope you find it useful. You might also find my commercial web apps useful, and I would really appreciate it if you checked them out:

**[YoutubeTranscriptOptimizer.com](https://youtubetranscriptoptimizer.com)** makes it really quick and easy to paste in a YouTube video URL and have it automatically generate not just a really accurate direct transcription, but also a super polished and beautifully formatted written document that can be used independently of the video.

The document basically sticks to the same material as discussed in the video, but it sounds much more like a real piece of writing and not just a transcript. It also lets you optionally generate quizzes based on the contents of the document, which can be either multiple choice or short-answer quizzes, and the multiple choice quizzes get turned into interactive HTML files that can be hosted and easily shared, where you can actually take the quiz and it will grade your answers and score the quiz for you.

**[FixMyDocuments.com](https://fixmydocuments.com/)** lets you submit any kind of document— PDFs (including scanned PDFs that require OCR), MS Word and Powerpoint files, images, audio files (mp3, m4a, etc.) —and turn them into highly optimized versions in nice markdown formatting, from which HTML and PDF versions are automatically generated. Once converted, you can also edit them directly in the site using the built-in markdown editor, where it saves a running revision history and regenerates the PDF/HTML versions.

In addition to just getting the optimized version of the document, you can also generate many other kinds of "derived documents" from the original: interactive multiple-choice quizzes that you can actually take and get graded on; slick looking presentation slides as PDF or HTML (using LaTeX and Reveal.js), an in-depth summary, a concept mind map (using Mermaid diagrams) and outline, custom lesson plans where you can select your target audience, a readability analysis and grade-level versions of your original document (good for simplifying concepts for students), Anki Flashcards that you can import directly into the Anki app or use on the site in a nice interface, and more.
