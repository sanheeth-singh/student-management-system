from src.student_manager import StudentManager
from src.utils import StudentNotFoundError, DuplicateStudentError, validate_gpa

def print_menu():
    print("\n--- Student Record Management ---")
    print("1. Add Student (Create)")
    print("2. View Student (Read)")
    print("3. Update Student (Update)")
    print("4. Delete Student (Delete)")
    print("5. List All / Top Achievers (List Comprehension & Lambda)")
    print("6. Export to CSV")
    print("7. Exit")

def main():
    manager = StudentManager()

    while True:
        print_menu()
        choice = input("Enter choice (1-7): ").strip()

        try:
            if choice == "1":
                sid = input("Enter Student ID: ").strip()
                name = input("Enter Name: ").strip()
                course = input("Enter Course/Major: ").strip()
                gpa = validate_gpa(input("Enter GPA (0.0 - 10.0): "))
                manager.add_student(sid, name, course, gpa)
                print(f"Student {sid} added successfully.")

            elif choice == "2":
                sid = input("Enter Student ID: ").strip()
                student = manager.get_student(sid)
                print(f"Record: ID={student['student_id']}, Name={student['name']}, Course={student['course']}, GPA={student['gpa']}")

            elif choice == "3":
                sid = input("Enter Student ID to update: ").strip()
                manager.get_student(sid)  # verify existence
                name = input("New Name (leave blank to skip): ").strip() or None
                course = input("New Course (leave blank to skip): ").strip() or None
                raw_gpa = input("New GPA (leave blank to skip): ").strip()
                gpa = validate_gpa(raw_gpa) if raw_gpa else None
                manager.update_student(sid, name, course, gpa)
                print(f"Student {sid} updated successfully.")

            elif choice == "4":
                sid = input("Enter Student ID to delete: ").strip()
                manager.delete_student(sid)
                print(f"Student {sid} removed.")

            elif choice == "5":
                print("\n1. All Students (Sorted by GPA desc)")
                print("2. Honor Roll (GPA >= 8.5)")
                sub = input("Select[1/2]: ").strip()
                if sub == "1":
                    results = manager.get_sorted_by_gpa()
                else:
                    results = manager.filter_honor_roll()
                
                for r in results:
                    print(f"• [{r['student_id']}] {r['name']} - {r['course']} (GPA: {r['gpa']})")

            elif choice == "6":
                manager.export_to_csv()
                print("Data exported to data/students.csv successfully.")

            elif choice == "7":
                print("Exiting application.")
                break
            else:
                print("Invalid option. Please choose between 1 and 7.")

        except (StudentNotFoundError, DuplicateStudentError, ValueError) as err:
            print(f"[Error] {err}")
        except Exception as e:
            print(f"[Unexpected Exception] {e}")

if __name__ == "__main__":
    main()