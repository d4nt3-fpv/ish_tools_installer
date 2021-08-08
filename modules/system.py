import json
import itertools
import time
import subprocess
from modules.main_menu import *
from modules.category_menu import *

main_menu()

class system():

    def __init__(self):

        with open('modules/core/data.json') as file:
            self.data = json.load(file)

        with  open('modules/core/dep.json') as depfile:
            self.dep_data = json.load(depfile)

        with  open('modules/core/cat.json') as catfile:
            self.cat_data = json.load(catfile)


        # cat_list = []
        #
        # for cat_name in self.cat_data:
        #     cat_list.append(cat_name)


        # print(data["4nonimizer"]["name"])

        self.names = []
        self.urls = []
        self.dependencies = []
        # categories = [[]]

        self.categories = {}


        #### Lists for the categories ###

        self.information_gathering = []
        self.vulnerability_scanner = []
        self.exploitation_tools = []
        self.wireless_testing = []
        self.forensics_tools = []
        self.web_hacking = []
        self.stress_testing = []
        self.sniffing_spoofing = []
        self.password_attack = []
        self.maintaining_access = []
        self.ip_tracking = []
        self.programming_language = []
        self.ddos = []
        self.web_server = []
        self.termux_os = []
        self.other = []


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

            if str(self.data[name]["category"]) == "['information_gathering']":
                self.information_gathering.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['vulnerability_scanner']":
                self.vulnerability_scanner.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['exploitation_tools']":
                self.exploitation_tools.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['wireless_testing']":
                self.wireless_testing.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['forensics_tools']":
                self.forensics_tools.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['web_hacking']":
                self.web_hacking.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['stress_testing']":
                self.stress_testing.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['sniffing_spoofing']":
                self.sniffing_spoofing.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['password_attack']":
                self.password_attack.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['maintaining_access']":
                self.maintaining_access.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['ip_tracking']":
                self.ip_tracking.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['programming_language']":
                self.programming_language.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['ddos']":
                self.ddos.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['web_server']":
                self.web_server.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['termux_os']":
                self.termux_os.append(str(self.data[name]["name"]))
            else:
                self.other.append(str(self.data[name]["name"]))
                # print(self.data[name]["category"])



        # print(other)
        # print(self.categories)

        ### Make a one dimensional array out of the multi-dimensional dependency list.


        self.one_dimensional_dependencies = list(itertools.chain(*self.dependencies))

        self.dependencies_without_duplicates = list(dict.fromkeys(self.one_dimensional_dependencies))

        # print(self.one_dimensional_dependencies)
        # print(self.dependencies_without_duplicates)

            ####

        # print(names)
        # print(self.urls)
        # print(self.dependencies)
        # print(self.categories)

        # print(data)

        self.choosen_option = input("##> ")

        if int(self.choosen_option) == 1:
            self.install_all()

        elif int(self.choosen_option) == 2:
            self.clone_all_tools()

        elif int(self.choosen_option) == 3:
            self.install_by_category()

        elif int(self.choosen_option) == 4:
            self.install_one_tool()

        elif int(self.choosen_option) == 5:
            self.show_about()
        elif int(self.choosen_option) == 6:
            self.quit_program()



    def install_menu(self):
        self.linux_version = input("What distro do you use? (Type A= Alpine, U=ubuntu):  ")

        if self.linux_version.lower() == "a":
            self.lv = "alpine"
        elif self.linux_version.lower() == "u":
            self.lv = "ubuntu"

        return(self.linux_version)

    def show_banner(self, text):
        item = text
        inst_msg = " Installing: " + item + " "
        print(" " + "_" * len(inst_msg))
        print("|" + " " * len(inst_msg) + "|")
        print("|" + inst_msg + "|")
        print("|" + "_" * len(inst_msg) + "|")



    def install_all(self):
        print("Install all")
        self.install_menu()
        # Install the dependencies

        # Install the required dependencies
        try:

            if self.linux_version.lower() == "a":
                for com in self.dep_commands_apk:
                    try:
                        subprocess.call("clear")
                        self.show_banner(com)
                        subprocess.call(com)
                    except:
                        print("Could not run: " + com)
                self.v = "alpine"
            elif self.linux_version.lower() == "u":
                for com in self.dep_commands_apt:
                    try:
                        subprocess.call("clear")
                        self.show_banner(com)
                        subprocess.call(com)
                    except:
                        print("Could not run: " + com)
                self.v = "ubuntu"

        except:
            subprocess.call("cls")
            print("Could not install dependencies.")


        # Install the tools:
        for item in self.names:
            if self.v == "alpine":

                install_command = ("apk add " + item)
                print(install_command)
                try:
                    subprocess.call("clear")
                    self.show_banner(item)
                    subprocess.call(install_command)
                except:
                    print("Could not install " + item)

            elif self.v == "ubuntu":
                install_command = ("sudo apt-get install " + item + " -y")
                print(install_command)
                try:
                    subprocess.call("clear")
                    self.show_banner(item)
                    subprocess.call(install_command)
                except:
                    print("Could not install " + item)

        print('''
        
            ███████╗██╗███╗   ██╗██╗███████╗██╗  ██╗███████╗██████╗ 
            ██╔════╝██║████╗  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗
            █████╗  ██║██╔██╗ ██║██║███████╗███████║█████╗  ██║  ██║
            ██╔══╝  ██║██║╚██╗██║██║╚════██║██╔══██║██╔══╝  ██║  ██║
            ██║     ██║██║ ╚████║██║███████║██║  ██║███████╗██████╔╝
            ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝
               
        
        ''')




    def install_by_category(self):
        print("Install category")
        category_menu()

        choosen_category_option = int(input("##> "))

        if choosen_category_option == 1:
            cat_list_to_install = self.information_gathering
        elif choosen_category_option == 2:
            cat_list_to_install = self.vulnerability_scanner
        elif choosen_category_option == 3:
            cat_list_to_install = self.exploitation_tools
        elif choosen_category_option == 4:
            cat_list_to_install = self.wireless_testing
        elif choosen_category_option == 5:
            cat_list_to_install = self.forensics_tools
        elif choosen_category_option == 6:
            cat_list_to_install = self.web_hacking
        elif choosen_category_option == 7:
            cat_list_to_install = self.stress_testing
        elif choosen_category_option == 8:
            cat_list_to_install = self.sniffing_spoofing
        elif choosen_category_option == 9:
            cat_list_to_install = self.password_attack
        elif choosen_category_option == 10:
            cat_list_to_install = self.maintaining_access
        elif choosen_category_option == 11:
            cat_list_to_install = self.ip_tracking
        elif choosen_category_option == 12:
            cat_list_to_install = self.programming_language
        elif choosen_category_option == 13:
            cat_list_to_install = self.ddos
        elif choosen_category_option == 14:
            cat_list_to_install = self.web_server
        elif choosen_category_option == 15:
            cat_list_to_install = self.termux_os
        elif choosen_category_option == 16:
            cat_list_to_install = self.other
        else:
            print("Command not found.")
            self.quit_program()

        print(cat_list_to_install)

        self.install_menu()

        # Install the tools:
        for  cat_tool in cat_list_to_install:
            if self.lv == "alpine":

                install_command = ("apk add " + cat_tool)
                print(install_command)
                try:
                    subprocess.call("clear")
                    self.show_banner(cat_tool)
                    subprocess.call(install_command)
                except:
                    print("Could not install " + cat_tool)

            elif self.lv == "ubuntu":
                install_command = ("sudo apt-get install " + cat_tool + " -y")
                print(install_command)
                try:
                    subprocess.call("clear")
                    self.show_banner(cat_tool)
                    subprocess.call(install_command)
                except:
                    print("Could not install " + cat_tool)

        print("######## OK: Finished Successfully! ########")


    def install_one_tool(self):
        print("Install one tool")

        self.install_menu()

        i = 0
        for name in self.names:
            print(str(i) + ") " + name)
            i +=1

        choosen_tool_number = int(input("##> "))
        choosen_tool = self.names[choosen_tool_number]
        # choosen_tool_url = self.urls[choosen_tool_number]
        # print(choosen_tool_url)
        print(choosen_tool)


        if self.lv == "alpine":

            install_command = ("apk add " + choosen_tool)
            print(install_command)
            try:
                subprocess.call("clear")
                self.show_banner(choosen_tool)
                subprocess.call(install_command)
                print("######## OK: Finished Successfully! ########")
            except:
                print("Could not install " + choosen_tool)
                print("Do you want to clone it from github? (y/n))")
                clone_question = input("##> ")

                if clone_question.lower() == "y":
                    self.clone_one_tool(choosen_tool_number)
                else:
                    print("OK. Bye!")

        elif self.lv == "ubuntu":
            install_command = ("sudo apt-get install " + choosen_tool + " -y")
            print(install_command)
            try:
                subprocess.call("clear")
                self.show_banner(choosen_tool)
                subprocess.call(install_command)
                print("######## OK: Finished Successfully! ########")
            except:
                print("Could not install " + choosen_tool)
                print("Do you want to clone it from github? (y/n))")
                clone_question = input("##> ")

                if clone_question.lower() == "y":
                    self.clone_one_tool(choosen_tool_number)
                else:
                    print("OK. Bye!")

        # self.clone_one_tool(5)


    def clone_one_tool(self, number):
        choosen_tool_url = self.urls[number]
        print("--- Cloning " + choosen_tool_url + "---")

        try:
            clone_string = "git clone " + choosen_tool_url
            subprocess.call(clone_string)
            print("######## OK: Finished Successfully! ########")

        except:
            print("Could not clone " + choosen_tool_url)






    def show_about(self):
        print("This tool is created by Ben Wilcken")
        print("")
        print("It allows you to install the kali Linux hacking tools")
        print("into the ish app, so you can hack on the ipad.")
        print("I was inpired by the Tool-x and have used his json file.")
        print("So please check him out.")


    def clone_all_tools(self):
        if self.install_menu().lower() == "a":
            self.git_inst_command = "apk add git"
        else:
            self.git_inst_command = "sudo apt-get install git -y"

        try:
            subprocess.call(self.git_inst_command)
        except:
            print("Could not install git")

        for url in self.urls:
            try:
                subprocess.call("clear")
                self.show_banner(url)
                subprocess.call("git clone " + url)
            except:
                print("Could not clone: " + url)

    def quit_program(self):
        print("OK: Thanks for using this tool. Bye!")
        quit()


system()
