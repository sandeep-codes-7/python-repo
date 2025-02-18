from options import *

def main():
    while True:
        print("\n\n----TO-DO List----\n")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Mark as done")
        print("5. Delete task")
        print("6. Delete done tasks")
        print("7. Delete all tasks")
        print("8. Exit")
        choice = int(input("choose options: "))
        print("\n")
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            update_task()
        elif choice == 4:
            mark_as_done()
        elif choice == 5:
            delete_task()
        elif choice == 6:
            delete_done_task()
        elif choice == 7:
            delete_all()
        elif choice == 8:
            cursor.close()
            conn.close()
            exit()
        else:
            print("Enter valid option!")

if __name__ == "__main__":
    main()