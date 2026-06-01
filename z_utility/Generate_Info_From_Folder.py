"""
Title                : Generate_Info_From_Folder (Dynamic Name & Path)
Author               : Sohayel Mahmud
Date of Modification : 01 June 2026
"""

import os
import re
import sys

# User preferred safe input format
input_safe = lambda: sys.stdin.readline().strip()

def valid_name(given_name):
    return re.sub(r"[^\w]", "", given_name)

def generate_info_from_directory():
    # Prompt the user to enter the target folder name from the root
    print("Enter the target folder name from root (e.g., Python, 30DaysOfCode): ", end="", flush=True)
    target_folder = input_safe()

    # Get the absolute path of the directory where this script file actually resides
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Assuming the target folder is located in the current working directory
    current_working_dir = os.getcwd()
    target_path = os.path.join(current_working_dir, target_folder)

    # Check if the requested folder actually exists
    if not os.path.exists(target_path) or not os.path.isdir(target_path):
        print(f"Error: Folder '{target_folder}' not found in the current working directory.")
        sys.exit()

    output_lines = []

    # Traverse only through the sub-folders of the specified target directory
    for root, dirs, files in os.walk(target_path, topdown=True):

        # Skip the root of the target directory to only process its children
        if root == target_path:
            continue

        subdomain_name = os.path.basename(root)
        problem_titles = []
        files.sort()

        for filename in files:
            # Filter valid code file extensions
            if filename.endswith(('.py', '.cpp', '.c', '.java', '.js', '.css', '.html')):
                # Remove file extension to extract the base title
                base_title = os.path.splitext(filename)[0]
                problem_titles.append(f'"{base_title}"')

        if problem_titles:
            # Format output lines to match info specification
            output_lines.append(f'{subdomain_name}')
            output_lines.append(f'[{", ".join(problem_titles)}]\n')

    if not output_lines:
        print(f"Error: Could not find any subfolders containing code files inside '{target_folder}'.")
        sys.exit()

    # Generate the output filename dynamically based on the target folder's name
    output_file_name = f"{target_folder}_info.txt"

    # Define the final output path strictly inside the script's own folder
    output_file_path = os.path.join(script_directory, output_file_name)

    with open(output_file_path, "w") as f:
        f.write('\n'.join(output_lines))

    print(f"\nSuccess! '{output_file_name}' has been generated and saved in the script's folder.")

if __name__ == "__main__":
    generate_info_from_directory()