# val1 = True
# val2 = False
# print(f"True and False= {val1 and val2}")
# print(f"True or False= {val1 or val2}")
# print(f"True not  = { not val1}")
result1 = input("username: ")
result2 = int(input("password: "))

if result1 == "Muhammadaziz" and result2 == 123:
    print("siz tizimga kirdingiz")
else:
    print("siz tizimga kirmadingiz ")

result1 = int(input("Bitta son kiriting  va biz shu sonni toq yoki juftligini aniqlaymiz:  "))
if result1 % 2== 0 :
    print("bu son juft songa kiradi ")
else:
    print("bu son toq songa teng ")



