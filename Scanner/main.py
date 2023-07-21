import os
import sys
import duplicates
import diskutil
import largefiles

def display_menu():
    print("Disk Space Manager:")
    print("1. Check Duplicate Files")
    print("2. Check Large Files")
    print("3. Check Disk Usage")
    print("0. Exit")

# Function to handle user's choice and call the corresponding function
def main():
    display_menu()
    while True:
        choice = input("Enter your choice (0-3): ")
        if choice == '1':
            duplicates.main()    
        elif choice == '2':
            largefiles.find_files()
        elif choice == '3':
            diskutil.show_disk_util()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
