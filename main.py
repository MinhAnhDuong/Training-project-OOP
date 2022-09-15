import exercise_model

def main():
    exercise_file_name = ""
    records_file_name = ""

    #exercise_file_name = input("Enter exercise file name: ").lower()
    #records_file_name = input("Enter training record file name: ").lower()
    exercise_file_name = "list_of_exercises.csv"
    records_file_name = "list_of_training_records.csv"

    main_menu = '''
    1. Exercises
    2. Training records
    0. Exit the program
    '''

    exercises_menu = '''
    1. List of exercises
    2. Add a new exercise
    3. Remove exercise
    4. Find exercise
    5. Back to the main menu
    0. Exit the program
    '''

    training_records_menu = '''
    1. List of training records
    2. Add a new training record 
    3. Remove training record
    4. Find training record
    5. Back to the main menu
    0. Exit the program
    '''

    exercise = exercise_model.Exercise(exercise_file_name)
    training_record = exercise_model.TrainingRecords(records_file_name)

    while True:

        print(main_menu)

        user_choice = input("Choose an option: ")
        
        if user_choice == "1":

            while True:
                print(exercises_menu)

                user_choice = input("Choose an option: ")

                if user_choice == "1":
                    content = exercise.list_exercises()
                    print(content)

                elif user_choice == "2":
                    new_list_exercise = []

                    new_exercise = input("Enter new exercise: ")
                    new_note = input("Enter note: ")

                    new_list_exercise.append(new_exercise)
                    new_list_exercise.append(new_note)

                    exercise.create_new_exercise(new_list_exercise)
                
                elif user_choice == "3":
                    remove_exercise = input("Enter exercise: ")
                    exercise.remove_exercise(remove_exercise)

                elif user_choice == "4":
                    user_find_exercise = input("Enter exercise: ")
                    exercise_content = exercise.find_exercise(user_find_exercise)
                    print(exercise_content)
                
                elif user_choice == "5":
                    break

                elif user_choice == "0":
                    exit()         

        elif user_choice == "2":

            while True:
                print(training_records_menu)

                user_choice = input("Choose an option: ")

                if user_choice == "1":
                    content = training_record.list_training_records()
                    print(content)

                elif user_choice == "2":
                    new_list_training_record = []

                    new_record = input("Enter exercise: ")
                    new_note = input("Enter note: ")
                    new_date = input("Enter date: ")
                    new_series = input("Enter number of series: ")
                    new_repetition = input("Enter number of repetitions: ")

                    new_list_training_record.extend([new_record, new_note, new_date, new_series, new_repetition])


                    if training_record.create_new_training_record(exercise_file_name, new_list_training_record) == False:
                        continue
                    
                elif user_choice == "3":
                    remove_training_record = input("Enter training record: ")
                    training_record.remove_training_record(remove_training_record)

                elif user_choice == "4":
                    user_find_record = input("Enter training record: ")
                    record = training_record.find_training_record(user_find_record)
                    print(record)
                
                elif user_choice == "5":
                    break

                elif user_choice == "0":
                    exit()

        elif user_choice == "0":

            exit()

main()