#definire
#get exrem informatii dintr un server
#post cand vrem sa cream date noi
#put cand vrem sa updatam date deja existente
#delete cand vrem sa stergem niste date
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get(self):
        data = {

            "name": self.__name,
            "age": self.__age
        }
        return data

    def put_name(self, name):
        self.__name = name

    def put_age (self, age):
        self.__age = age

    def put(self, name, age):
        self.__name = name
        self.__age = age

    def delete (self):
        self.__name = None
        self.__age = None

a = Animal("Ruf", 10)

#afisare
print(f"Name = {a.get_name()}")
print(f"Name = {a.get_age()}")
print(f"Name + Age = {a.get()}")

a.put("rufff", 5)
print(f"Name + Age = {a.get()}")

#request, a scoate informii din cele necesare
from flask import Flask #din flask importam obiectul Flask


app = Flask(__name__) #cream instanta acestei resurse

@app.route("/") #redirectionare
def hello_world():
    return "<h1> Hello World!</h1>" #se poate trimite orice cat timp e string sau dictionar

@app.route("/animal-info")  #se iau date de la animal /animal-info route
def anima_info():
    a = Animal("Ruf", 10)
    response = a.get()
    return response

if __name__ == "__main__": #delimiteaza scriptul in doua moduri, ce e sub if nu se ruleaza decat daca rulez acest script
    app.run(debug=True, host='localhost', port=3002)