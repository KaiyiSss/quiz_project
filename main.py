from question_batch_prepare import question_database



def please_select_batch():
    """This function will prompt the user to select a batch from the list of batches."""
    database = question_database()
    database.load_questions_from_json("quiz_project/data_config.json")
    question_dict = database.get_question()
    retry_max = 6
    recall_question_dict = {}
    
    for i, batch in enumerate(question_dict):
        print(f"{i+1}. {batch['quiz name']}")
        recall_question_dict = {i+1: batch['quiz name'] for i, batch in enumerate(question_dict)}
           
    while True:
        input_decision = int(input("Please select the target quiz number: ")) - 1
        decision_number = input_decision
        if 0 <= decision_number < len(question_dict): 
            selected_quiz = question_dict[decision_number]
            checkpoint = input("please enter Y if you selected the correct quiz name otherwise enter N: ")
            if checkpoint.lower() == 'y':
                return selected_quiz
            else:
                print(f"Please select the correct quiz name from the list." + "\n" + f"{recall_question_dict}")
        else:
            invalid_input = input("Invalid input: {decision_number + 1}, please select a valid quiz number: ")
            if 0 <= invalid_input < len(question_dict):
                return True
            else:
                for retry_i in range(retry_max):
                    input("Please select a valid quiz number: ")
                exit("You have exceeded the maximum number of retries. Exiting the program.")
                    
                    


def main():
    please_select_batch()
    

if __name__ == "__main__":
    main()