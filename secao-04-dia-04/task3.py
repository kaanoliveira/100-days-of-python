# Banker Roulette

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_name = random.choice(friends)
print(random_name)

random_index = random.randint(0, 4)
print(friends[random_index])

random_index2 = random.randint(0, len(friends) - 1)
print(friends[random_index2])