# Operators in python
"""
 1.Arithmetic operators
 2.Comparison operators
 3.Assignment Operators
 4.Logical Operators
 5.Bitwise Operators
 6.Membership Operators
 7.Identity Operators 
"""
# 1.Arithmetic Operators
print("Arithematic operators")
"""
 +  : Addition
 -  : Subtraction
 *  : Multiplication
 /  : Divide
 %  : Reminder
 ** : Exponent
 // : Floor division
"""
x, y = 8, 6
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# 2.Comparision operators
print("\nComparision operators")
"""
 == : 
 != :
 >= :
 <= :
 >  :
 <  :
"""
a, b = 5, 6
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

# 3.Assignment Operators
print("\nAssignment operators")
"""
 =   :
 +=  :
 -=  :
 *=  :
 %=  :
 **= :
 //= :
"""
c, d = 2, 3
print(c, d)
c += 2
print(c)
c -= 1
print(c)
c %= 2
print(c)
d //= 2
print(d)

# 4.Logical Operators
print("\nLogical operators")
"""
 and :
 or  :
 not :
"""
e,  f = 3, 4
print(e<4 and f>3)
print(e>2 or f<3)
print( not(e>2 or f<3) )

# 5.Bitwise Operators
print("\nBitwise operators")
"""
 Used to compare binary numbers
 &  : Binary and
 |  : Binary or
 ^  : Binary xor
 ~  : negation
 << : Left shift
 >> : Right Shift
 Example:
   if a =5, b = 3
   then, binary(a) = 101
         binary(b) = 011
   Hence, a & b = 001
          a | b = 111
          a ^ b = 110
           ~a   = 010
"""
k, l = 5, 3
print(k & l)
print(k | l)
print(k ^ l)
print( ~k)
print( k << 2)
print( k >> 2)

# 6.Membership Operators
print("\nMembership operators")
"""
lists, Tuple, Dictionary
 in     : true if the first operand is found in the second operand
 not in : true if the first operand is not found in the second operand
"""
lst = ["Mango", "Apple", "Banana", 5]
print(6 in lst)
print("Apple" in lst)
print( 6 not in lst)
print("Mango" not in lst)

# 7.Identity Operators
print("\nIdentity operators")
"""
 is     : true if the reference present at both sides point to the same object
 is not : true if the reference present at both sides do not point to the same object
"""
print("NITIN" is "NITIN")
print("LILI"  is not "LILI")