dig= input("Ingrese un numero: ")
print(f"Proceso de reduccion para {dig}")
while len(dig)>1:  
    x=0  
    for i in dig:
        y=int(i)
        x+=y
    print(f"{dig} = {x}")
    dig=str(x)
print(f"El resultado final es: {dig}")