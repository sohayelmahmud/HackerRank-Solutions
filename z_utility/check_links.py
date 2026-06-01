import os
import re

# File paths
readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
output_path = os.path.join(os.path.dirname(__file__), "broken_links.txt")

if not os.path.exists(readme_path):
    print(f" Error: {readme_path} not found!")
    exit(1)

# Read README.md file content
with open(readme_path, "r", encoding="utf-8") as f:
    html_data = f.read()

# Extract all links inside href="..." or href='...'
links = re.findall(r'href=["\'](.*?)["\']', html_data)

broken_links_list = []

for link in links:
    # Ignore external web links
    if link.startswith("http://") or link.startswith("https://"):
        continue

    # Resolve file path relative to the root folder (where README.md is)
    actual_path = os.path.join(os.path.dirname(readme_path), link)

    if not os.path.exists(actual_path):
        broken_links_list.append(link)

# Write results to broken_links.txt inside child folder
with open(output_path, "w", encoding="utf-8") as out_file:
    if broken_links_list:
        out_file.write(f"Total {len(broken_links_list)} broken links found:\n")
        out_file.write("="*30 + "\n")
        for broken_link in broken_links_list:
            out_file.write(f" {broken_link}\n")
        print(f" Done! {len(broken_links_list)} broken links saved to txt file.")
    else:
        out_file.write("All links are workable! No broken links found.\n")
        print(" All are workable")