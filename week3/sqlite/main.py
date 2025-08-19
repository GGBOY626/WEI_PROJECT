from database import create_table
from user_manager import add_user, view_users, search_user, delete_user,add_stu,view_stu,search_stu,delete_stu

def menu():
    print("\n==== User Student Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Add Student")
    print("6. View All Students")
    print("7. Search Students by Name")
    print("8. Delete Students by ID")
    print("9. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-9): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            name = input("Enter stu_name: ")
            address = input("Enter stu_address: ")
            add_stu(name, address)
        elif choice == '6':
            students = view_stu()
            for student in students:
                print(student)
        elif choice == '7':
            name = input("Enter stu_name to search: ")
            students = search_stu(name)
            for student in students:
                print(student)
        elif choice == '8':
            stu_id = int(input("Enter Student ID to delete: "))
            delete_stu(stu_id)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
