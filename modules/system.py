import json
import os
import itertools

from main_menu import *

main_menu()


class system():

    def __init__(self):

        with open('core/data.json') as file:
            self.data = json.load(file)


        # print(data["4nonimizer"]["name"])

        self.names = []
        self.urls = []
        self.dependencies = []
        # categories = [[]]

        self.categories = {}


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
        self.install_location = input("Where do you want to install?: ")
        return(self.install_location)


    def install_all(self):
        print("Install all")
        # print(self.install_menu())
        # os.system("cd " + self.install_menu())




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