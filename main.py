# with open('data/pi.txt', 'r') as file:
#     # data = file.read()
#     for i in file:
#         print(i)


# # a = [i+1 for i in range(10)]  #1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# # a = []
# # for i in range(10):
# #     a.append(i+1)
# # print(a)

# import os

# f = open("demofile.txt")
# print(f.readline())
# f.write("Hello, World!")
# f.close()

# import os

# os.remove("data/pi.txt")

# os.mkdir("myfolder")


# # data1 = {}

# # import json

# # with open('myfile.json', 'r') as file:
# #     data = json.load(file)
# #     print(type(data), data)
# #     data["name"] = "Hosbhshbhs"
# #     data1 = data.copy()
    
# # with open('myfile.json', 'w') as file:
# #     json.dump(data, file)
    
    
# import re

# matn = "Bizning operatorlar:  +998919876543 va +998912345678 bilan ishlaydi."
# andoza = r"\+998\d{9}"

# # natija = re.findall(andoza, matn)
# # print(natija) 
# # # Natija: ['+998901234567', '+998919876543']


# moslik = re.search(andoza, matn)
# if moslik:
#     print("Raqam topildi:", moslik.group()) # Natija: +998935554433
# else:
#     print("Raqam topilmadi")