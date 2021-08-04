
import requests 
import time
import os

def new():
    print("""
  ███                ██████              █████      ███            
 ░░░                ███░░███            ░░███      ░░░             
 ████  ████████    ░███ ░░░   ██████     ░███████  ████  ████████  
░░███ ░░███░░███  ███████    ███░░███    ░███░░███░░███ ░░███░░███ 
 ░███  ░███ ░███ ░░░███░    ░███ ░███    ░███ ░███ ░███  ░███ ░███ 
 ░███  ░███ ░███   ░███     ░███ ░███    ░███ ░███ ░███  ░███ ░███ 
 █████ ████ █████  █████    ░░██████     ████████  █████ ████ █████
░░░░░ ░░░░ ░░░░░  ░░░░░      ░░░░░░     ░░░░░░░░  ░░░░░ ░░░░ ░░░░░ 

   Created by cholohatwhite : https://github.com/ch0l0hatwhite
   
""")  
    bi=int(input(" Ingresa Los primeros 6 Digitos de el bin >>"))
    print("")
    r=requests.get(f"https://lookup.binlist.net/{bi}").text
    print( r )
    exp=str(input(" Exportar a archivo .txt ? [ yes / no ] "))
    if exp=="y" or "yes" :
        f = open ('datos-bin.txt','w',encoding='utf-8')
        f.write(f"datos de el bin : \n\n {r}")
        f.close()
        print("\n\nArchivo exportado a texto exitosamente !\n\n",sep='-')
        
        
    else:
        new()
    



new()








