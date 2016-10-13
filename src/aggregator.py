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

            this_title = latin_replace(row[4].value)
            this_content = latin_replace(row[5].value)

            if is_valid_text(this_title) and is_valid_text(this_content) and this_title != '' and this_content != '':
                temp_review = Review(row[2].value, row[3].value, this_title, row[7].value, row[6].value, this_content,
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


def is_valid_text(sentence):
    try:
        sentence.encode('ascii').decode('ascii')
    except:
        return False

    return True


def latin_replace(sentence):
    if sentence == '' or sentence is None:
        return ''

    sentence = sentence.replace("Č", "Ch")
    sentence = sentence.replace("Ć", "C")
    sentence = sentence.replace("Đ", "Dj")
    sentence = sentence.replace("Š", "Sh")
    sentence = sentence.replace("Ž", "Zh")

    sentence = sentence.replace("č", "ch")
    sentence = sentence.replace("ć", "c")
    sentence = sentence.replace("đ", "dj")
    sentence = sentence.replace("š", "sh")
    sentence = sentence.replace("ž", "zh")

    return sentence

if __name__ == "__main__":
    # directories: ../data/xyz
    write_folder_reviews("../data/cg", "../data/filtered/fcg.xlsx")
    write_folder_reviews("../data/bih", "../data/filtered/fbih.xlsx")
    write_folder_reviews("../data/srb", "../data/filtered/fsrb.xlsx")
    write_folder_reviews("../data/filtered", "../data/filtered/fall.xlsx")