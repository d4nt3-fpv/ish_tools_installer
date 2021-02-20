import json
from main_menu import *

main_menu()



with open('core/data.json') as file:
    data = json.load(file)


# print(data["4nonimizer"]["name"])

names = []
urls = []
dependencies = []
categories = [[]]


for name in data:
    names.append(name)
    urls.append(data[name]["url"])
    dependencies.append(data[name]["dependency"])
    categories.append([str(data[name]["name"]) , str(data[name]["category"])])


print(names)
print(urls)
print(dependencies)
print(categories)

# print(data)