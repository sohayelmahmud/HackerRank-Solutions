"""
Title     : Hackerrank Solution Lister
Subdomain : None
Domain    : None
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2017
"""

import os
import re
import sys

info_file_name = "python_info.txt"


def get_valid_name(given_name):
    return re.sub(r"[^\w]", "", given_name)


problem_list = ""
subdomain_name = ""
extension = ".py"
output_file_name = "solution_list.html"

try:
    info_file = open(info_file_name, "r")
    info_file_lines = info_file.readlines()
    info_file.close()
except FileNotFoundError:
    print(f"error: '{info_file_name}' not found. please create the info file.")
    sys.exit()

f = open(output_file_name, "w")
f.write("\n")

folder_count = 0

i = 0
while i < len(info_file_lines):
    line1 = info_file_lines[i].strip()

    if not line1.startswith("[") and line1 != "":
        subdomain_name = line1

        if i + 1 < len(info_file_lines):
            line2 = info_file_lines[i + 1].strip()

            if line2.startswith("["):
                problem_list = line2

                folder_count += 1
                folder_serial = f'{folder_count:02d}'

                base_folder_name = get_valid_name(subdomain_name)
                folder_name = f'{folder_serial}_{base_folder_name}'

                title_ar = re.findall(r'("[^"]*")', problem_list)

                f.write("\n\n- **" + subdomain_name + "**\n")

                for idx, title in enumerate(title_ar):

                    file_serial = f'{(idx + 1):02d}'
                    filename_base = get_valid_name(title[1:-1])

                    filename_with_serial = f'{file_serial}_{filename_base}'

                    filepath = folder_name + "/" + filename_with_serial + extension

                    f.write("   - [" + title[1:-1] + "](" + filepath + ")\n")

                i += 2
                continue

    i += 1

f.close()
print("List generated successfully. Open " + output_file_name + " to view.")