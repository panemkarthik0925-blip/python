def add_student():
    try:
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        age = input("Enter Age: ")

        with open("students.txt", "a") as file:
            file.write(f"{sid}, {name}, {course}, {age}\n")
        print("Student added successfully!")
    except Exception as e:
        print("Error:", e)


def view_students():
    try:
        with open("students.txt", "r") as file:
            print("\n--- Student Records ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No records found.")


def search_student():
    sid = input("Enter ID to search: ")
    found = False
    with open("students.txt", "r") as file:
        for line in file:
            if line.startswith(sid):
                print("Student Found:", line.strip())
                found = True
                break
    if not found:
        print("Student not found.")


def update_student():
    sid = input("Enter ID to update: ")
    lines = []
    updated = False

    with open("students.txt", "r") as file:
        lines = file.readlines()

    with open("students.txt", "w") as file:
        for line in lines:
            if line.startswith(sid):
                name = input("Enter new name: ")
                course = input("Enter new course: ")
                age = input("Enter new age: ")
                file.write(f"{sid}, {name}, {course}, {age}\n")
                updated = True
            else:
                file.write(line)

    print("Student updated!" if updated else "Student not found.")


def delete_student():
    sid = input("Enter ID to delete: ")
    lines = []

    with open("students.txt", "r") as file:
        lines = file.readlines()

    with open("students.txt", "w") as file:
        for line in lines:
            if not line.startswith(sid):
                file.write(line)

    print("Student deleted if ID existed.")


def main():
    while True:
        print("\n1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")


main()
