"""
Title                : Hackerrank_Solution_Blank_File_Creator (Multi-language Commenting)
Original Author      : Ahmedur Rahman Shovon
Modified Author      : Sohayel Mahmud
Date of Modification : 01 June 2026
"""

import datetime
import os
import re
import sys

# User preferred safe input format
input_safe = lambda: sys.stdin.readline().strip()

def valid_name(given_name):
    name_with_underscore = given_name.replace(" ", "_")
    return re.sub(r"[^a-zA-Z0-9_]", "", name_with_underscore)

def write_file_header(title, subdomain, domain, author, created_date, extension):
    """Creates the file header comment block based on language extension."""
    # Check if the file is Python or uses C-style syntax
    if extension == '.py':
        start_comment = "'''\n"
        end_comment = "'''\n"
    else:
        # For .java, .cpp, .c, .js etc.
        start_comment = "/*\n"
        end_comment = " */\n"

    header_str = start_comment
    header_str += "title     : " + title + "\n"
    header_str += "subdomain : " + subdomain + "\n"
    header_str += "domain    : " + domain + "\n"
    header_str += "author    : " + author + "\n"
    header_str += "created   : " + created_date + "\n"
    header_str += end_comment
    return header_str

def main():
    author = "Sohayel Mahmud"
    created_date = datetime.datetime.today().strftime("%d %b, %Y")

    # Get the directory where this script file is physically located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    current_working_dir = os.getcwd()

    # 1. Ask for target root folder name
    print("Enter the target root folder name (will be created in current root): ", end="", flush=True)
    target_root_folder = input_safe()
    target_root_path = os.path.join(current_working_dir, target_root_folder)

    # 2. Ask for folder numbering preference
    print("Do you want folder numbering? (y/n): ", end="", flush=True)
    folder_num_pref = input_safe().lower() == 'y'

    # 3. Ask for file numbering preference
    print("Do you want file numbering? (y/n): ", end="", flush=True)
    file_num_pref = input_safe().lower() == 'y'

    # 4. Ask for info file name (located in the script's own folder)
    print("Enter the info file name (e.g., python_info.txt): ", end="", flush=True)
    info_file_input = input_safe()
    info_file_path = os.path.join(script_directory, info_file_input)

    # 5. Ask for programming language / file extension
    print("Enter the file extension (e.g., .py, .cpp, .java): ", end="", flush=True)
    extension = input_safe()
    if not extension.startswith('.'):
        extension = '.' + extension

    # Infer domain name from extension for the file header
    domain_map = {'.py': 'Python', '.cpp': 'C++', '.c': 'C', '.java': 'Java', '.js': 'JavaScript'}
    domain = domain_map.get(extension, 'Unknown')

    # Read the info file from the script's directory
    try:
        with open(info_file_path, "r") as info_file:
            info_file_lines = info_file.readlines()
    except FileNotFoundError:
        print(f"Error: '{info_file_input}' not found inside script directory: {script_directory}")
        sys.exit()

    # Create the main target root directory if it doesn't exist
    if not os.path.exists(target_root_path):
        os.makedirs(target_root_path)

    folder_count = 0
    i = 0

    # Processing data in pairs (subdomain name + problem list)
    while i < len(info_file_lines):
        line1 = info_file_lines[i].strip()

        # Checking for subdomain name: must not start with '[' and must not be empty
        if not line1.startswith("[") and line1 != "":
            subdomain_name = line1

            if i + 1 < len(info_file_lines):
                line2 = info_file_lines[i + 1].strip()

                # Checking for problem list: must start with '['
                if line2.startswith("["):
                    problem_list = line2

                    # Folder name generation
                    base_folder_name = valid_name(subdomain_name)
                    if folder_num_pref:
                        folder_count += 1
                        serial_number = f'{folder_count:02d}'
                        folder_name = f'{serial_number}_{base_folder_name}'
                    else:
                        folder_name = base_folder_name

                    final_folder_path = os.path.join(target_root_path, folder_name)

                    # Skip if the subfolder already exists
                    if os.path.exists(final_folder_path):
                        print(f"Skipping: Subfolder '{folder_name}' already exists.")
                        i += 2
                        continue

                    # Create subfolder if it does not exist
                    os.makedirs(final_folder_path)

                    # File creation logic
                    title_ar = re.findall(r'("[^"]*")', problem_list)
                    title_ar_len = len(title_ar)

                    for idx, title in enumerate(title_ar):
                        # Pass extension parameter to determine dynamic commenting style
                        file_header_str = write_file_header(title[1:-1], subdomain_name, domain, author, created_date, extension)
                        title_valid = valid_name(title[1:-1])

                        if file_num_pref:
                            file_serial = f'{(idx + 1):02d}'
                            final_file_name = f'{file_serial}_{title_valid}{extension}'
                        else:
                            final_file_name = f'{title_valid}{extension}'

                        # Create and write file safely inside the generated subfolder
                        final_file_path = os.path.join(final_folder_path, final_file_name)
                        with open(final_file_path, "w") as f:
                            f.write(file_header_str)

                    print(f"Folder: {folder_name}. Total files created: {title_ar_len}")
                    i += 2
                    continue
        i += 1

    print("\nSkeleton structure updated successfully with correct commenting syntax!")

if __name__ == "__main__":
    main()