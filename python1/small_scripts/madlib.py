"""
LESSON: 1.2 - Values
EXERCISE: Code Your Own

TITLE: Physics Mad-lib
DESCRIPTION: A mad lib that uses math to make a scientifically-accurate story
"""

# Program intro
print("Welcome to the physics madlib!")
print("This is a madlib that uses physics math to make it scientifically accurate")
print("")

# Get user input for first calculation (gravitational energy)
print("For an object that is close to falling: ")
mass1 = float(input("Enter object mass (in Kilograms): "))
gravity = float(input("Enter gravity (in Meters per Second): "))
height = float(input("Enter object fall height (in Meters): "))
noun1 = input("Object name: ")
noun4 = input("Name of the planet/moon this is happening on: ")
print("")

# Get user input for second calculation (kinetic energy)
print("For a quickly-moving object: ")
mass2 = float(input("Enter object mass (in Kilograms): "))
vel = float(input("Enter object velocity (in Meters per Second): "))
noun2 = input("Object name: ")
print("")

# get parts of speech
noun3 = input("Enter the name of a famous person: ")
verb1 = input("Enter a past-tense verb: ")
adj1 = input("Enter an adjective: ")
print("")

# Calculate the results
potentialEnergy =  mass1 * gravity * height
gpf = "U =  mgh"
kineticEnergy = (1/2) * mass2 * (vel ** 2)
kf = "K.E. = 1/2 m v^2"

# The story part 1
print("\n \n")
print("An unfortunate situation \n")
print("One day, " + noun3 + " " + verb1 + " a " + adj1 + " " + noun2 + " at a " + noun1 + " near a cliff on " + noun4 + ".")

# First equation
print("Formula for Kinetic Energy: " + kf)
print(str(kineticEnergy) + " joules = 1/2 x " + str(mass2) + " kilograms x " + str(vel) + "^2 m/s velocity")
print("The kinetic energy of the " + noun2 + ": " + str(kineticEnergy))

# The story part 2
print("The " + noun1 + " plummeted to the ground to utter destruction.")

# Second equation
print("Formula for Gravitational Potential Energy: " + gpf)
print(str(potentialEnergy) + " joules = " + str(mass1) + " kilograms x " + str(gravity) + " m/s gravity x " + str(height) + " meters height")
print("The potential energy of the " + noun1 + ": " + str(potentialEnergy))

# Final equation
print("The total energy: " + str(potentialEnergy + kineticEnergy) + " joules")
print("The End!")