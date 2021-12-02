# Nathan Le
# Assignment 10.1: Your Own Class
# Implement your own class based on a real-world object. 
# You will write a class to meet certain requirements (detailed below) and write a short demo program in the main function that highlights all your class variables and methods. 
# Along with this code, you will also create a short README file (this can be a .txt, .md, or .pdf) that describes your class, each of the variables and methods within, and describes the demo program and how to use it.
import random

# Creates a class called GamingConsole
class GamingConsole:
    def __init__(self, brand="", model="", age=0):
        # Set variables based on constructor arguments
        self.__brand = brand
        self.__model = model
        # Raises a ValueError if age < 0
        if age < 0:
            print("Age cannot be less than zero.")
            raise ValueError
        else:
            self.__age = age
    # Sets the brand
    def set_brand(self, brand):
        self.__brand = brand
    # Returns the brand
    def get_brand(self):
        return self.__brand
    # Sets the model
    def set_model(self, model):
        self.__model = model
    # Returns the model
    def get_model(self):
        return self.__model
    # Sets the age
    def set_age(self, age):
        # Raises a ValueError if age < 0
        if age < 0:
            print("Age cannot be less than zero.")
            raise ValueError
        else:
            self.__age = age
    # Returns the age
    def get_age(self):
        return self.__age
    def will_it_start(self):
        # If age is greater than 10, than the console will have a higher chance of not starting up
        if self.__age > 10:
            x = random.randint(0,2)
            if x == 0:
                return ("Your console is up and running! :D")
            else:
                return ("Your console has failed to start! :(")
        # If age is less than 10, than the console will have a higher chance of starting up
        else:
            x = random.randint(0,7)
            if x == 0:
                return ("Your console has failed to start! :(")
            else:
                return ("Your console is up and running! :D")
    def getting_older(self):
        # Increments the age of the console by 1
        self.__age += 1
    # Magic method
    def __str__(self):
        return(f"Gaming Console: Brand - {self.__brand}, Model - {self.__model}, Age - {self.__age}.")

def main():
    # Creates a PS5 with GamingConsole class
    ps5 = GamingConsole("Play Station", "PS5", 4)
    # Prints the PS5 out
    print(ps5)
    # Sets the age in a variable
    x = ps5.get_age()
    # Asks the user to input a number
    user = int(input("Enter a number: "))
    # Enters a while loop that prints the age, shows whether it will start, and increments the age by one
    while ps5.get_age() <= user + x:
        print(ps5.get_age())
        print(ps5.will_it_start())
        ps5.getting_older()
    print(ps5)
    # Creates a default console
    console = GamingConsole()
    # Sets the brand, model, and age of the console
    console.set_brand("Nintendo")
    console.set_model("Switch OLED")
    console.set_age(0)
    # Prints the console out
    print(console)
    y = console.get_age()
    # Asks the user to input a number
    user2 = int(input("Enter a number: "))
    # Enters a while loop that prints the age, shows whether it will start, and increments the age by one
    while console.get_age() <= user2 + y:
        print(console.get_age())
        print(console.will_it_start())
        console.getting_older()
    print(console)

if __name__ == "__main__":
    main()