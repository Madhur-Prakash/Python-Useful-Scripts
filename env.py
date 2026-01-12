import os
from rich import console

console = console.Console()

def read_env_file():
    try:
        # env_lines = []
        if not os.path.exists('.env'):
            console.print("[red]'.env'[/red] [red]file not found[/red]")
            return
        with open('.env', 'r') as env_file:
            env_lines = env_file.readlines()            
            env_var = [line.split('=')[0] for line in env_lines if not line.startswith('#')]
            return(env_var)
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")
        return

def create_env_sample(env_content: str=[]):
    try:
        new_content = [f'{env_var}= "YOUR_{env_var}"' for env_var in env_content]
        with open('.env.sample', 'w') as sample_file:
            sample_file.write('\n'.join(new_content))
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")

def main():
    env_content = read_env_file()
    if env_content:
        create_env_sample(env_content)

if __name__ == "__main__":
    main()