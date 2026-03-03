#Diego Lipa
while False:
    print('Diego')

#Valida Contraseña
contrasenia_correcta = "123456"
intentos = 0

while True:
    contrasenia = input("Ingresa porafor su contraseña: ")
    intentos += 1

    if (contrasenia == contrasenia_correcta):
        print("Contraseña Corecta 👍👍👍")
    else:
        print("Contraseña Incorecta 😭😭😭")
        if(intentos >= 3):
            print('Tarjeta Bloqueada 🫤🫤🫤')
            break

