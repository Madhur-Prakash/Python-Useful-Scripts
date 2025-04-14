import os
import subprocess
import sys


def create_venv():
    try:
        venv_name = str(input("Enter the name of the virtual environment: ")).strip()
        print("Creating virtual environment...")
        os.system(f'python -m venv "{venv_name}"')
        print("Virtual environment created successfully.")
        res = (f"./{venv_name}/Scripts/activate\n")
        print("To activate the virtual environment type:\n")
        subprocess.Popen(res, shell=True)
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