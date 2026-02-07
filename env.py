import os
from rich import console

console = console.Console()


def create_env_sample():
    try:
        if not os.path.exists('.env'):
            console.print("[red]'.env file not found'[/red]")
            return

        output_lines = []

        with open('.env', 'r') as env_file:
            for line in env_file:

                stripped = line.strip()

                # Keep comments & empty lines unchanged
                if not stripped or stripped.startswith('#'):
                    output_lines.append(line.rstrip())
                    continue

                # Process env variable lines
                if '=' in line:
                    key, _ = line.split('=', 1)

                    key = key.strip()

                    new_line = f"{key} = \"YOUR_{key}\""
                    output_lines.append(new_line)

                else:
                    # Fallback: keep line unchanged
                    output_lines.append(line.rstrip())

        with open('.env.sample', 'w') as sample_file:
            sample_file.write('\n'.join(output_lines))

        console.print("[green].env.sample created successfully[/green]")

    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")


def main():
    create_env_sample()


if __name__ == "__main__":
    main()