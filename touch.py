import os
import sys

def make_new_file(*args):
    try:
        for file in args:
            with open(file, "w") as f:
                pass
    except Exception as e:
        print(f"An error occurred while creating the file {file}: {e}")
        return False
        

def main():
    if(len(sys.argv) < 2):
        print("File name must be provided")
    file_to_create = sys.argv[1:]
    make_new_file(*file_to_create)

if __name__ == "__main__":
    main()
    