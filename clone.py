import os

def clone_org_repo():
    try:
        #  appointments
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Appointments.git")
        os.chdir("CuraDocs_Appointments")
        os.system("github 1")
        os.chdir("..")

        #  get_request
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Get_Request.git")
        os.chdir("CuraDocs_Get_Request")
        os.system("github 1")
        os.chdir("..")

        #  connect
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Connect.git")
        os.chdir("CuraDocs_Connect")
        os.system("github 1")
        os.chdir("..")

        #  patient public profile
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Patient_Public_Profile.git")
        os.chdir("CuraDocs_Patient_Public_Profile")
        os.system("github 1")
        os.chdir("..")

        #  doctor public profile    
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Doctor_Public_Profile.git")
        os.chdir("CuraDocs_Doctor_Public_Profile")
        os.system("github 1")
        os.chdir("..")

        #  doctor search
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Doctor_Search.git")
        os.chdir("CuraDocs_Doctor_Search")
        os.system("github 1")
        os.chdir("..")

        #  internal search
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Internal_Search.git")
        os.chdir("CuraDocs_Internal_Search")
        os.system("github 1")
        os.chdir("..")

        # auth
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Auth.git")
        os.chdir("CuraDocs_Auth")
        os.system("github 1")
        os.chdir("..")

        #  pdf to json
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Pdf_json_api.git")
        os.chdir("CuraDocs_Pdf_json_api")
        os.system("github 1")
        os.chdir("..")

        #  img to json
        os.system("git clone git@github.com:CuraDocs/CuraDocs_img_json_api.git")
        os.chdir("CuraDocs_img_json_api")
        os.system("github 1")
        os.chdir("..")

        #  report problem
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Report_Problem.git")
        os.chdir("CuraDocs_Report_Problem")
        os.system("github 1")
        os.chdir("..")

        #  timeline
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Timeline.git")
        os.chdir("CuraDocs_Timeline")
        os.system("github 1")
        os.chdir("..")

        #  private profile
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Profile.git")
        os.chdir("CuraDocs_Profile")
        os.system("github 1")
        os.chdir("..")
        
        #  basic info
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Basic_Medical_Info.git")
        os.chdir("CuraDocs_Basic_Medical_Info")
        os.system("github 1")
        os.chdir("..")
        
        #  summary
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Summary.git")
        os.chdir("CuraDocs_Summary")
        os.system("github 1")
        os.chdir("..")

        #  logging
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Logging.git")
        os.chdir("CuraDocs_Logging")
        os.system("github 1")
        os.chdir("..")

        #  auth beta
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Auth_Beta.git")
        os.chdir("CuraDocs_Auth_Beta")
        os.system("github 1")
        os.chdir("..")

        #  message
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Message.git")
        os.chdir("CuraDocs_Message")
        os.system("github 1")
        os.chdir("..")

        #  profile qr
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Profile_Qr.git")
        os.chdir("CuraDocs_Profile_Qr")
        os.system("github 1")
        os.chdir("..")

        # medical records
        os.system("git clone git@github.com:CuraDocs/CuraDocs_Medical_Records.git")
        os.chdir("CuraDocs_Medical_Records")
        os.system("github 1")
        os.chdir("..")
        
    
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your repo clonning script and try again.")
    
    finally:
        print("Exiting...")
        print("Happy coding!")
        exit(0)


def main():
    print("Welcome to the CuraDocs repository cloning script!")
    print("This script will clone all the necessary repositories for you.")
    print("---------------------------------------")
    print("---------------------------------------")
    print("Note:")
    print("     Please make sure you have access to the repositories.")
    print("     Please make sure you are in the correct directory to clone the repositories.")
    print("     Please ensure you have Git installed and configured on your system.")
    print("----------------------------------------")
    print("----------------------------------------")
    print("Starting the cloning process...Please be patient.")
    print("This may take a while depending on your internet connection.")
    clone_org_repo()
    print("----------------------------------------")
    print("----------------------------------------")
    print("All repositories have been cloned successfully!")
    print("----------------------------------------")
    print("----------------------------------------")


if __name__ == "__main__":
    main()