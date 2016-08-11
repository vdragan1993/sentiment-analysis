# coding=utf-8
__author__ = 'Dragan Vidakovic'
import os
from openpyxl import load_workbook
from src.model import Review
from src.writer import write_reviews


def list_files_from_directory(directory):
    ret_val = []
    for file in os.listdir(directory):
        if file.endswith(".xlsx"):
            ret_val.append(str(directory) + "/" + str(file))
    return ret_val


def read_reviews_from_file(file_name):
    wb = load_workbook(filename=file_name)
    ws = wb['Sheet1']
    ret_val = []

    index = 0
    for row in ws.rows:
        index += 1
        if index > 1:
            temp_review = Review(row[2].value, row[3].value, row[4].value, row[7].value, row[6].value, row[5].value,
                                 row[8].value, row[9].value, row[10].value, row[11].value, row[12].value, row[1].value,
                                 row[0].value)
            ret_val.append(temp_review)

    return ret_val


def write_folder_reviews(folder, file_name):
    files = list_files_from_directory(folder)
    reviews = []
    for file in files:
        reviews += read_reviews_from_file(file)

    write_reviews(file_name, reviews)
    print("Write file: " + file_name + ", total reviews: " + str(len(reviews)))


if __name__ == "__main__":
    # directories: ../data/xyz
    write_folder_reviews("../data/cg", "../data/cg.xlsx")
    write_folder_reviews("../data/bih", "../data/bih.xlsx")
    write_folder_reviews("../data/srb", "../data/srb.xlsx")
    write_folder_reviews("../data", "../data/all.xlsx")