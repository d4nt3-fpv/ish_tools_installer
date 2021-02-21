class main_menu():
    global choosen_option
    def __init__(self):



        print('''
  _____  _____ _    _            _ _______ ____   ____  _       _____ 
 |_   _|/ ____| |  | |          | |__   __/ __ \ / __ \| |     / ____|
   | | | (___ | |__| | __ _  ___| | _| | | |  | | |  | | |    | (___  
   | |  \___ \|  __  |/ _` |/ __| |/ / | | |  | | |  | | |     \___ \ 
  _| |_ ____) | |  | | (_| | (__|   <| | | |__| | |__| | |____ ____) |
 |_____|_____/|_|  |_|\__,_|\___|_|\_\_|  \____/ \____/|______|_____/                                                                                                                                                                                                                                          
''')

        self.choose_options()

    def choose_options(self):

        print("Please select an option: ")
        print("1) Install all tools")
        print("2) Clone all tools from github")
        print("3) Install tools by category")
        print("4) Choose a tool to install")
        print("5) About this project")
        print("6) Exit the program")





