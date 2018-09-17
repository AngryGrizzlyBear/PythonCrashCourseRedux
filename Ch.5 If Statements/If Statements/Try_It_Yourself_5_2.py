# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# •	 Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# •	 Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)
# 5
alien_color = ['green']

if 'green' in alien_color:
    print("You just earned 5 points.")
else:
    print("The color is not green.")

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain.
# •	 If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# •	 If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# •	 Write one version of this program that runs the if block and another that
# runs the else block.

alien_color = ['red']

if 'green' in alien_color:
    print("You just earned 5 points.")
else:
    print("You just earned 10 points.")

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
# chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

alien_color = ['red']

if 'green' in alien_color:
    print("You just earned 5 points.")
elif 'yellow' in alien_color:
    print("You just earned 10 points.")
elif 'red' in alien_color:
    print("You just earned 15 points.")
else:
    print("There aren't any aliens to shoot!")

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
# •	 If the person is less than 2 years old, print a message that the person is
# a baby.
# •	 If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.
# •	 If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
# •	 If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# •	 If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# •	 If the person is age 65 or older, print a message that the person is an
# elder.

stages_of_life = 70

if stages_of_life < 2:
    print("You're just a baby.")
elif stages_of_life < 4:
    print("You're a toddler.")
elif stages_of_life < 13:
    print("You're a kid.")
elif stages_of_life < 20:
    print("You're a teenager.")
elif stages_of_life < 65:
    print("You're an adult.")
else:
    print("You're old.")