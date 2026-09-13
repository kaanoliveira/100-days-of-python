len(12345) >> TypeError: object of type 'int' has no len()
len("12345") 


print(type("Hello")) # <class 'str'>
print(type(12345)) # class 'int'>
print(type(3.14159)) # <class 'float'>
print(type(True)) # <class 'bool'>

#Type conversion
print("123" + "345") # 123345
print(int("123") + int("345")) # 468
print(int("abc") + int("345")) # ValueError: invalid literal for int() with base 10: 'abc'

#Correct and make this line of code run without errors
print("Number of letters in your name: " + len(input("Enter your name: "))) # TypeError: can only concatenate str (not "int") to str


name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)
print(type("Number of letters in your name: ")) #string
print(type(length_of_name)) #int


print("Number of letters in your name: " + str(len(input("Enter your name: ")))) # Corrected line

