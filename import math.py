import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطأ: القسمة على صفر غير معرفة"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "خطأ: لا يمكن حساب الجذر التربيعي لعدد سالب"
    return math.sqrt(x)

def logarithm(x, base=10):
    if x <= 0:
        return "خطأ: اللوغاريتم غير معرف للأعداد صفر أو سالبة"
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    print("مرحباً بك في الآلة الحاسبة المتكاملة")
    print("العمليات المتاحة:")
    print("1. جمع (+)")
    print("2. طرح (-)")
    print("3. ضرب (*)")
    print("4. قسمة (/)")
    print("5. أس (^)")
    print("6. جذر تربيعي (sqrt)")
    print("7. لوغاريتم (log)")
    print("8. جيب (sin)")
    print("9. جيب تمام (cos)")
    print("10. ظل (tan)")
    print("11. خروج")

    while True:
        choice = input("اختر العملية (1-11): ")

        if choice == '11':
            print("شكراً لاستخدامك الآلة الحاسبة. إلى اللقاء!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("أدخل الرقم الأول: "))
                num2 = float(input("أدخل الرقم الثاني: "))
            except ValueError:
                print("خطأ: يرجى إدخال أرقام صحيحة.")
                continue

            if choice == '1':
                print(f"النتيجة: {add(num1, num2)}")
            elif choice == '2':
                print(f"النتيجة: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"النتيجة: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"النتيجة: {divide(num1, num2)}")
            elif choice == '5':
                print(f"النتيجة: {power(num1, num2)}")

        elif choice == '6':
            try:
                num = float(input("أدخل الرقم: "))
            except ValueError:
                print("خطأ: يرجى إدخال رقم صحيح.")
                continue
            print(f"النتيجة: {sqrt(num)}")

        elif choice == '7':
            try:
                num = float(input("أدخل الرقم: "))
                base = input("أدخل الأساس (افتراضي 10): ")
                if base == '':
                    base = 10
                else:
                    base = float(base)
            except ValueError:
                print("خطأ: يرجى إدخال أرقام صحيحة.")
                continue
            print(f"النتيجة: {logarithm(num, base)}")

        elif choice == '8':
            try:
                angle = float(input("أدخل الزاوية بالدرجات: "))
            except ValueError:
                print("خطأ: يرجى إدخال رقم صحيح.")
                continue
            print(f"النتيجة: {sine(angle)}")

        elif choice == '9':
            try:
                angle = float(input("أدخل الزاوية بالدرجات: "))
            except ValueError:
                print("خطأ: يرجى إدخال رقم صحيح.")
                continue
            print(f"النتيجة: {cosine(angle)}")

        elif choice == '10':
            try:
                angle = float(input("أدخل الزاوية بالدرجات: "))
            except ValueError:
                print("خطأ: يرجى إدخال رقم صحيح.")
                continue
            print(f"النتيجة: {tangent(angle)}")

        else:
            print("اختيار غير صحيح، يرجى المحاولة مرة أخرى.")

if __name__ == "__main__":
    calculator()
