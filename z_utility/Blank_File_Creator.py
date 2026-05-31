"""
Title                : Hackerrank_Solution_Blank_File_Creator
Subdomain            : None
Domain               : None
Original Author      : Ahmedur Rahman Shovon
Modified Author      : Sohayel Mahmud
Date of Creation     : 12 July 2017
Date of Modification : 24 June 2024
"""

import datetime
import os
import re
import sys

# global configurations
extension = ".py"
domain = "Python"
author = "Sohayel Mahmud"
created_date = datetime.datetime.today().strftime("%d %b, %Y")
info_file_name = "python_info.txt"


def valid_name(given_name):
    name_with_underscore = given_name.replace(" ", "_")
    return re.sub(r"[^a-zA-Z0-9_]", "", name_with_underscore)


def write_file_header(title, subdomain):
    """creates the file header comment block."""
    header_str = "'''\n"
    header_str += "title     : " + title + "\n"
    header_str += "subdomain : " + subdomain + "\n"
    header_str += "domain    : " + domain + "\n"
    header_str += "author    : " + author + "\n"
    header_str += "created   : " + created_date + "\n"
    header_str += "'''\n"
    return header_str


# main program logic

try:
    info_file = open(info_file_name, "r")
    info_file_lines = info_file.readlines()
    info_file.close()
except FileNotFoundError:
    print(f"error: '{info_file_name}' not found. please create the info file.")
    sys.exit()

# folder counter initialization
folder_count = 0
i = 0

# processing data in pairs (subdomain name + problem list)
while i < len(info_file_lines):
    line1 = info_file_lines[i].strip() # line 1: subdomain name

    # checking for subdomain name: must not start with '[' and must not be empty
    if not line1.startswith("[") and line1 != "":
        subdomain_name = line1

        # checking if the next line (problem list) exists
        if i + 1 < len(info_file_lines):
            line2 = info_file_lines[i + 1].strip() # line 2: problem list

            # checking for problem list: must start with '['
            if line2.startswith("["):
                problem_list = line2

                # --- folder creation logic ---

                # incrementing folder counter and creating serial number (01, 02, ...)
                folder_count += 1
                serial_number = f'{folder_count:02d}'

                base_folder_name = valid_name(subdomain_name)
                # creating final folder name with serial number
                folder_name = f'{serial_number}_{base_folder_name}'

                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)

                # --- file creation logic ---

                # extracting titles enclosed in double quotes
                title_ar = re.findall(r'("[^"]*")', problem_list)
                title_ar_len = len(title_ar)

                # iterating to create files with sequential numbering
                for idx, title in enumerate(title_ar):

                    # creating file serial number (01, 02, ...)
                    file_serial = f'{(idx + 1):02d}'

                    file_header_str = write_file_header(title[1:-1], subdomain_name)
                    title_valid = valid_name(title)

                    # creating final file name: serial_name.py
                    final_file_name = f'{file_serial}_{title_valid}{extension}'

                    # opening and writing to the file using os.path.join for safety
                    f = open(os.path.join(folder_name, final_file_name), "w")
                    f.write(file_header_str)
                    f.close()

                print(f"Folder: {folder_name}. total files created: {title_ar_len}")

                i += 2 # successfully processed two lines (subdomain + problem list)
                continue

    i += 1 # moving to the next line if the current one didn't match the pair logic