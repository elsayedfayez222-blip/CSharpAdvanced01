# الحروف تتحول لشكل يفهمه الكمبيوتر، والعملية دي اسمها الترميز أو التشفير (Encoding).
# بايثون بيستخدم نظام ترميز عالمي اسمه Unicode، وده بيسمح له يتعرف على كل الحروف بلغات العالم المختلفة

Name = "Elsayed"
Name = "Elsayed"

# النصوص عبارة عن مصفوفات
print(Name[0])  # المصفوفه دايما تبدا من 0

# حساب طول النص باستخدام الدالة len()
print(len(Name))

# دمج النصوص (String Concatenation)
D = Name + Name
print(D)

H = "mo\
fayez"  # بتخليك تكتب نص طويل على كذا سطر في الكود بس يظهر سطر واحد في
print(H)

name = "Ali"
age = 19
# بايثون هيشيل القوس بالمتغير ويصب قيمته مكانه تلقائياً
print(
    f"My name is {name} and I am {age} years old."
)  # F معناها ان اي حاجه جوه الدبل كوتيشن حتي لو متغير هتطبع استرنج ومش لازم تحولها لكاستنج
print("My name is " + name + " and I am " + str(age) + " years old.")
