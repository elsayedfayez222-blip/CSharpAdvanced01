# for loop
for i in range(
    5
):  # in بتاخد القيم من المتغير الي بعده وتحطها في المتغير الي قبلها وتطبع في كل مره
    print(i)


for name in ["mo", "jo"]:
    print(
        name
    )  # خد اول فيمه في الليست حطها في المتغير وامر الطبعه كان طباعه المتغير وكرر العمليه علي الاتنين

for i, o in enumerate(
    range(5)
):  # enumerate داله بترجع رقم اللفه مع العناصر كل عنصر معاه رقمه اللفه
    print(
        f"{i} : {o}"
    )  # بتحتاج طبعا متغيرين علشان واحد يشيل قيمه العناصر والتاني يشيل رقم اللفه


names = ["Ali", "Ahmed"]
scores = [85, 90]
for name, score in zip(names, scores):  # zip مهمه في الليست لما يكون عندي ليستتين
    print(
        f"{name} -> {score}"
    )  # عايز اتحكم في كل العناصر فيهم بطريقه معينه سواء ان كانت طباعه او تغير او ادخال


num = [6, 7, 4]
for o, m in enumerate(num):
    print(f" {o} -> {m * m}")


# while loop
u = 2
while u >= 0:
    print(u)
    u = u - 1

# Nested loop
for i in range(9):
    for n in range(9):
        print(
            0, end=" "
        )  # end معناها اطبع الكل علي سطر واحد واي حاجه بين الدبل كوتيشن بتتطبع بين كل طباعه
    print()  # البرينت دي معناها ان بقول انزل سطر جديد بعد متخلص جوه
