# Project File Automation Tools

This is a set of simple Python utility scripts designed to keep your coding projects perfectly organized, regardless of the platform or language.

The tools automate the setup, naming, and documentation process for any structured collection of files.

---

## The 3 Scripts

These three scripts work together using the `info.txt` file as their central data source.

### 1. `Generate_Info_From_Folder.py` (Data Generator)
* **What it does:** Scans your existing project folders and files, and prints the data in the required `info.txt` format (`Folder Name` followed by a `["File 1", "File 2"]` list).
* **Run When:** You need to update your data file from your current directory structure.
* **Use Case:** Perfect for when you've manually created folders and files and want to generate the `info.txt` for further automation to make clickable documentation for README files..

### 2. `Blank_File_Creator.py` (Project Creator)
* **What it does:** Reads the `info.txt` file and automatically creates all necessary, serial-numbered project folders (e.g., `01_Basics`) and solution files (e.g., `01_Problem_Title.py`).
* **Run When:** You need to create a large number of empty files and folders for a new section of your project.
* **Use Case:** Ideal for bootstrapping new coding projects or sections where you want a consistent structure without manually creating each file.

### 3. `Folder_and_File_Lister.py` (Documentation Lister)
* **What it does:** Reads the `info.txt` data and generates a `project_list.md` file. This file contains **clickable Markdown links** for every single file you created.
* **Run When:** You need to generate the final, clean list of all your work for documentation or sharing.
* **Use Case:** Great for GitHub README files! It'll make your readme look super organized and professional.

---

## Customization
You can easily customize the scripts to fit your specific needs. I commented the key sections in each script where you can make changes:

- **Data Format:** Modify the `info.txt` format if you have a different way of organizing your project data.
- **File Extensions:** Change the file extensions in `file_creator.py` to match your programming language (e.g., `.js`, `.java`, etc.).
- **Header Templates:** Modify the header templates in `file_creator.py` to include your name, date, or any other metadata you want at the top of each file.
- **Directory Structure:** Change the folder and file naming conventions in `file_creator.py` to match your project's requirements. (e.g., adding prefixes, suffixes, numerical serialization etc.).
- **Output Formats:** Adjust the output format in `project_lister.py` to suit your documentation style.
- **Link Style:** Change how links are formatted in `project_lister.py` (e.g., relative vs absolute paths).



---

## Quick Start


1. Make your `info.txt` file with the Generator script if you don't already have one.
2.  Place your project data in `info.txt`.
3.  Run the appropriate script to create files or documentation.


---

##  Feedback

If you have any feedback or ideas to improve this project, feel free to contact me via

<a href="https://www.linkedin.com/in/sohayelmahmud/">
  <img align="left" alt="Sohayel's Linkdein" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />

</a>
<a href="https://github.com/sohayelmahmud">
  <img align="left" alt="Sohayel's Github" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" />
</a>
<a href="https://www.facebook.com/sohayel.mahmud.7/">
  <img align="left" alt="Sohayel's Facebook" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/facebook.svg" />
</a>