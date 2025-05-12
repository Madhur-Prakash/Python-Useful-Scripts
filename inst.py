import os

def install():
    try:
        print("Installation started... Please be patient.")
        with open("requirements.txt", "w") as f:
            f.write("fastapi[standard]\n")
            f.write("motor\n")
            f.write("kafka-python\n")
            f.write("aioredis\n")
            f.write("concurrent_log_handler\n")
            f.close()
        os.system("pip install -r requirements.txt")
        print("Installation completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your fastapi installation script and try again.")
    finally:
        print("Exiting...")
        print("Happy coding!")
        exit(0)


def main():
    print("Welcome to the FastAPI installation script!")
    print("This script will install FastAPI and some other basic dependencies.")
    install()



if __name__ == "__main__":
    main()

