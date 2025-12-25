import csv
import os

student = []
def load_student():
    with open("student.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student.append(row)
            
        return student

def add_student():
    new_student = {}

    new_student["id"] = input("Enter Student ID: ")
    new_student["name"] = input("Enter Name: ")
    new_student["department"] = input("Enter Department: ")
    new_student["semester"] = input("Enter Semester: ")
    new_student["cgpa"] = input("Enter CGPA: ")

    student.append(new_student)

    with open("student.csv", mode="w", newline="") as file:
        fieldnames = ["id", "name", "department", "semester", "cgpa"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(student)

    print("student added successfully.")
def search_student():
    search_id = input("Enter id =")
    
    for s in student:
        if s ["id"] == search_id:
            print("student found :")
            print(f"ID: {s['id']} | Name: {s['name']} | Dept: {s['department']} | Semester: {s['semester']} | CGPA: {s['cgpa']}")
            return
        else:
            print("not found :")
            
def update_student():
    update_id = input("Enter id to update :")
    
    for s in student:
        if s["id"]== update_id:
         print("Enter the id you want to update :")
        
        name = input("Enter the new name: ")
        dep = input ("ENter the new department name: ")
        sem = input('Enter the new semester')
        cgpa = input("Enter the new CGPA")
        
        
        if name:
            s['name'] = name
        if dep:
            s['department'] = dep
        if sem:
            s['semester']= sem
        if cgpa :
            s['cgpa']=cgpa
            
        with open("student.csv", mode="w", newline="") as file:
                fieldnames = ["id", "name", "department", "semester", "cgpa"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(student)

                print("student record updated successfully.")
                return 

    print("student not found.")
         
def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    for s in student:
        if s["id"] == delete_id:
            student.remove(s)

            with open("student.csv", mode="w", newline="") as file:
                fieldnames = ["id", "name", "department", "semester", "cgpa"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(student)

            print("student deleted successfully.")
            return

    print("student not found.")
    
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. View All Students")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("Add student option selected")
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        for s in student:
            print(f"{s['id']} | {s['name']} | {s['department']} | {s['semester']} | {s['cgpa']}")

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")