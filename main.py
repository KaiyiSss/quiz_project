from question_batch_prepare import load_questions_from_json


def please_select_batch():
#"""This function will prompt the user to select a batch from the list of batches."""
    question_dict = load_questions_from_json("quiz_project/data_config.json")
    for i, batch in enumerate(question_dict):
        print(f"{i+1}. {batch['quiz name']}")
        decision = int(input("Please select the target quiz name: ")) - 1
        selected_quiz = batch[decision]
        input("please enter Y if you selected the correct quiz name otherwise enter N: "
              + selected_quiz['quiz name'])
        if str(input) == 'Y' or 'y':
            return selected_quiz
        if str(input) == 'N' or 'n':
            print("Please select the correct quiz name from the list.")
            continue
    return selected_quiz
    


def main():
    please_select_batch()
    print("This is the main function.")

if __name__ == "__main__":
    main()