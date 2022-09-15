import os
import csv
from csv import writer
import io



def file_existence_checker(file_name, column_name_1, column_name_2, column_name_3, column_name_4 = None, column_name_5 = None, column_name_6 = None):
    try:
        with open(file_name) as csv_file:
            return

    except Exception:
        with open(file_name, mode="w") as csv_file:
            fieldnames = [column_name_1, column_name_2, column_name_3, column_name_4, column_name_5, column_name_6]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
        print("File has not been created yet. New file was created")
        return Exception


def data_writer(file_name, add_new_content):

    try:

        with open(file_name, mode="a+") as csv_file:
            csv_writer = writer(csv_file)
            csv_writer.writerow(add_new_content)

        print("New content was added.")
        return

    except Exception:
        print("Content could not be added.")
        return Exception

def data_writer_without_duplicity(file_name, add_new_content):

    with io.open(file_name, mode="r", newline='', encoding='utf-8') as csv_file:
        content = csv_file.read()

        if add_new_content[0] in content:
            print(f"\nContent cannot be added.\nContent has already been added.")
            return False

        try:
            with open(file_name, mode="a+") as csv_file:
                csv_writer = writer(csv_file)
                csv_writer.writerow(add_new_content)
            print("New content was added.")
            return

        except Exception:
            print("Content could not be added.")
            return Exception

def get_file_content(file_name):
    with io.open(file_name, mode="r", newline='', encoding='utf-8') as csv_file:
        content = csv_file.read()
    return content

def remove_data(file_name, content_to_remove):
    row = []
    lines = list()
    lines_content = []

    try:
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                lines.append(row)

                for field in row:
                    if field == content_to_remove:
                        lines.remove(row)
                        lines_content.append(row)
                        print("Content was removed.")

                        with open(file_name, 'w') as csv_file:
                            writer = csv.writer(csv_file)
                            writer.writerows(lines)
                        return lines

                    else:
                        row = []

            if len(lines_content) == 0:
                print("Content cannot be found.")
            return lines_content  
                      
    except Exception:
        print("No content has been added yet.")
        return Exception

def find_data(file_name, find_content):
    row = []
    found_content = []

    try:
        with io.open(file_name, mode="r", newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                if find_content in row:
                    found_content.append(row)
                else:
                    row = []
            
            if len(found_content) == 0:
                print("Content cannot be found.")
            return found_content

    except Exception:
        print("No content has been added yet.")
        return Exception

def record_counter(file_name):
    try:
        with open(file_name,"r") as csv_file: 
	        content = csv_file.readlines() 

        lastRow = content[-1] 
        first_col = lastRow[0]
        int_first_col = int(first_col)

        last_record_num = int_first_col + 1

        return last_record_num
        
    except Exception:
        return Exception




