import readAndParseExcel as rp
import createXML as cx
import os

def clear_bash():
    os.system("cls")
    
def show_current_directory():
    # PWD - shows current path
    currentDir = os.getcwd()
    print(f"Current directory: {currentDir}")

def list_directory_files():
    # Lists all items in a folder and numerotates them from 1
    files = os.listdir()

    print("\nListing all files in current directory.")
    for name, number in zip(files, range(1, len(files) + 1)):
        print(f"\t{number}. {name}")
    print()

    return files

def change_directory():
    # Function that changes the os working directory 
    try:
        newDir = str(input("Please enter new destination\n"))
        os.chdir(newDir)
    except FileNotFoundError:
        print("Destination path cannot be found.")
        return 0
    except:
        print("Unknown error.")
        return 0

    return 1

def main():
    pass

if __name__ == "__main__":
    main()