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
            f.write("__pycache__\n")
            f.write(".vscode\n")
            f.write("logs\n")

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

def make_working_directory(file_name: str):
    try:
        folder_name = str(input("Enter the name of the folder: ")).strip()
        os.makedirs(folder_name, exist_ok=True)
        os.chdir(folder_name)
        os.makedirs("models", exist_ok=True)
        os.chdir("models")
        with open("__init__.py", "w") as f:
            f.write("# This is the init file for the models directory\n")
            f.close()
        with open("models.py", "w") as f:
            f.write("from pydantic import BaseModel, Field\n")
            f.write("\n")
            f.write("\n")
            f.write("class demo(BaseModel):\n")
            f.write("    pass\n")
            f.close()
            

        os.chdir("..") # Go back to the root directory
        os.makedirs("src", exist_ok=True)
        os.chdir("src")
        with open("__init__.py", "w") as f:
            f.write("# This is the init file for the src directory\n")
            f.close()
        with open(f"{file_name}.py", "w") as f:
            f.write("from fastapi import APIRouter, status\n")
            f.write("from fastapi.exceptions import HTTPException\n")
            f.write("import traceback\n")
            f.write("import os\n")
            f.write("import sys\n")
            f.write("sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n")
            f.write("from models.models import demo\n")
            f.write("from config.database import mongo_client\n")
            f.write("from helpers.utils import create_new_log, setup_logging\n")

        os.chdir("..") # Go back to the root directory
        os.makedirs("config", exist_ok=True)
        os.chdir("config")
        with open("__init__.py", "w") as f:
            f.write("# This is the init file for the config directory\n")
            f.close()
        with open("database.py", "w") as f:
            f.write("from motor.motor_asyncio import AsyncIOMotorClient\n")
            f.write("\n")
            f.write("# MONGO_URI = \"mongodb://localhost:27017\"\n")
            f.write("\n")
            f.write("\n")
            f.write("MONGO_URI = \"mongodb://ec2-44-222-241-47.compute-1.amazonaws.com:27017\"  # --> for aws testing\n")
            f.write("mongo_client = AsyncIOMotorClient(MONGO_URI)\n")
            f.close()

        with open ("redis_config.py", "w") as f:
            f.write("import aioredis\n\n")
            f.write("# redis connection\n")
            f.write("client = aioredis.from_url('redis://default@100.26.150.73:6379', decode_responses=True)  # in production\n")
            f.write("\n")
            f.write("\n")
            f.write("# client = aioredis.from_url('redis://localhost', decode_responses=True)  # in local testing\n")

        os.chdir("..") # Go back to the root directory
        os.makedirs("helpers", exist_ok=True)   
        os.chdir("helpers")
        with open("__init__.py", "w") as f: 
            f.write("# This is the init file for the helpers directory\n")
            f.close()
        with open("utils.py", "w") as f:
            f.write('import logging\n')
            f.write('import requests\n')
            f.write('import os\n')
            f.write('from concurrent_log_handler import ConcurrentRotatingFileHandler\n\n')

            f.write('def create_new_log(log_type: str, message: str, head: str):\n')
            f.write('    url = "https://0xda081649.execute-api.us-east-1.amazonaws.com/Dev/logger/backend/create_new_logs"\n')
            f.write('    log = {\n')
            f.write('         "log_type": log_type,\n')
            f.write('         "message": message}\n')
            f.write('    headers = {\n')
            f.write('        "X-Source-Endpoint": head}\n')
            f.write('    \n')
            f.write('    resp = requests.post(url, json=log, headers=headers)\n')
            f.write('    return resp\n\n\n')

            f.write('def setup_logging():\n')
            f.write('    logger = logging.getLogger("patient_public_profile")\n')
            f.write('    if not logger.hasHandlers():\n')
            f.write('        logger.setLevel(logging.INFO)\n')
            f.write('        log_dir = "logs"\n')
            f.write('        os.makedirs(log_dir, exist_ok=True)\n\n')
            f.write('        file_handler = ConcurrentRotatingFileHandler(\n')
            f.write('            os.path.join(log_dir, "patient_public_profile.log"),\n')
            f.write('            maxBytes=10000,\n')
            f.write('            backupCount=500\n')
            f.write('        )\n')
            f.write('        file_handler.setLevel(logging.INFO)\n\n')
            f.write('        console_handler = logging.StreamHandler()\n')
            f.write('        console_handler.setLevel(logging.INFO)\n\n')
            f.write('        formatter = logging.Formatter(\n')
            f.write('            "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s - %(filename)s - %(lineno)d",\n')
            f.write('            datefmt="%Y-%m-%d %H:%M:%S"\n')
            f.write('        )\n')
            f.write('        file_handler.setFormatter(formatter)\n')
            f.write('        console_handler.setFormatter(formatter)\n\n')
            f.write('        logger.addHandler(file_handler)\n')
            f.write('        logger.addHandler(console_handler)\n')
            f.write('    return logger\n')


        os.chdir("..") # Go back to the root directory
        os.makedirs("tests", exist_ok=True)
        os.chdir("tests")
        with open("__init__.py", "a") as f:
            f.write("# This is the init file for the tests directory\n")
            f.close()
        os.chdir("..") # Go back to the root directory
        os.chdir("..") # Go back to the root directory
        with open("__init__.py", "w") as f:
            f.write("# This is the init file for the root directory\n")
            f.close()
        with open("app.py", "w") as f:
            f.write("from fastapi import FastAPI\n")
            f.write("from fastapi.middleware.cors import CORSMiddleware\n")
            f.write("from starlette.middleware.sessions import SessionMiddleware\n")
            f.write("import os\n")
            f.write("import sys\n")
            f.write("sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n")
            f.write("\n")
            f.write("app = FastAPI()\n")
            f.write("\n")
            f.write(
                "app.add_middleware(\n"
                "    CORSMiddleware,\n"
                "    allow_origins=[\"*\"],  # Configure this appropriately for production\n"
                "    allow_credentials=True,\n"
                "    allow_methods=[\"*\"],\n"
                "    allow_headers=[\"*\"],\n"
                ")\n")
            f.write("\n")
            f.write('app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET_KEY"))\n')

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
    src_file_name = str(input("Enter the name of the source file: ")).strip()
    make_working_directory(src_file_name)
    create_venv()
    print("\n")
    print("Your workspace is ready!")
   
   

if __name__ == "__main__":
    main()