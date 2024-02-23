def person():
    name = input("Enter your name : ")
    age = int(input("Enter you age ? "))
    location =input("Enter you Location ")

    return name, age , location

name, age, location = person()

print("Hello, My name", name ,"I am ", age, "years old located in", location )