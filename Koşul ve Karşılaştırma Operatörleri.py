user = "admin"
password = 1234

user_input = str(input("Kullanıcı Adı:"))
password_input = int(input("Şifre:"))

if(user_input == user and password_input == password):
    print("Hoşgeldin")
else:
    print("Hata")
