from time import sleep

a = input('Enter number: ')
b = 0
c=""
a=int(a)

while b!=3:

    while a % 2 == 1:
        a=a*3
        a=a+1
        print(a)
        c=str(a)
        file=open("C:/Users/utente/Desktop/programmazione/Py_project/3x+1.txt", "w")
        file.write("/n "+c)
        file.close
        sleep(1)

    while a % 2 == 0:
        a=a/2
        print(a)
        c=str(a)
        file=open("C:/Users/utente/Desktop/programmazione/Py_project/3x+1.txt", "w")
        file.write("/n "+c)
        file.close
        sleep(1)

    if a==1:
        b=b+1

    c=str(a)

    file=open("C:/Users/utente/Desktop/programmazione/Py_project/3x+1.txt", "w")
    file.write("/n "+c)
    file.close
