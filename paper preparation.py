import random
print("generating 3 random integer between 100 andd 999 divisible by 5")
for num in range(5):
    print(random.randrange(100,999,5),end=',')
