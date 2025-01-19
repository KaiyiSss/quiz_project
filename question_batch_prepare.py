import json

class question_database:
    def __init__(self):
        self.question_list = []
        
    def add_question(self, question):
        self.question_list.append(question)
        
    def get_question(self):
        return self.question_list

    def load_questions_from_json(self, file_path) -> json:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for question in data['questions']:
                self.add_question(question)