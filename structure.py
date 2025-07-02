import os
import sys

FILE_COMMENTS = {
    "app.py": "main FastAPI app",
    "README.md": "Project documentation",
    ".gitignore": "gitignore file for GitHub",
    "__init__.py": "initializes package",
    "log.py": "main logic",
    "models.py": "models"
}

IGNORED_FILES = [".git", "__pycache__", ".DS_Store", ".vscode", "node_modules", ".pytest_cache", "logs", "venv", "FOLDER_STRUCTURE.md", "dist", "build"]

def ignore_files(venv: str = "venv"):
    ignore_file = list(str(input("Any specific file to ignore? Please provide a list of files separated by commas: ")).split(","))
    if venv:
        # Add venv to the list, not extend with venv as a string
        ignore_file.append(venv)
    ignore_file = [file.strip() for file in ignore_file if file.strip()]  # Clean up the list
    ignore_file.extend(IGNORED_FILES)  # Add default ignored files - don't assign the result
    return ignore_file

def draw_tree_to_md(dir_path, prefix="", output=[], function_output=None):
    try:
        files = sorted(os.listdir(dir_path))
    except PermissionError:
        return output  # Skip inaccessible directories
        
    for index, file in enumerate(files):
        path = os.path.join(dir_path, file)
        file_name = str(files[index])
        
        # Make sure function_output is iterable before checking
        ignored_files = function_output if function_output is not None else []
        
        if file_name in ignored_files:
            continue
        connector = "└── " if index == len(files) - 1 else "├── "
        comment = FILE_COMMENTS.get(file, "")
        comment_str = f"  # {comment}" if comment else ""
        output.append(f"{prefix}{connector}{file}{comment_str}")

        if os.path.isdir(path):
            extension = "    " if index == len(files) - 1 else "│   "
            draw_tree_to_md(path, prefix + extension, output, function_output)

    return output

def main():
    venv = str(input("Enter the name of your virtual environment (default: venv): ") or "venv")
    root_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    folder_name = os.path.basename(root_dir.rstrip("/\\"))
    ignored_files = ignore_files(venv)
    
    print(f"Generating folder structure for: {root_dir}")
    lines = [f"{folder_name}/"]
    lines += draw_tree_to_md(root_dir, function_output=ignored_files)

    md_output = "```\n" + "\n".join(lines) + "\n```"
    with open("FOLDER_STRUCTURE.md", "w", encoding="utf-8") as f:
        f.write(md_output)

    print("\n✅ Folder structure saved as 'FOLDER_STRUCTURE.md'")

if __name__ == "__main__":
    main()