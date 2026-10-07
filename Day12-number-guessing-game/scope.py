enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope: Variables created inside a function belong to the local scope of that function, and can only be used inside that function.

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(drink_potion())

# Global Scope: Variables created in the main body of the Python code are considered to be in the global scope, and can be used by anyone, both inside functions and outside functions.

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)
