def my_function():
    x = 10  # x هنا Local
    print("جوة الدالة:", x)


my_function()

# لو حاولت تطبعه برة الدالة:
# print(x)  <-- NameError: name 'x' is not defined


def outer_function():
    y = "أنا جوة الدالة الخارجية"

    def inner_function():
        # الدالة الداخلية شايفين y الخاصة بالدالة الخارجية
        print("من الدالة الداخلية:", y)

    inner_function()


outer_function()


z = 100  # متغير Global


def check_global():
    print("جوة الدالة شايفين الـ Global:", z)


check_global()
print("وبرة الدالة برضه شايفينه:", z)


counter = 0  # Global


def increment():
    global counter  # بنقول لبايثون: اتعاملي مع counter الأصلي اللي برة
    counter += 1


increment()
increment()
print(counter)  # القيمة بقت 2
