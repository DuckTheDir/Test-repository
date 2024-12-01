from functions import hello_who, salary

money = salary(3,5)

if money != 20:
    print("Error")
else:
    print("Good job")
if salary(2,5) != 10:
    print("👿")
else:
    print("good")
if hello_who("Max") != "Hello, Max":
    print("Failed")
else:
    print("Good")
if hello_who("Leo") != "Hello, Leo":
    print("Failed")
else:
    print("👽")


print(hello_who("snickers"))
print(money)



