#def test(outputs):
#    for i in range(outputs):
#        print(f"{i+1}. Hello")
#        i += 1
#
#test (int(input("XD: ")))
#
#
#x = int(input("XD2: "))
#for i in range(x):
#    print(f"{i+1}. Hello")
#    i += 1

#====[ทั้งคู่รันเหมือนกัน]======


#====[Debug Partice]======
#def introduction(x):
#    print(f"My name is: {x}\n======================\n")
#introduction(x = (input("Input your name: ")))
#
#
#def age():
#    youAge = input("Enter your age: ")
#    print("Your age is: ", youAge)
#age()
#

# def introduction():
#     print(f"My name is: Beam\n======================\n")

# introduction()

# import time
# def spam(times):
#     for i in range(times):
#         i += 1
#         print(f"รอบที่ {i}. Yo")
#         time.sleep(0.5)
# spam(int(input("Spam times: ")))

# =====[How to return]========
# def my_sum(a, b):
#     return a + b

# a = int(input("Enter number1: "))
# b = int(input("Enter number2: "))

# print(my_sum(a, b))

x = ["data1", "data2", 2, 3]
# print(x[0])
# x[0] = "1data"
# print(x[0])

# sum = (x[2] + x[3])
# print(sum)

# x[2] = "ton"
# print(x[2])

# x.append("data3")
# print(x[4])      
# print(x)     

# a = "amogus"
# x.append(a)
# print(x[5])
# print(x)     

# for i in range(3):
#     x.append(i)
#     i += 1
# print(x)

# x.pop(3)
# print(x)

# pos = 0
# for i in x:
#     pos += 1
#     if i == 2:
#         print(f"Found 2 at position: {pos}")
#         print(x)

# dict_a = {
#     "sword": 80,
#     "gun": 70
# }
# weapon = input("Choose Weapon: ")
# print(dict_a[weapon])
# print("Added bow to your inventory!")

# dict_a["bow"] = 35
# print(dict_a)
# # dict_a["sword"] = 20
# # print(dict_a["sword"])

students = [
    {"name": "Tom", "id": 10, "score": 85},
    {"name": "Jerry", "id": 34, "score": 76},
    {"name": "Skibidi", "id": 12, "score": 99},
    {"name": "tung sahur", "id": 11, "score": 42},
    {"name": "amogus", "id": 12, "score": 65}
]

def grader():
    print(f"id | Name     | score  | grade")
    for student in students:
        if student["score"] > 80:
            student["grade"] = "A" 
        elif student["score"] > 70:
            student["grade"] = "B"
        elif student["score"] > 60:
            student["grade"] = "C"
        elif student["score"] > 50:
            student["grade"] = "D"
        else:
            student["grade"] = "F"

        print(student["id"], student["name"], student["score"], student["grade"])

        
grader()

# def checkMoney(list_of_student):
#     for student in list_of_student:
#         if student["money"] > 500:
#             print(student["name"], "you rich")
#         else:
#             print(student["name"], "you poor")

# students = [
#     {"name": "Skibidi", "money": 400},
#     {"name": "Ton", "money": 900}
# ]

# checkMoney(students)