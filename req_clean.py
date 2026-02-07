import os

from rich import console

console = console.Console()

def clean_requirements_file():
    try:
        if not os.path.exists('requirements.txt'):
            console.print("[red]'requirements.txt file not found'[/red]")
            return

        with open('requirements.txt', 'r', encoding='utf-16') as req_file:
            lines = req_file.readlines()

        cleaned_lines = []
        for line in lines:
            stripped = line.strip()
            splitted = stripped.split('==') # split on '==' to separate package name from version, if version is specified
            
            # if there was an '==' in the line, take only the first part (the package name), otherwise take the whole line
            eq_removed = splitted[0].strip() if len(splitted) > 1 else stripped 
            if not stripped or stripped.startswith('#'):
                cleaned_lines.append(line.rstrip())
                continue
            cleaned_lines.append(eq_removed)

        with open('requirements.txt', 'w', encoding='utf-16') as req_file:
            req_file.write('\n'.join(cleaned_lines))

        console.print("[green]requirements.txt cleaned successfully[/green]")

    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

def main():
    clean_requirements_file()

if __name__ == "__main__":
    main()