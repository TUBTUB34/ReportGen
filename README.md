# Lab Template Generator

This Python program is a simple tool to create and edit Word document templates for labs or reports. It offers an interactive command-line interface that guides you through creating a structured document with headers, footers, and customizable sections.

## Features

- **Generate a New Lab Template**: Add a title, subheading, and author details with formatted headers and footers.
- **Edit an Existing Document**: Append paragraphs or headings under existing sections in a document.
- **Auto-save**: Saves the document as you make edits to prevent data loss.

## Requirements

- Python 3.x
- `python-docx` library for manipulating Word documents.

To install `python-docx`, use:

```bash
pip install python-docx
```

## How to Use
1. Run the program in your Python environment.
2. Select an option from the main menu:
   - Make a Template: Creates a new lab template document. You will be prompted to provide a title, subheading, author, and section titles.
   - Edit a Document: Opens an existing .docx document and allows you to add a paragraph or a heading to an existing section.
   - Exit: Exits the program.
   
## Creating a New Lab Template
1. Choose Make a Template from the main menu.
2. Enter the title, subheading, and author details for the document.
3. Add section titles to structure the document (type "done" when finished).

## Editing a Document
1. Choose Edit a Document from the main menu.
2. Enter the name of the .docx file you wish to edit (without the file extension).
3. Add a paragraph or heading to an existing section of the document.

## Code Structure
- Template Class: Handles the creation of a new lab template document, including setting headers, footers, title, and section headings.
- Edit Class: Enables editing of an existing document by adding paragraphs and headings to specific sections.
- Main Program: Provides a command-line interface for user interaction and manages the main menu flow.

## Example
**Here's a quick example of what a session might look like:**

```vbnet
What do you want to do?
1: Make a template
2: Edit a document
3: Exit
Enter your choice (1, 2, or 3): 1

What is the title? Lab Report
Subheading? Experiment 1: Chemical Reactions
Who is it by? John Doe

Enter section titles or 'done' to finish: Introduction
Enter section titles or 'done' to finish: Procedure
Enter section titles or 'done' to finish: Results
Enter section titles or 'done' to finish: done
```
**This example creates a new document titled "Lab Report" with sections for Introduction, Procedure, and Results.**
