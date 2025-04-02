import User
print("What is your height in inches?")
height=input()
print("What is your weight in pounds?")
weight=input()

person=User.User(height,weight)

print("User made that is "+person.height+" inches tall and weighs "+person.weight+" pounds")