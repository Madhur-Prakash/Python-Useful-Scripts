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

def delete_commit_from_history_locally(head_number: int):
    try:
        os.system(f"git reset --hard HEAD~{head_number}")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_commit_from_history_remotely(head_number: int):
    try:
        os.system(f"git reset --hard HEAD~{head_number}")
        os.system("git push origin main --force")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_help():
    help_text = """
    Git Helper Tool Commands:
    push (p)                     : Push committed changes to the remote repository.
    add (a)                      : Stage all changes for commit.
    commit (c) <message>         : Commit staged changes with the provided message.
    commit-no-edit (cne)         : Amend the last commit without changing its message.
    delete-local (dl) <number>   : Delete the last <number> commits from local history.
    delete-remote (dr) <number>  : Delete the last <number> commits from remote history.
    """
    print(help_text)

def main():
    if len(sys.argv) < 1:
        return
    command = sys.argv[1]
    if command == 'help' or command == '--help' or command == '-h':
        get_help()
        return
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
    elif command == 'dl' or command == 'delete-local':
        if len(sys.argv) < 3:
            print("Please provide the number of commits to delete.")
            return
        if (len(sys.argv) > 3):
            confirm = sys.argv[3]
            if confirm.lower() == '-y':
                try:
                    head_number = int(sys.argv[2])
                    delete_commit_from_history_locally(head_number)
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                return
        else:
            confirm = input(f"Are you sure you want to delete the last {sys.argv[2]} commits locally? This action cannot be undone. (y/n): ")
            if confirm.lower() != 'y':
                return
            head_number = int(sys.argv[2])
            delete_commit_from_history_locally(head_number)
    elif command == 'dr' or command == 'delete-remote':
        if len(sys.argv) < 3:
            print("Please provide the number of commits to delete.")
            return
        if (len(sys.argv) > 3):
            confirm = sys.argv[3]
            if confirm.lower() == '-y':
                try:
                    head_number = int(sys.argv[2])
                    delete_commit_from_history_remotely(head_number)
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                return
        else:
            confirm = input(f"Are you sure you want to delete the last {sys.argv[2]} commits locally? This action cannot be undone. (y/n): ")
            if confirm.lower() != 'y':
                return
            head_number = int(sys.argv[2])
            delete_commit_from_history_remotely(head_number)

if __name__ == "__main__":
    main()
