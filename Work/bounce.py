# bounce.py
#
# Exercise 1.5

height = 100.0  # Initial height in meters

bounce_back = 3/5
bounces = 11


for i in range(1, bounces):
    height = height * bounce_back
    print(f"After bounce {i}, height is {height:.2f} meters")




