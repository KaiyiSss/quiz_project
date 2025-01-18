import json

class question_database:
    def __init__(self):
        self.question_list = []
        
    def add_question(self, question):
        self.question_list.append(question)
        
    def get_question(self):
        return self.question_list

def load_questions_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['questions']