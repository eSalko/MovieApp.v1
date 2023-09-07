from model import MenuFunctions


class MakeMenu:
    """MakeMenu class containing the formatting and printing of the menu to
        display to the user on application start"""
    def printMenu(self):
        """function to print menu"""
        menuFunction = MenuFunctions()
        # creating MenuFunctions object to access available functions
        menuFunction.make_menu()
        # calling menu function to show the user a menu
        option = input("What would you like to do? ")
        # getting input from user to select a menu option
        match option:
            case "1":
                menuFunction.add_movie()
            case "2":
                menuFunction.edit_movie()
            case "3":
                menuFunction.print_movies()
            case "4":
                menuFunction.delete_movie()
            case "5":
                exit()
