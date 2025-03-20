import json
import os

def read_data(filename):
    if os.path.exists(filename):
        with open("./data/" + filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {"standard_questions": [], "spam_questions": []}
def write_data(filename, data):
    with open("./data/" + filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_question(data, category, question):
    if category == '1':
        data['standard_questions'].append(question)
    elif category == '2':
        data['spam_questions'].append(question)
    else:
        print("Category Invalid")

def cli_menu():
    filename = 'questions_dataset.json'
    data = read_data(filename)

    while True:
        os.system('clear')
        print("1. Correct Question's")
        print("2. Incorrect Question's")
        print("3. Exit")
        choice = input("[1/2/3]==> ")

        if choice in ['1', '2']:
            question = input("Question text: ")
            add_question(data, choice, question)
            write_data(filename, data)
            print("Question added")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    cli_menu()

