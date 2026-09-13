# Calculate the bmi using weight and height.
height = 1.65 
weight = 84
bmi = weight / height ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2)) # round to 2 decimal places


score = 0

#User scores a point
score += 1 # = score = score + 1
print(score)

# f-strings
print("Your score is " + str(score))
print(f"Your score is {score}")

score = 0
height = 1.8
is_winning = True
print(f"Your score is {score}, your height is {height}. You are winning is {is_winning}")