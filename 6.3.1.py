x=input("Dame una lista de numeros: ")
lista= x.split()
z=[]
for i in x:
    if i not in z:
        z.append(i)
for i in z:
    print(i,end=" ")
