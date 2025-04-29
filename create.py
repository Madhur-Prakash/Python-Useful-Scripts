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
            f.write("_pycache_\n")

        print(f"Added '{venv_name}' to .gitignore")
        res = (f"./{venv_name}/Scripts/activate\n")
        print("To activate the virtual environment type:\n")
        print(res)
        print("Exiting...")
        print("Happy coding!")
    
    except Exception as e:  
        print(f"An error occurred: {e}")
        print("Please check your Python installation and try again.")
        
    finally:
        print("\n")
        print("Exiting...")
        print("Happy coding!")
        exit(0)

def make_working_directory():
    try:
        with open("__init__.py", "w") as f:
            f.write("# This is the init file for the root directory\n")
            f.close()
        with open("app.py", "w") as f:
            f.write("from fastapi import FastAPI\n")
            f.write("\n")
            f.write("app = FastAPI()\n")

        os.makedirs("models", exist_ok=True)
        os.chdir("models")
        with open("__init__.py", "w") as f:
            f.write("# This is the init file for the models directory\n")
            f.close()
        with open("models.py", "w") as f:
            f.write("from pydantic import BaseModel, Field\n")
            f.close()
            

        os.chdir("..") # Go back to the root directory
        os.makedirs("src", exist_ok=True)
        os.chdir("src")
        with open("__init__.py", "w") as f:
            f.write("# This is the init file for the src directory\n")
            f.close()

        os.chdir("..") # Go back to the root directory
        os.makedirs("config", exist_ok=True)
        os.chdir("config")
        with open("__init__.py", "w") as f:
            f.write("# This is the init file for the config directory\n")
            f.close()
        with open("database.py", "w") as f:
            f.write("from motor.motor_asyncio import AsyncIOMotorClient\n")
            f.write("\n")
            f.write("MONGO_URI = \"mongodb://localhost:27017\"\n")
            f.write("\n")
            f.write("\n")
            f.write("client = AsyncIOMotorClient(MONGO_URI)\n")
            f.close()

        os.chdir("..") # Go back to the root directory
        os.makedirs("helpers", exist_ok=True)   
        os.chdir("helpers")
        with open("__init__.py", "w") as f: 
            f.write("# This is the init file for the helpers directory\n")
            f.close()
        with open("utils.py", "w") as f:
            f.close()

        os.chdir("..") # Go back to the root directory
        os.makedirs("tests", exist_ok=True)
        os.chdir("tests")
        with open("__init__.py", "a") as f:
            f.write("# This is the init file for the tests directory\n")
            f.close()
        os.chdir("..") # Go back to the root directory


    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your directory creation and try again.")

    finally:
        print("\n")
        print("Exiting...")
        print("Happy coding!")



def main():

    print("Welcome lazy User!")
    print("This script will help you create and setup a python workspace.")
    print("Please follow the prompts.")
    print("\n")
    make_working_directory()
    create_venv()
    print("\n")
    print("Your workspace is ready!")
   
   

if __name__ == "__main__":
    main()