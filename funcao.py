from datetime import timezone
data = timezone()
#Declarar uma função
def bom_dia():
    print("Bom Dia!!")

def boa_tarde():
    print("Boa Tarde!!")

def boa_noite():
    print("Boa noite!!")

def boa_madrugada():
    print("Boa Madrugada!!")

if data >= 4:
    bom_dia()
elif data >= 12:
    boa_tarde()
elif data >= 18:
    boa_noite()
elif data >= 00:
    boa_madrugada()

