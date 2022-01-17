from audioop import mul


print("numero enteros entre 0 y 150")
for i in range(0,151):
    print(i)

print("multiplos de 5 entre 5 y 100")
for i in range(5,1001):
    if i%5 == 0:
        print(i)

print("Contar, a la manera del Dojo")
for i in range(1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)

print ("Whoa")
sum = 0
for i in range(0,500001):
    if i%2 == 0:
        sum+=i

print(sum)

print("Cuenta regresiva de a 4")
for i in range(2018,0,-4):
    print(i)

print("Contador flexible")
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum,highNum+1):
    if i%mult == 0:
        print(i)

