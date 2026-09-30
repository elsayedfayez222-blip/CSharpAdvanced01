# variables

g = 9  # الشرطه دي معناها كمل السطر الجاي معابا
print(g)

j = 7 + 5
+3
print(j)

s, e, r = 1, 2, 3
print(s)
print(e)  # في اللغه دي مش هيفرق لو نفس المتغير خد نفس القيمه لانها بتترجم سطر بسطر
print(r)  # وعلي حسب البرينت فين هتطبع القيمه الي قبلوا
s = e = r = 10
print(s)
print(e)
print(r)
del r  # بتحزف المتغير من الزاكره وركز ان اللغه شغاله سطر بسطر


# تسمه المتغيرات
MyName = "Elsayed"  # Camel cace
my_name = "Elsayed"  # snake cace

# Advanced Concepts  =================================================

# أرقام صغيرة (تخضع للـ Interning)
x = 100
y = 100  # is معناها هل للمتغرين مكان واحد في الزاكره
print(x is y)  # هيطبع True (لأنهم بيشاوروا على نفس المكان بالظبط) /////////////////////////////

# أرقام كبيرة (لا تخضع للـ Interning في بعض بيئات التشغيل)
num1 = 500
num2 = 500
print(num1 is num2)  # هيطبع False (كل واحد واخد مكان مستقل في الذاكرة)

import sys  # مكتبه

# إنشاء قائمة في الذاكرة والإشارة إليها بمتغير واحد
my_list = [1, 2, 3]
print(sys.getrefcount(my_list) - 1)  # هيطبع 1 (متغير واحد بيشاور عليها)
# عمل متغير جديد يشاور على نفس القائمة
another_ref = my_list
print(sys.getrefcount(my_list) - 1)  # هيطبع 2 (متغيرين بيشاوروا على نفس المكان)
# getrefcount الداله دي لما الكائن يتحول لارجيومنت جواها يعتبر ده اشاره جديده علي الكائن علشان كده طرحنا 1

# Nested Unpacking
# بيانات مستخدم قادمة من قاعدة البيانات (معرف، اسم، وتفاصيل الاتصال)
user_data = (101, "Elsayed", ("Egypt", "Cairo"))
# تفكيك متداخل في سطر واحد
user_id, name, (country, city) = user_data
print(user_id)  # 101
print(country)  # Egypt
print(city)  # Cairo
age = 19
# عرض كل العمليات الرياضية والدوال المتاحة لمتغير من نوع int
print(dir(age))  # هيطبع قائمة طويلة بالعمليات المتاحة جوه اللغة للـ int

print(id(x))
