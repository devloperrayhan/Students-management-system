#  I imported the menu from another of my custom files. (File name is function.py)
from function import show_menu, search_student, add_student, show_student, remove_student

# Check students.txt file
file_name = "students.txt"
try:
    with open(file_name, 'x',) as f:
        pass
except FileExistsError:
    pass
except Exception as e:
   print(f"somthing is wrong: {e}")

# Main Title.

print("\nWelcome to the Student Record Management System!\nLoading student records from students.txt... Done!") # Open msg.

while True:
    print(show_menu()) # Menu Function Calling. 
    select_option = input("Select Option (1 TO 5): ")
    if select_option.isdigit():
        select_option = int(select_option)
    else:
        print("ERROR : Use number to select option. Word and any symbols is not allowed.") # Err msg, if use enter the input as a str.

    if select_option == 5:
        print("*****Thank you for using the Student Record Management System. Have a gread day!*****") # open msg.
        break # select_option Equals 5 for break while.
    elif select_option == 1:
        print(add_student()) # Add Student Function calling,
    elif select_option == 2:
        print(show_student()) # show student function calling.
    elif select_option == 3:
        print(search_student()) # Search StuDent function calling.
    elif select_option == 4:
        print(remove_student()) # Remove student function is calling.