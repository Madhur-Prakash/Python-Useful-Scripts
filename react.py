import os

def react_app():
    os.system("npm create vite@latest . -- --template react")

def main():
    print("Welcome to the React app creation tool!")
    print("This script will help you create a new React app using Vite.")
    print("\n")
    
    try:
        react_app()
        print("\n")
        print("React app created successfully!")
        print("Installing dependencies... Please be patient.")
        print("This may take a while depending on your internet connection.")
        os.system("npm install")
        print("Dependencies installed successfully!")

        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your setup and try again.")
    
    finally:
        print("\n")
        print("Exiting...")
        print("Happy coding!")
    
if __name__ == "__main__":
    main()