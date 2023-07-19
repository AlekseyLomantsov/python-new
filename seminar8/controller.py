import input_user
import functions


user_choice = input_user.menu()

if user_choice == "1":
    functions.add_info()
elif user_choice == "2":
    functions.find_num()
elif user_choice == "3":
    functions.delete_item()
elif user_choice == "4":
    functions.show_all()