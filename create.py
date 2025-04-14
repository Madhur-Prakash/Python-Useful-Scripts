import os

def create_venv():
    try:
        venv_name = str(input("Enter the name of the virtual environment: ")).strip()
        print("Creating virtual environment...")
        os.system(f'python -m venv "{venv_name}"')
        print("Virtual environment created successfully.")

        if not os.path.exists(".gitignore"):
            open(".gitignore", "w").close()
        with open(".gitignore", "rb+") as f:
            f.seek(0, os.SEEK_END)
            if f.tell() > 0:
                f.seek(-1, os.SEEK_END)
                last_char = f.read(1)
                if last_char != b'\n':
                    f.write(b'\n')

    # Now append the venv name
        with open(".gitignore", "a", encoding="utf-8") as f:
            f.write(f"{venv_name}\n")

        print(f"Added '{venv_name}' to .gitignore")
        res = (f"./{venv_name}/Scripts/activate\n")
        print("To activate the virtual environment type:\n")
        print(res)
        print("Exiting...")
        print("Happy coding!")
    
    except Exception as e:  
        print(f"An error occurred: {e}")
        print("Please check your Python installation and try again.")
        print("Exiting...")

def main():
    print("Welcome to the Virtual Environment Setup Script!")
    print("This script will help you create and activate a virtual environment.")
    print("Please follow the prompts.")
    print("\n")
    create_venv()
    

if __name__ == "__main__":
    main()