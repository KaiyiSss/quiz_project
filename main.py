from question_batch_prepare import question_database


# todo: batch is generally utilized to indicate grouped items. From a dev who does not know how your question input or other
#  code works do you think the term 'batch' is appropriate?
def please_select_batch():
    """This function will prompt the user to select a batch from the list of batches."""
    database = question_database()
    # todo: different users name their folders differently. So my project is named "Kaiyi_Quiz_Project". The data file
    #  for me is located at: "Kaiyi_Quiz_Project/data_config.json" which is different from this.
    #  What are your potential options so that you can avoid this from happening?
    database.load_questions_from_json("data_config.json")
    question_dict = database.get_question()
    # todo: Adding a retry is very important for APIs this help avoid excessive network usage and server load.
    #  This being a code that users will run locally , do you think this is required? Please provide pros/cons for having this vs not having.
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
            # todo: This is a great checkpoint and properly required to make sure the user knows which name they selected.
            #  Do you think it would help if you output the selected quiz's name?
            checkpoint = input("please enter Y if you selected the correct quiz name otherwise enter N: ")
            if checkpoint.lower() == 'y':
                return selected_quiz
            else:
                # todo: This display of the list of questions shows up differently from the initial one line 19.
                #  Do you think a consistent input would help users navigate?
                print(f"Please select the correct quiz name from the list." + "\n" + f"{recall_question_dict}")
        else:
            invalid_input = input("Invalid input, please select a valid quiz number: ")
            retry_i = 0    
            for retry_i in range(retry_max):
                input("Please select a valid quiz number: ")
                exit("You have exceeded the maximum number of retries. Exiting the program.")
                    
                    


def main():
    please_select_batch()
    

if __name__ == "__main__":
    main()