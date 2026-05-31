"""
Title                : Generate_Info_From_Folder
Author               : Sohayel Mahmud
Date of Creation     : 24 June 2024
"""


import os
import re
import sys

info_file_name = "30DaysOfCode.txt"


def get_valid_subdomain_name(given_name):
    # used to create folder names (only letters, numbers, underscore)
    return re.sub(r"[^\w]", "", given_name)

def clean_problem_title(title_with_serial):
    """
    removes special characters from the entire title, keeping numbers and letters.
    """
    # [^a-zA-Z0-9\s_] means: remove everything except letters, numbers, spaces, and underscore
    return re.sub(r"[^a-zA-Z0-9\s_]", "", title_with_serial).strip()


def generate_info_from_directory():
    """
    reads sub-folders and files from the current directory and generates
    output in the required format.
    """

    current_directory = os.getcwd()
    output_lines = []

    # os.walk traverses the directory tree
    for root, dirs, files in os.walk(current_directory, topdown=True):

        # skip the current directory, only process sub-folders
        if root == current_directory:
            continue

        # 1. create subdomain name
        subdomain_name = os.path.basename(root)
        problem_titles = []
        files.sort()

        for filename in files:
            # process only code files (e.g., .py, .cpp, .js)
            if filename.endswith(('.py', '.cpp', '.c', '.java', '.js', '.css', '.html')):

                # remove file extension
                base_title = os.path.splitext(filename)[0]

                # cleaning function, apply it if needed
                cleaned_title = base_title

                # enclose in double quotes for output format
                problem_titles.append(f'"{cleaned_title}"')

        # 3. generate output format
        if problem_titles:
            # subdomain name
            output_lines.append(f'{subdomain_name}')

            # list of problems (e.g., ["01 Day 00 Hello World", "02 Data Types", ...])
            output_lines.append(f'[{", ".join(problem_titles)}]')

    # output

    if not output_lines:
        print("error: could not find any subfolders containing code files in the current directory.")
        sys.exit()

    print("--- generated info (copy this for python_info.txt) ---")
    print('\n'.join(output_lines))
    print("-------------------------------------------------------")


if __name__ == "__main__":
    generate_info_from_directory()