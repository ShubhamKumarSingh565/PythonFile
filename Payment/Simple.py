"""Question 1 : Write a program to prompt the user for days and rate per day to compute total pay.
Use 50 days and a rate of 3.5 per day to test the program. Total pay is equal to (days* Rate per day).
You should use input to read a string and float() to convert the string to a number.
Don't worry about error checking or bad user data. Good Job!
"""
ud = input("Enter Days: ")
ur = input("Enter Rate: ")
upay = float(ud) * float(ur)
print("You have to Pay: ", upay)