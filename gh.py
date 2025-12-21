import os
import sys


def commit(msg: str):
    try:
        os.system(f'git commit -m "{msg}"')
    except Exception as e:
        print(f"An error occurred: {e}")

def add_all():
    try:
        os.system("git add .")
    except Exception as e:
        print(f"An error occurred: {e}")

def push(): 
    try:
        os.system("git push -u origin main")
    except Exception as e:
        print(f"An error occurred: {e}")

def commit_no_edit():
    try:
        os.system("git add .")
        os.system('git commit --amend --no-edit')
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) < 1:
        return
    command = sys.argv[1]
    if command == 'push' or command == 'p':
        push()
    elif command == 'add' or command == 'a':
        add_all()

    elif command == 'commit' or command == 'c':
        if len(sys.argv) < 3:
            print("Please provide a commit message.")
            return
        msg = sys.argv[2]
        commit(msg)
    elif command == 'cne' or command == 'commit-no-edit':
        commit_no_edit()

if __name__ == "__main__":
    main()
