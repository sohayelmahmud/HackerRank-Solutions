import os
import sys

# Fast I/O
input = lambda: sys.stdin.readline()
def out(x): sys.stdout.write(str(x) + '\n')

def format_title_from_name(name):
    # Remove extension if present
    base_name = os.path.splitext(name)[0]
    # Remove leading numbers and underscores (e.g., '01_Introduction' -> 'Introduction')
    # Also replaces underscores with spaces for clean display
    clean_name = base_name.split('_', 1)[-1] if '_' in base_name and base_name.split('_', 1)[0].isdigit() else base_name
    return clean_name.replace('_', ' ')

def generate_nested_list(target_folder):
    # Base directory is the parent of this utility script
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    target_path = os.path.join(root_dir, target_folder)

    if not os.path.exists(target_path):
        out(f"Error: Folder '{target_folder}' not found at {target_path}")
        return

    output_lines = []

    # Main parent tag for the language/folder
    output_lines.append("<details>")
    output_lines.append(f"  <summary><b>{target_folder}</b></summary>\n  \n  <blockquote>")

    # Get all items in the target directory and sort them to keep order (01_, 02_, etc.)
    try:
        sub_items = sorted(os.listdir(target_path))
    except Exception as e:
        out(f"Error reading directory: {e}")
        return

    for item in sub_items:
        item_path = os.path.join(target_path, item)

        # Process sub-directories as Topics
        if os.path.isdir(item_path):
            # Skip hidden folders or venv if any
            if item.startswith('.') or item == "venv":
                continue

            topic_title = format_title_from_name(item)
            output_lines.append(f"   <!-- {topic_title} -->")
            output_lines.append(f"   <details>")
            output_lines.append(f"      <summary>{topic_title}</summary>")
            output_lines.append(f"      <ol>")

            # Read and sort files inside the sub-directory
            files = sorted(os.listdir(item_path))
            for file in files:
                file_path = os.path.join(item_path, file)
                if os.path.isfile(file_path):
                    file_title = format_title_from_name(file)
                    # Create the relative link from the repository root
                    rel_link = f"{target_folder}/{item}/{file}"
                    output_lines.append(f'        <li><a href="{rel_link}">{file_title}</a></li>')

            output_lines.append(f"      </ol>")
            output_lines.append(f"   </details>\n")

    output_lines.append("  </blockquote>\n</details>")

    # Write output to a local txt file
    output_file = os.path.join(os.path.dirname(__file__), "generated_repo_structure.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    out(f"Successfully generated nested list inside '{os.path.basename(output_file)}'!")

def solve():
    sys.stdout.write("Enter root folder name to generate list (e.g., Python, 30DaysOfCode): ")
    sys.stdout.flush()
    target_folder = sys.stdin.readline().strip()

    if target_folder:
        generate_nested_list(target_folder)

if __name__ == "__main__":
    solve()