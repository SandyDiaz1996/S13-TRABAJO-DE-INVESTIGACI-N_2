from helpers import borrarPantalla, gotoxy
import time
from colorama import Fore
import datetime


class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        print(Fore.LIGHTBLUE_EX + "              **********************************************************");gotoxy(self.col,self.fil);print(self.titulo);
        self.col-=5
        gotoxy(self.col+5,self.fil+1);print("**********************************************************")
        for opcion in self.opciones:
            self.fil +=2
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+1);print("**********************************************************")
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones))) 
        return opc   

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col, fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
                else:
                   gotoxy(col,fil);print("Solo positivos") 
                   time.sleep(2)
                   gotoxy(col, fil);print(" "*20)
            except:
                gotoxy(col, fil);print("------> | {} ".format(mensajeError))
                time.sleep(2)
                gotoxy(col, fil);print(" "*20)
        return valor

    def solo_letras(self,mensajeError,col,fil): 
        while True:
            gotoxy(col,fil) 
            valor = str(input())
            if valor.isalpha():
                break
            else:
                gotoxy(col,fil);print("------> | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col, fil);print(" "*30)
        return valor

    def solo_decimales(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil) 
            valor = input()
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                gotoxy(col, fil);print("          ------><  | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col, fil);print(" "*50)
        return valor
    
    def solo_boleanos(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil) 
            valor = input()
            try:
                if valor.isnumeric():
                    if valor == 0 or valor == 1:
                        break
                    else:
                        gotoxy(col, fil);print("Solo se aceptan: [0] o [1]")
                        time.sleep(1)
                        gotoxy(col, fil);print(" "*32)
                
                elif valor.isalpha():
                    if valor == "True" or valor == "False":
                        break

                    else:
                        gotoxy(col, fil);print("Solo se aceptan: [True] o [False]")
                        time.sleep(1)
                        gotoxy(col, fil);print(" "*33)
                
                else:
                    gotoxy(col, fil);print("------><  | {} ".format(mensajeError))
                    time.sleep(1)
                    gotoxy(col, fil);print(" "*32)

            except:
                gotoxy(col, fil);print("------><  | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col, fil);print(" "*32)
        return valor
    
    def validar_cedula(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil) 
            valor = input()
            if valor.isnumeric():
                l = len(valor)
                if l == 10:
                        break
                else:
                    gotoxy(col, fil);print("------>< | {} ".format(mensajeError))
                    time.sleep(1)
                    gotoxy(col, fil);print(" "*38)
            else:
                gotoxy(col,fil);print("Solo números")
                time.sleep(1)
                gotoxy(col, fil);print(" "*38)
        return valor

    def validar_ruc(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil) 
            valor = input()
            l = len(valor)
            if l == 14:
                break
            else:
                gotoxy(col, fil);print("------>< | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col, fil);print(" "*38)
           
            return valor
    
    def validar_tel(self,mensajeError,col,fil):
        while True: 
            gotoxy(col, fil)            
            valor = input()
            if valor.isnumeric():
                if int(valor) >= 0:
                    l = len(valor)
                    if l == 10:
                                break
                    else:
                        gotoxy(col,fil);print("No es un número telefónico!!!") 
                        time.sleep(1)
                        gotoxy(col, fil);print(" "*38)
                else:
                    gotoxy(col, fil);print("------> | {} ".format(mensajeError))
                    time.sleep(1)
                    gotoxy(col, fil);print(" "*38)
            else: 
                gotoxy(col,fil);print("Solo números")
                time.sleep(1)
                gotoxy(col, fil);print(" "*38)
        return valor
    
    def validar_rol(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil) 
            valor = str(input())
            if valor.isalpha():
                if valor == "A" or valor == "O":
                    break

                else: 
                    gotoxy(col,fil);print("{} ".format(mensajeError))
                    time.sleep(1)
                    gotoxy(col, fil);print(" "*23)
                    
            else:
                gotoxy(col,fil);print("Solo letras")
                time.sleep(1)
                gotoxy(col, fil);print(" "*23)
        return valor

        
    """def validar_fecha(self,mensajeError,col,fil):
        while True:
            try:
                gotoxy(col, fil)            
                valor = input()
                datetime.strptime(valor, '%Y-%m-%d')
                break

            except:
                gotoxy(col, fil);print("------><  | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col, fil);print(" "*32)"""


    """def validar_fecha(self,mensajeError,col,fil):
        while True: 
            gotoxy(col, fil)            
            valor = input()
            if valor == datetime.datetime.strptime(valor, '%Y-%m-%d'):
                 break
            else:
                gotoxy(col,fil);print("------> | {} ".format(mensajeError)) 
                time.sleep(1)
                gotoxy(col, fil);print(" "*38)"""
