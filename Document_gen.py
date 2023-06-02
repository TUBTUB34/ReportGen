from Template import Template
from Edit_doc import Edit
import os

def is_doc():
    while True:
        temp = input("Enter the name of the document you want to edit (or 'cancel' to go back): ")
        document_name = temp + '.docx'

        if temp == 'cancel':
            print("Returning to the main menu.")
            break

        if not os.path.exists(document_name):
            print("Document does not exist. Please try again.")
            continue

        # Add your document editing logic here
        print("Editing document:", document_name)
        break
    e = Edit(document_name)
    return e

def ed_menu():
    print("\nWhat do you want to do?")
    print("1: Add Paragraph to existing menu")
    print("2: Add heading")
    print("3: Exit")

    choice = input("Enter your choice (1, 2, or 3): ")
    return choice
    

while True:
    print("\nWhat do you want to do?")
    print("1: Make a template")
    print("2: Edit a document")
    print("3: Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        title = input('What is the title?')
        my_doc=Template(title)
        my_doc.add_headings()
    elif choice == '2':
        e = is_doc()
        c2 = ed_menu()
        if c2 =='1':
            e.add_info('p')
        elif c2 == '2':
            e.add_info('h')

    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")