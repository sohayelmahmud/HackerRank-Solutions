"""
Title                : Hackerrank_Solution_Lister
Subdomain            : None
Domain               : None
Original Author      : Ahmedur Rahman Shovon
Modified Author      : Sohayel Mahmud
Date of Creation     : 12 July 2017
Date of Modification : 24 June 2024
"""

import os
import re
import sys

info_file_name = "python_info.txt" # Adjust this path as needed

# valid name generator
def valid_name(given_name):
    name_with_underscore = given_name.replace(" ", "_")
    return re.sub(r"[^a-zA-Z0-9_]", "", name_with_underscore)


# main code
problem_list = ""
subdomain_name = ""
extension = ".py"
output_file_name = "solution_list.md" # Adjust this extension as needed

base_path = "Python/" # Adjust this path as needed

# read info file
try:
    info_file = open(info_file_name, "r")
    info_file_lines = info_file.readlines()
    info_file.close()
except FileNotFoundError:
    print(f"error: '{info_file_name}' not found. please create the info file.")
    sys.exit()

# create output file
f = open(output_file_name, "w")
f.write("\n")

# process info file lines
folder_count = 0
i = 0
# loop for serializing folders --- remove this if not needed
while i < len(info_file_lines):
    line1 = info_file_lines[i].strip()

    if not line1.startswith("[") and line1 != "":
        subdomain_name = line1

        if i + 1 < len(info_file_lines):
            line2 = info_file_lines[i + 1].strip()

            if line2.startswith("["):
                problem_list = line2

                # increment folder count --- remove this if not needed
                folder_count += 1
                folder_serial = f'{folder_count:02d}'

                base_folder_name = get_valid_name(subdomain_name)
                folder_name = f'{folder_serial}_{base_folder_name}'

                title_ar = re.findall(r'("[^"]*")', problem_list)

                # output --- will be changed as per requirement
                f.write("\n\n- **" + subdomain_name + "**\n")

                for idx, title in enumerate(title_ar):
                    file_serial = f'{(idx + 1):02d}'
                    filename_base = get_valid_name(title[1:-1])
                    filename_with_serial = f'{file_serial}_{filename_base}'
                    filepath = base_path + folder_name + "/" + filename_with_serial + extension
                    f.write("   - [" + title[1:-1] + "](" + filepath + ")\n")

                i += 2 # skip next line as it's already processed
                continue

    i += 1 # move to next line

# finalize output file
f.close()
print("List generated successfully. Open " + output_file_name + " to view.")