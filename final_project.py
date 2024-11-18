import sys
task_list = []
def main() :
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("0. Exit the application")

        try:
            choice = int(input("Enter your choice: "))
        # except ValueError:
        #     print("You need to choose from the numbers in menu!")
            if choice >= 4 :
                raise ValueError("The choice does not exist. Choose an option from the menu!")
            else :
                if choice == 1:
                    
                        add_task = input("Add the needed task: ")
                        task_list.append(add_task)
                        print(f'Task Added')
                
                    # Do something for option 1
                elif choice == 2:
                    try:
                        if not task_list:
                            raise IndexError("Error")
                        else:
                            print(task_list)
                    except IndexError:
                        print("there are no tasks associated with your list")
                    # Do something for option 2
                elif choice == 3:
                    try:
                        if not task_list:
                            raise IndexError("Error")
                        else: 
                            for index, element in enumerate(task_list):
                                print(f"{index}: {element}")
                            delete = int(input(f'which item would you like to delete?'))
                            if 0 <= delete < len(task_list):
                                deleted_item = task_list.pop(delete)
                                print(f"Deleted item: {deleted_item}")
                            else:
                                print("Invalid index. Please choose a valid index.")    


                    except IndexError:
                        print("The list is empty. Try adding something first.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                elif choice == 0:
                    print("Exiting...")
                    sys.exit()
                else:
                    print("Invalid choice. Please try again.")
        
        except ValueError as e:
            # Handle the error
            print(f"Error: {e}")

if __name__ == "__main__":
    main()