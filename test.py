# Create user defined functions

#Defined a non value returning function
def my_animal(name, sound, pounds_food):
    print(f"The {name} makes a {sound} noise!")
    print(f"The {name} eats {pounds_food} pounds of food a day")
    print(f"The {name} eats {pounds_food * 7} pounds of food a week")
def getName():
    name = input("Enter your name!: ")
    return name + "********"
def displayName(first):
    lastName = input("Enter your last name!: ")
    fullName = first + " " + lastName
    return fullName
#Create a main function logic goes here
def main():
    print("The main function is executing!")
    print()
    #Call the my animal function
    my_animal("Lion","rawr", 20.5)
#call the main function
myName = getName()
print(myName)
print()
print(displayName(myName))
# Call the main function
if __name__ == "__main__":
    main()



