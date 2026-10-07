# Modifying Global Scope
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

def increase_enemies2(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies2(enemies)
print(f"enemies outside function: {enemies}")