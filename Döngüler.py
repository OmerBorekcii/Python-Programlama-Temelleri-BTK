liste = ['ali','can',1,2,3,4]
print(liste)
print('ali' in liste)

isim = input("İsim:")
if isim in liste:
    print("OK")
if isim not in liste:
    print("NOT")

for a in range(10,12,2):
    print(a)

for x in range(1,30):
    if(x % 2 == 1):
        print(x)

x = 0
while(x < 10):
    print(x)
    x += 1

while(True):
    y = float(input("Sayı:"))
    print(y*y)
    if(y == 0):
        break

for A in range(100):
    if(A % 7 == 0):
        continue
    print(A)

for X in range(1,11):
    for Y in range(1,11):
        print(X,"*",Y,"=",X*Y)
    print("\n")
    
    
