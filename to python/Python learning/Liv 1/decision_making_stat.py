# Control flow: If / else, else if
mark = int(input("Enter your grade: "))
if mark >= 90 and mark <= 100:
    print("Mark = A")
elif mark >= 80 and mark < 90:
    print("Mark = B")
elif mark >= 70 and mark < 80:
    print("Mark = C")
elif mark >= 60 and mark < 70:
    print("Mark = D")
else:
    print("Mark = F")

# Nested If
age = 19
has_id = True

if age >= 18:
    print("السن مناسب")
    if has_id:
        print("اتفضل ادخل المعمل ")
    else:
        print("السن تمام بس فين الكارنيه؟")
else:
    print("ممنوع الدخول للقصر")


# Ternary Operator تستخدم في الشروط البسيطه السريعه=
score = 85
# باستخدام الـ Ternary Operator في سطر واحد
status = "ناجح" if score >= 50 else "راسب"

print(status)  # الناتج: ناجح


# Match statement هي السوتش في C++
# عادي جدا لو حطيت شرط في بدايه الماتش بس في النهايه هيططلع منه قيمه تقارنها في الكييس
match mark:
    case x if (
        x >= 90 and x <= 100
    ):  # دي طريقه كتابه شرط في الكيس واكس دي صدوق اخد قيمه المتغير
        print("A")
    case 50 | 40 | 30 | 20:  # | معناها Or
        print("F")
    case 50:  # لما احط اي قيمه من اي نوع داتا من غير اي شروط كده انا بسندها للمتغير
        print("Dun")
    case _:
        print("sheeeeeeeeet")  # دي سنتاكس اخر كيس متنساش ال ___
