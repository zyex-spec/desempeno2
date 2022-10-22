class Cliente:
    nombre = ''
    apellido = ''
    cedula = ''
    ciudad = ''
     
    def print_nombre(self):
        print (self.nombre)
         
    def print_apellido(self):
        print (self.apellido)

    def print_cedula(self):
        print (self.cedula)
         
    def print_ciudad(self):
        print (self.ciudad)
     
cliente1 = Cliente()
cliente1.nombre = 'Sebas'
cliente1.apellido = 'Gallego'
cliente1.cedula = '1020451096'
cliente1.ciudad = 'Medellín'

cliente1.print_nombre()
cliente1.print_apellido()
cliente1.print_cedula()
cliente1.print_ciudad()

class Cuenta:
    numeroCuenta=''
    saldo=''

    def print_numCuenta(self):
        print (self.numeroCuenta)

    def print_saldo(self):
        print (self.saldo)

cuenta1 = Cuenta()
cuenta1.numeroCuenta = '123456'
cuenta1.saldo = '5000'

cuenta1.print_numCuenta()
cuenta1.print_saldo()

guardian  = 100


## Ciclo While
print("Menu")
print("1.Consultar Saldo")
print("2. Ingresar ")
print("3.Retirar")
print("0. Salir")
while guardian!=0:
    
    guardian = int(input("Digita una opcion"))
    if guardian ==1:
         print(f"El saldo es  $" + (cuenta1.saldo) )
         
    elif guardian ==2:
         dinero = int(input("Digita el monto"))
         suma = dinero + int(cuenta1.saldo)
         print(suma)
    
    elif guardian ==3:
         dinero2 = int(input("Digita el monto a restar"))
         resta =int(cuenta1.saldo) - dinero2 
         print(resta)

    
    elif guardian ==0:
         print()

        
    elif guardian ==0:
        break
    else:
        print("no valido")

else:
    print("Terminé")