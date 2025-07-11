import os


def start_auth_containers():
    try:
        print("Starting authentication... Please be patient.")
        os.system("docker start bc601") # -> for mailhog
        os.system("docker start b4683") # -> for redis
        os.system("docker start 77d33") # -> for kafka 
        os.system("docker start 6e4e8") # -> for zookeper

        inp = str(input("Do you want to start the containers for logging? (y/n): ")).strip().lower()
        if inp == "y":
            os.system("docker start 9ffd9") # -> for logging
        elif inp == "n":
            print("Skipping logging container startup.")
        print("All containers started successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your Docker setup and try again.")
    
    finally:
        print("\n")
        print("Exiting...")
        print("Happy coding!")
        exit(0)

def stop_auth_containers():
    try:
        print("Stopping authentication... Please be patient.")
        os.system("docker stop bc601") # -> for mailhog
        os.system("docker stop b4683") # -> for redis
        os.system("docker stop 77d33") # -> for kafka 
        os.system("docker stop 6e4e8") # -> for zookeper
        os.system("docker stop 9ffd9") # -> for logging
        print("All containers stopped successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your Docker setup and try again.")
    
    finally:
        print("\n")
        print("Exiting...")
        print("Happy coding!")
        exit(0)

def main():
    print("Welcome to the Docker container startup script!")
    print("This script will help you start your Docker container.")
    ch = str(input("Do you want to start or stop the containers? (start/stop): ")).strip().lower()
    if ch == "start" or ch.__contains__("rt"):
        start_auth_containers()
    elif ch == "stop" or ch.__contains__("op"):
        stop_auth_containers()
    else:
        print("Invalid choice. Please enter 'start' or 'stop'.")
        exit(1)
   


if __name__ == "__main__":
    main()