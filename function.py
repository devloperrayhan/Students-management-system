# Our searvice menu.. show_menu() is used for show our menu.
def show_menu():
    print("=========== MENU ===========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    return "5. Exit"

# add_student(), it's work for add students.

def add_student():
    Add_name = open("students.txt","a") # Opne .txt file as append()
    rolls = set()
    while True:
        students_name = input("Enter studennts ame : ") # Imput student Name.
        if students_name.isdigit() or not students_name:
            print("ERROR: Student name must be a string")
            continue
        else:
            break
    while True:
        students_roll = input("Enter students roll : ").strip()
        with open('students.txt', 'r') as students_roll_open: # open file as a read mode.
            for line in students_roll_open: # Work for check Duplicate Roll number.
                if 'Roll' in line and ':' in line:
                    roll = line.split(':', 1)[1].strip()
                    if roll:
                        rolls.add(roll)
        if students_roll in rolls: 
            print("ERROR: Roll number already exists for another student.")
            while True:
                students_roll = input("Enter students roll : ").strip()
                students_roll = students_roll

                if students_roll not in rolls:                    
                    # students_roll = int(students_roll)
                    break
                else:
                    print("ERROR: Roll number already exists for another student.")

        if students_roll == "0": # 0 Roll Condition. you can't input 0 for roll number.
            print("Zero is not allow for roll.")
        elif students_roll.isdigit():
            students_roll = int(students_roll)
            break
        else:
            print("ERROR : Use number to select option. Word and any symbols is not allowed.")
    students_dept = input("Enter students deparment : ")
    students_semestar = input("Enter students semestar : ")
    students_email = input("Enter students e-mail : ")
    # Add Student's all details
    add_name = Add_name.write(f"\nName      : {students_name}\nRoll      : {students_roll}\nDepatment : {students_dept}\nSemestar  : {students_semestar}\nE-mail    : {students_email}\n =============END============= \n")
    # Add_name.flush()
    Add_name.close() # Close file.
    return "\n*****Student record added successfully!*****\n"

# show students list... show_student() work for showing students list.

def show_student():
    opne_file_as_a_read = open("students.txt","r")
    read_students = opne_file_as_a_read.read()
    print(read_students)
    opne_file_as_a_read.close()
    return "All Students are here.\n"

# Search student... it's work for searching students. it can search student.

def search_student():
    def search_and_show_student(file_name, search_roll): # Students.txt File and input roll number Parameter.
        found = False
        printing = False
        try:
            with open(file_name, 'r') as file: # Open students file as a read mode, here is students.txt == file_name
                for line in file:
                    strippede = line.strip()
                    if "Name" in strippede and ':' in strippede:
                        roll_value = strippede.split(':', 1)[1].strip()
                        if roll_value == search_roll:
                            found = True
                            printing = True
                            print("Student Found:\n") # Roll found msg.
                    if printing:
                        print(line.rstrip())
                    if printing and 'END' in strippede: # if found 'END' in students.txt file, it will be break.
                        printing = False
                        # break
            if not found:
                print(f"\n-- Did not find '{search_roll}' in students list. (or Check your search name spelling)") # Roll not found msg.
        except FileNotFoundError:
            print(f"ERROR: The file '{file_name}' was not found.") # File not found msg.
        except Exception as e:
            print(f"An error occurred: {e}")
        file.close() # Here is file closed.
    while True:
        search_students = input("\nEnter student name to search (or 'exit' to quit): ").strip() # Input Roll numner.
        if search_students.lower() in ['exit', 'e', 'quit', 'q']: # Exit Condition for exit to while loop.
            print("Thank You, Search option is exit")
            break
        if not search_students: # Input is not, condition.
            print("Must required Name.")
            continue
        search_and_show_student("students.txt", search_students) # import students.txt file.
    return "Now You Have Menu Option."

# Remove student. remove_student() can remove student.

def remove_student():
    file_name = "students.txt" # file name.
    while True:
        search_roll = input("Enter student roll to remove (or 'exit' to quit): ").strip()
        if search_roll.lower() in ['exit', 'e', 'quit', 'q']: # Break while system.
            print("Remove option exited.")
            break
        if not search_roll:
            print("Roll number is required.")
            continue
        students = []
        found = False
        try:
            with open(file_name, 'r') as file: # Open students.txt as a read() mode.
                current_student = []
                for line in file:
                    if "Name" in line and ':' in line: # If line has Name and :
                        current_student = [line]
                    elif current_student:
                        current_student.append(line)
                        if 'END' in line and '=' in line:
                            if 'Roll' in ''.join(current_student):
                                roll_value = None
                                for l in current_student:
                                    if 'Roll' in l and ':' in l:
                                        roll_value = l.split(':', 1)[1].strip()
                                        break
                                if roll_value == search_roll: # If roll_value Equals search_roll.
                                    found = True
                                else:
                                    students.extend(current_student)
                            else:
                                students.extend(current_student)
            if found: # If Roll number found.
                sure = input(f"Are You sure to delete roll number '{search_roll}' student? Y/N : ")
                if sure.lower() in ['Y', 'y', 'Yeah', 'yess']:
                    with open(file_name, 'w') as file: # Open file as a Write() Mode.
                        file.writelines(students)
                    print(f"*****Student with roll '{search_roll}' removed successfully!*****\n") # Remove msg.
            else:
                print(f"Student with roll '{search_roll}' not found.\n")
        except FileNotFoundError: # If students.txt file can't found.
            print(f"ERROR: The file '{file_name}' was not found.")
    file.close()
    return "Now You Have Menu Option."

def dev():
    print("Made By Developer Rayhan from Ostad's Learner, Bacth-9 at Full Stack Web Development with Python, Django, React & AI. ")
    print("Exam-Week-1, Create a Student Record Management System!")
    print("developerrayhan@iCould.com")
    print("Copyright 01/30/2026")