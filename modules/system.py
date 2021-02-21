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

        with  open('core/cat.json') as catfile:
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

        information_gathering = []
        vulnerability_scanner = []
        exploitation_tools = []
        wireless_testing = []
        forensics_tools = []
        web_hacking = []
        stress_testing = []
        sniffing_spoofing = []
        password_attack = []
        maintaining_access = []
        ip_tracking = []
        programming_language = []
        ddos = []
        web_server = []
        termux_os = []
        other = []


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
                information_gathering.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['vulnerability_scanner']":
                vulnerability_scanner.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['exploitation_tools']":
                exploitation_tools.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['wireless_testing']":
                wireless_testing.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['forensics_tools']":
                forensics_tools.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['web_hacking']":
                web_hacking.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['stress_testing']":
                stress_testing.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['sniffing_spoofing']":
                sniffing_spoofing.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['password_attack']":
                password_attack.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['maintaining_access']":
                maintaining_access.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['ip_tracking']":
                ip_tracking.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['programming_language']":
                programming_language.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['ddos']":
                ddos.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['web_server']":
                web_server.append(str(self.data[name]["name"]))
            elif str(self.data[name]["category"]) == "['termux_os']":
                termux_os.append(str(self.data[name]["name"]))
            else:
                other.append(str(self.data[name]["name"]))
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
                v = "alpine"
            elif self.linux_version.lower() == "u":
                for com in self.dep_commands_apt:
                    try:
                        subprocess.call("clear")
                        self.show_banner(com)
                        subprocess.call(com)
                    except:
                        print("Could not run: " + com)
                v = "ubuntu"

        except:
            subprocess.call("cls")
            print("Could not install dependencies.")


        # Install the tools:
        for item in self.names:
            if v == "alpine":

                install_command = ("apk add " + item)
                print(install_command)
                try:
                    subprocess.call("clear")
                    self.show_banner(item)
                    subprocess.call(install_command)
                except:
                    print("Could not install " + item)

            elif v == "ubuntu":
                install_command = ("sudo apt-get install " + item)
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

    def install_one_tool(self):
        print("Install one tool")

    def show_about(self):
        print("This tool is created by Ben Wilcken")
        print("")
        print("It allows you to install the kali Linux hacking tools")
        print("into the ish app, so you can hack on the ipad.")
        print("I was inpired by the Tool-x and have used their json file.")
        print("So please check them out.")


    def clone_all_tools(self):
        if self.install_menu().lower() == "a":
            self.git_inst_command = "apk add git"
        else:
            self.git_inst_command = "sudo apt-get install git"

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