import file_operations
import io


class Exercise:
    def __init__(self, exercise_file_name):
        self.exercise_file_name = exercise_file_name

    def create_new_exercise(self, list_of_new_exercises):
        file_operations.file_existence_checker(self.exercise_file_name, "Number", "Exercises", "Notes")
        file_operations.data_writer_without_duplicity(self.exercise_file_name, list_of_new_exercises)
    
    def list_exercises(self):
        file_operations.file_existence_checker(self.exercise_file_name, "Number","Exercises", "Notes")
        content = file_operations.get_file_content(self.exercise_file_name)
        return content

    def remove_exercise(self, exercise_to_remove):
        file_operations.remove_data(self.exercise_file_name, exercise_to_remove)
    
    def find_exercise(self, exercise):
        row = file_operations.find_data(self.exercise_file_name, exercise)
        return row


class TrainingRecords:
    def __init__(self, records_file_name):
        self.records_file_name = records_file_name

    def create_new_training_record(self, exercise_file_name, list_of_new_records):
        exercise_name = list_of_new_records[1]
        
        exercise = Exercise(exercise_file_name)
        if len(exercise.find_exercise(exercise_name)) == 0:
            print("Training record cannot be added. The exercise does not exist, enter the exercise in to the exercise list.")
            return False

        file_operations.file_existence_checker(self.records_file_name, "Number","Exercises", "Notes", "Date", "Series", "Repetitions")
        file_operations.data_writer(self.records_file_name, list_of_new_records)
    
    def list_training_records(self):
        file_operations.file_existence_checker(self.records_file_name, "Number","Exercises", "Notes", "Date", "Series", "Repetitions")
        content = file_operations.get_file_content(self.records_file_name)
        return content

    def remove_training_record(self, records_to_remove):
        file_operations.remove_data(self.records_file_name, records_to_remove)
    
    def find_training_record(self, training_record):
        row = file_operations.find_data(self.records_file_name, training_record)
        return row
    def record_number(self):
        number = file_operations.record_counter(self.records_file_name)
        print(number)
        return number



    
#---------------------------------------------------------------------------------------------------
##           create
##list_of_new_exercises = ["beh", "drepPoznamkaZkouska"]
#list_of_new_records = ["beh","drepPoznamkaZkouska222", "15.7.2021", 5, 10]
#
##           remove
##exercise_to_remove = "pritahy"
##records_to_remove = "shyby"
#
##           find
#exercise = "klik"
##training_record = "beh"
##---------------------------------------------------------------------------------------------------
#
##exercise = Exercise("list_of_exercises.csv")
##exer = Exercise("list_of_exercises.csv")
record = TrainingRecords("list_of_training_records.csv")
record.record_number()














    