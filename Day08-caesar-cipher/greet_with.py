#Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is like in {location}")

greet_with("Angela", "London")
greet_with("London", "Angela")
# Hello London, what is like in Angela
greet_with(name="Angela", location="London")
greet_with(location="London", name="Angela")
	#Hello"Angela, what is like in London