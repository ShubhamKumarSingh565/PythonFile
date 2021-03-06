# Python Data Types

'''

1. Numbers : Integer, Complex Number, Float
2. Sequence Type : Strings, List, Tuple, range
3. Boolean
4. Set
5. Dictionary

'''
# 1. Numbers : Integer, Complex Number, Float
# Integer
print("Integer")
print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 ** 3) # power of
print(17 / 3)
print(17 // 3)
print(type(2 + 5))
# Float
print("\nFloat")
print(2.3)
print(2 / 3)
print(5 / 5)
print(4.9 + 0.1)
# Complex Number
print("\nComplex Number")
print(1j)
print(1 + 1j)
print(type(1 + 1j))

# 2. Sequence Type : Strings, Lists, Tuple, range
#Text Type - Str
print("\nStrings\n")
print("This is String")
isString = "Hello, Buddy"
print(isString)
print(type(isString))
# Lists
print("\nLists")
print(["apple", "banana", "Cherry"])
lst = [ ["Potato", "Onion", "Bringle"],
        ["Rice", "Dal", "Curd"] ]
print(lst)
print(type(lst))
# Tuple
print("\nTuple")
print(("apple", "banana", "Cherry"))
tpl = (("Potato", "Onion", "Bringle"),
       ("Rice", "Dal", "Curd"))
print(tpl)
print(type(tpl))
# Range
print("\nRange")
print(range(6))
print(range(1, 6))
print(type(range(5)))

# 3. Boolean
print("\nBoolean")
x = 4
y = 5
print(x == y)
print(type(x == y))

# 4. Set
print("\nSet")
print({"apple", "banana", "Cherry"})
sets = {"Potato", "Onion", "Bringle", "Rice", "Dal", "Curd"}
print(sets)
print(type(sets))

# 5. Dictionary
print("\nDictionary")
dic = {"Name": "Shubham Ji", "Age" : 20}
print(dic)
print(type(dic))
