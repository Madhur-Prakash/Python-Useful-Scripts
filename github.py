import os

def push_pull():
    try:

        os.system("git checkout Dev")
        os.system("git pull")
        os.system("git checkout main")
        os.system("git pull")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your Github and try again.")

    finally:
        os.system("git checkout Dev")
        print("Exiting...")
        print("Happy coding!")
        exit(0)


def push_to_github():
    try:
        os.system("git add .")
        print("Added all changes to staging area.")
        commit_message = str(input("Enter commit message: ")).strip()
        os.system(f'git commit -m "{commit_message}"')
        print("Committed changes.")
        os.system("git push -u origin Dev")
        print("Pushed changes to remote repository.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your Github and try again.")

    finally:
        os.system("git checkout Dev")
        print("Exiting...")
        print("Happy coding!")
        exit(0)

def push_to_personal():
    try:
        os.system("git add .")
        print("Added all changes to staging area.")
        commit_message = str(input("Enter commit message: ")).strip()
        os.system(f'git commit -m "{commit_message}"')
        print("Committed changes.")
        os.system("git push")
        print("Pushed changes to personal repository.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your Github and try again.")

    finally:
        print("Exiting...")
        print("Happy coding!")
        exit(0)


def clone_repo():
    try:
        repo_url = str(input("Enter the repository URL: ")).strip()
        os.system(f"git clone {repo_url}")
        print("Cloned the repository successfully.")
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        print(f"Repository name: {repo_name}")
        os.chdir(repo_name)
        print(f"Changed directory to {repo_name}.\n")

        print("Do you want to open the repository in VS Code? (yes/no)")
        open_in_vscode = str(input()).strip().lower()
        if open_in_vscode == "yes" or open_in_vscode == "y":
            os.system("code .")
            print("Opened the repository in VS Code.")
        else:
            print("Exiting...")
            print("Happy coding!")
            exit(0)

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your Github and try again.")

    finally:
        print("\n")
        print("Exiting...")
        print("Happy coding!")
        exit(0)


def setup_new_repo():
    try:
        os.system("git init")
        os.system("git add .")
        print("Added all changes to staging area.")
        commit_message = str(input("Enter commit message: ")).strip()
        os.system(f'git commit -m "{commit_message}"')
        print("Committed changes.")
        remote_origin_link = str(input("Enter the remote origin link: ")).strip()
        os.system(f'git remote add origin "{remote_origin_link}"')
        print("Added remote origin.")
        os.system("git branch -M main")
        print("Renamed branch to main.")
        os.system("git push -u origin main")
        print("Pushed changes to main branch.\n")
        print("Repository setup successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your Github and try again.")

    finally:
        print("Exiting...")
        print("Happy coding!")
        exit(0)

def main():
    print("Welcome to the GitHub Pull and Push Script")
    print("This script will help you pull and push changes to your remote repository.")
    print("Please make sure you have a stable internet connection.\n")
    print("- Enter 1 if you want to pull from your organization repo.")
    print("- Enter 2 if you want to push to your organization repo.")
    print("- Enter 3 if you want to push to your personal repo.")
    print("- Enter 4 if you want to clone a new repo.")
    print("- Enter 5 if you want to setup a new repo.\n")
    print("Note: Please ensure you have Git installed and configured on your system.")

    choice = str(input("Enter the choice: ")).strip().lower()

    if choice == "1":
        print("Pulling from organization repo... Please be patient.")
        push_pull()
    elif choice == "2":
        print("Pushing to organisation repo... Please be patient.")
        push_to_github()
    elif choice == "3":
        print("Pushing to personal repo... Please be patient.")
        push_to_personal()
    elif choice == "4":
        print("Cloning the repo... Please be patient.")
        clone_repo()
    elif choice == "5":
        print("Setting up new repository... Please be patient.")
        setup_new_repo()
    else:
        print("Invalid choice. Please enter 'pull' or 'push'.")
        exit(1)

if __name__ == "__main__":
    main()


