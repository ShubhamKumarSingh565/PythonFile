# Python if else
"""
if statements
if else statements
elif statements
"""

# if statement
print("----if statements-----")
print("Check the number is even or not")
num = int(input("Enter the number?: "))
if num % 2 == 0:
  print("Number is even")

# if-else statement
print("\n----if-else statements----")
print("Check that you are eligible to vote or not")
age = int(input("Enter your age?: "))
if age >= 18:
  print("😀 Wow!, you are eligible..")
else:
  print("😥 Sorry!, you have to wait..")

# elif statement
print("\n----elif statements----")
marks = int(input("Enter your marks: "))
if marks > 85 and marks < 100:
  print("😄 Congrates!, your score grade is A..")
elif marks > 60 and marks < 80:
  print("Your score grade is B+..")
elif marks > 40 and marks < 60:
  print("Your score grade is B..")
elif marks > 30 and marks < 40:
  print("Your score grade is C..")
else:
  print("😥 Sorry!, you are fail..")