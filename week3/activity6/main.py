from database import create_tables
from school_manager import *

def menu():
    print("\n=== Menu ===")
    print(" 1) Add student")
    print(" 2) View students")
    print(" 3) Add program")
    print(" 4) View programs")
    print(" 5) Add teacher")
    print(" 6) View teachers")
    print(" 7) Add student <-> teacher (M:N)")
    print(" 8) View student-teacher links")
    print(" 9) Add teacher <-> program (M:N)")
    print("10) View teacher-program links")
    print("11) Update a student")
    print("12) Delete a student")
    print("13) Update a teacher")
    print("14) Delete a teacher")
    print("15) Update a program")
    print("16) Delete a program")
    print("17) Exit")

def main():
    create_tables()
    while True:
        menu()
        choice = input("Select an option (1-17): ").strip()

        if choice == '1':
            student_id = input("Enter student_id: ").strip()
            name = input("Enter name: ").strip()
            gender = input("Enter gender: ").strip()
            nationality = input("Enter nationality: ").strip()
            email = input("Enter email: ").strip()
            program_id = input("Enter program_id (or blank): ").strip()
            birth_date = input("Enter birth_date (YYYY-MM-DD, or blank): ").strip()
            add_stu(student_id, name, gender, nationality, email, program_id, birth_date)

        elif choice == '2':
            rows = view_stu()
            if not rows:
                print("[INFO] No students.")
            else:
                for r in rows:
                    print(r)

        elif choice == '3':
            name = input("Enter program name: ").strip()
            code = input("Enter program code: ").strip()
            add_program(name, code)

        elif choice == '4':
            rows = view_programs()
            if not rows:
                print("[INFO] No programs.")
            else:
                for r in rows:
                    print(r)

        elif choice == '5':
            name = input("Enter teacher name: ").strip()
            email = input("Enter teacher email: ").strip()
            add_teacher(name, email)

        elif choice == '6':
            rows = view_teachers()
            if not rows:
                print("[INFO] No teachers.")
            else:
                for r in rows:
                    print(r)

        elif choice == '7':
            student_id = input("Enter student PK id: ").strip()
            teacher_id = input("Enter teacher PK id: ").strip()
            add_student_teacher(student_id, teacher_id)

        elif choice == '8':
            rows = view_student_teacher()
            if not rows:
                print("[INFO] No student-teacher links.")
            else:
                for r in rows:
                    print(r)

        elif choice == '9':
            teacher_id = input("Enter teacher PK id: ").strip()
            program_id = input("Enter program PK id: ").strip()
            role = input("Enter role (optional): ").strip() or None
            add_teacher_program(teacher_id, program_id, role)

        elif choice == '10':
            rows = view_teacher_program()
            if not rows:
                print("[INFO] No teacher-program links.")
            else:
                for r in rows:
                    print(r)

        elif choice == '11':
            pk = to_int_or_none(input("Enter student PK id to update: ").strip())
            if not pk:
                print("[ERR] Invalid PK.")
                continue
            fields = {}
            print("Leave blank to keep current value.")
            v = input("New student_id: ").strip()
            if v: fields["student_id"] = v
            v = input("New name: ").strip()
            if v: fields["name"] = v
            v = input("New gender: ").strip()
            if v: fields["gender"] = v
            v = input("New nationality: ").strip()
            if v: fields["nationality"] = v
            v = input("New email: ").strip()
            if v: fields["email"] = v
            v = input("New program_id: ").strip()
            if v: fields["program_id"] = v
            v = input("New birth_date (YYYY-MM-DD): ").strip()
            if v: fields["birth_date"] = v
            v = input("New del_time: ").strip()
            if v: fields["del_time"] = v
            update_stu(pk, **fields)

        elif choice == '12':
            pk = to_int_or_none(input("Enter student PK id to delete: ").strip())
            if not pk:
                print("[ERR] Invalid PK.")
                continue
            delete_stu(pk)

        elif choice == '13':
            pk = to_int_or_none(input("Enter teacher PK id to update: ").strip())
            if not pk:
                print("[ERR] Invalid PK.")
                continue
            fields = {}
            print("Leave blank to keep current value.")
            v = input("New name: ").strip()
            if v: fields["name"] = v
            v = input("New email: ").strip()
            if v: fields["email"] = v
            v = input("New del_time: ").strip()
            if v: fields["del_time"] = v
            update_teacher(pk, **fields)

        elif choice == '14':
            pk = to_int_or_none(input("Enter teacher PK id to delete: ").strip())
            if not pk:
                print("[ERR] Invalid PK.")
                continue
            delete_teacher(pk)

        elif choice == '15':
            pk = to_int_or_none(input("Enter program PK id to update: ").strip())
            if not pk:
                print("[ERR] Invalid PK.")
                continue
            fields = {}
            print("Leave blank to keep current value.")
            v = input("New name: ").strip()
            if v: fields["name"] = v
            v = input("New code: ").strip()
            if v: fields["code"] = v
            v = input("New del_time: ").strip()
            if v: fields["del_time"] = v
            update_program(pk, **fields)

        elif choice == '16':
            pk = to_int_or_none(input("Enter program PK id to delete: ").strip())
            if not pk:
                print("[ERR] Invalid PK.")
                continue
            delete_program(pk)

        elif choice == '17':
            print("Bye.")
            break

        else:
            print("[ERR] Invalid option.")

if __name__ == '__main__':
    main()