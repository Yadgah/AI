import json
import os

def read_data(filename):
    filepath = "./data/" + filename
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"standard_questions": [], "spam_questions": []}
    return {"standard_questions": [], "spam_questions": []}

def write_data(filename, data):
    filepath = "./data/" + filename
    existing_data = read_data(filename)
    
    # ترکیب داده‌های قبلی و جدید
    existing_data['standard_questions'].extend(data.get('standard_questions', []))
    existing_data['spam_questions'].extend(data.get('spam_questions', []))
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

def add_question(category, question):
    filename = 'questions_dataset.json'
    new_data = {"standard_questions": [], "spam_questions": []}
    
    if category == '1':
        new_data['standard_questions'].append(question)
    elif category == '2':
        new_data['spam_questions'].append(question)
    else:
        print("Category Invalid")
        return
    
    write_data(filename, new_data)
    print("Question added")

def cli_menu():
    while True:
        os.system('clear')
        print("1. Correct Question's")
        print("2. Incorrect Question's")
        print("3. Exit")
        choice = input("[1/2/3]==> ")

        if choice in ['1', '2']:
            question = input("Question text: ")
            add_question(choice, question)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    cli_menu()
