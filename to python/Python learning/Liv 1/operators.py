# Arithmetic Operators
# + , - , % , * , /
s, h = 1, 2
print(s + h)  # SUM
print(s.__add__(h))
print(s - h)  # Sub
print(s * h)  # Mul
print(s / h)  # Div
print(s % h)  # Mod
print(s**h)  # pow


# Comparison Operators
# == و != و < و > و <= و >=
print(s > h)
print(s < h)
print(s >= h)  # هيتعامل Bool
print(s <= h)
print(s == h)
print(s != h)

# الرياضيات والمنطق
GG = (
    2 + 3
) + 2 * 3 / 2 % 2  # القوس الاول بعدها ما دون الجمع والطرح من الشمال لليمين بعدها الجمع والطرح
print(GG)

# Logical Operators
h, u = True, False
# and
if h and u:
    print(h)
else:
    print("oo")
# or
if h or u:
    print(h)
else:
    print("oo")  # الترتيب والاولويه ازاي وجدوا مع بعض
# not              # الاقواس الاول بعديها نوت بعديها اند بعديها اوور
if not u:
    print(h)
else:
    print("oo")
