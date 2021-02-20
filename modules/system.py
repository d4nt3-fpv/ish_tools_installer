import json
import itertools
import time
import subprocess
from main_menu import *


main_menu()

class system():

    def __init__(self):

        with open('core/data.json') as file:
            self.data = json.load(file)

        with  open('core/dep.json') as depfile:
            self.dep_data = json.load(depfile)


        # print(data["4nonimizer"]["name"])

        self.names = []
        self.urls = []
        self.dependencies = []
        # categories = [[]]

        self.categories = {}


        # Put all commands in a list:

        self.dep_commands_apt = []
        self.dep_commands_apk = []


        for dep in self.dep_data:
            self.dep_commands_apt.append(self.dep_data[dep]["command_apt"])
            self.dep_commands_apk.append(self.dep_data[dep]["command_apk"])


        for name in self.data:
            self.names.append(name)
            self.urls.append(self.data[name]["url"])
            self.dependencies.append(self.data[name]["dependency"])
            # categories.append([str(data[name]["name"]) , str(data[name]["category"])])
            self.categories[self.data[name]["name"]] = self.data[name]["category"]



        ### Make a one dimensional array out of the multi-dimensional dependency list.


        self.one_dimensional_dependencies = list(itertools.chain(*self.dependencies))

        self.dependencies_without_duplicates = list(dict.fromkeys(self.one_dimensional_dependencies))

        print(self.one_dimensional_dependencies)
        print(self.dependencies_without_duplicates)

            ####

        # print(names)
        # print(urls)
        # print(self.dependencies)
        # print(categories)

        # print(data)

        self.choosen_option = input("##> ")

        if int(self.choosen_option) == 1:
            self.install_all()

        elif int(self.choosen_option) == 2:
            self.install_by_category()

        elif int(self.choosen_option) == 3:
            self.install_one_tool()

        elif int(self.choosen_option) == 4:
            self.show_about()

        elif int(self.choosen_option) == 5:
            self.quit_program()

    def install_menu(self):
        self.linux_version = input("What distro do you use? (Type A= Alpine, U=ubuntu):  ")
        return(self.linux_version)


    def install_all(self):
        print("Install all")
        self.install_menu()
        # Install the dependencies

        # Install the required dependencies
        try:

            if self.linux_version.lower() == "a":
                for com in self.dep_commands_apk:
                    subprocess.call(com)
                v = "alpine"
            elif self.linux_version.lower() == "u":
                for com in self.dep_commands_apt:
                    subprocess.call(com)
                v = "ubuntu"

        except:
            subprocess.call("cls")
            print("Could not install dependencies.")


        # Install the tools:
        for item in self.names:
            if v == "alpine":
                install_command = ("apk add " + item)
                print(install_command)
                subprocess.call(install_command)
            elif v == "ubuntu":
                install_command = ("sudo apt-get install " + item)
                print(install_command)
                subprocess.call(install_command)



        # for self.dependency in self.dependencies:
        #     print(self.dependency)



    def install_by_category(self):
        print("Install category")

    def install_one_tool(self):
        print("Install one tool")

    def show_about(self):
        print("Show about")

    def quit_program(self):
        print("Bye")


system()