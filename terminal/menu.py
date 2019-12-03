#Python libraries
import os



class Menu:

    def __init__(self, options):
        """options (list) : list of different options we can select in the menu
        size (int) : number of options in the menu"""

        self.options = options
        self.size = len(options)



    def display_menu(self):
        """Display the menu on the terminal, and user must chose an option by entering the number corresponding to an option.
        
        Return the option_selected as a string (str)"""
        wrong_input = True

        while wrong_input:
            for i, option in enumerate(self.options):
                print(str(i+1)+" : "+option)
            
            option_selected = input("Choisissez une option : ")
            if 1 <= int(option_selected) <= self.size:
                wrong_input = False
            else:
                os.system("cls")

        return option_selected
        