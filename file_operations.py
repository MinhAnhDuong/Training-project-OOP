import os
import csv
from csv import writer
import io
from turtle import Turtle


def file_existence_checker(file_name, column_name_1, column_name_2, column_name_3 = None, column_name_4 = None, column_name_5 = None):
    try:
        with open(file_name) as csv_file:
            return

    except FileNotFoundError:
        with open(file_name, mode="w") as csv_file:
            fieldnames = [column_name_1, column_name_2, column_name_3, column_name_4, column_name_5]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
        print("File has not been created yet. New file was created")


def data_writer(file_name, add_new_content):

    try:
        with open(file_name, mode="a+") as csv_file:
            csv_writer = writer(csv_file)
            csv_writer.writerow(add_new_content)
        print("New content was added.")
        return

    except:
        print("Content could not be added.")
        return

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

        except:
            print("Content could not be added.")
            return

def get_file_content(file_name):
    with io.open(file_name, mode="r", newline='', encoding='utf-8') as csv_file:
        content = csv_file.read()
    return content

def remove_data(file_name, content_to_remove):

    lines = list()

    try:
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                lines.append(row)

                for field in row:
                    if field == content_to_remove:
                        lines.remove(row)
                        print("Content was removed.")
                        return lines

        print("Content cannot be removed. The specified content does not exist.")


        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(lines)
            return   
                      
    except:
        print("No content has been added yet.")
        return

def find_data(file_name, find_content):
    row = []

    try:
        with io.open(file_name, mode="r", newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                if row[0] == find_content:
                    return row
                else:
                    row = []
                    
            print("Content cannot be found.")
            return row

    except FileNotFoundError:
        print("No content has been added yet.")



