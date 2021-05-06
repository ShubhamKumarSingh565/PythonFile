# Operators Precedence

 # ()
 # **
 # * /
 # + -

x = 5 * 4 + (6 - 4) ** 2 + 5
''' 
Flow goes like-
  first () : inside i.e., 6 - 4 = 2    # 5 * 4 + 2 ** 2 + 5 
  second **: power i.e., 2 ** 2 = 4    # 5 * 4 + 4 + 5
  Third *  : multiple i.e., 5 * 4 = 20 # 20 + 4 + 5
  fourth + : add i.e., 20 + 4 + 5 = 29 
'''
print(x)