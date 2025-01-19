import json

# todo: is this database for all the potential questions? Will you create more than 1 database object?
class question_database:
    def __init__(self):
        self.question_list = []
        
    def add_question(self, question):
        self.question_list.append(question)

    # todo: So this is a item that holds a list of questions; however, in the get_question() you are returning
    #  the whole list would it be more accurate to rename the function to get_questions() ?
    def get_question(self):
        return self.question_list

    def load_questions_from_json(self, file_path) -> json:
        # todo: what happens if a user enters a file that is missing or the folder does not exist?
        # todo: Does his accept all file types? (csv, txt, etc.) I usually add validations for file inputs before the
        #  feature is complete. This prevents me from potentially forgetting that I need to validate.
        with open(file_path, 'r') as file:
            data = json.load(file)
            for question in data['questions']:
                self.add_question(question)