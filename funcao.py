#Declarar uma função
def saudacoes(hora_do_dia):
    if hora_do_dia >= 0 and hora_do_dia <= 12:
        print("Bom Dia!")
    elif hora_do_dia >= 13 and hora_do_dia <= 18:
        print("Boa Tarde!")
    else:
        print("Boa Noite!")

resposta = int(input("Digite que horas são:\n"))

saudacoes(resposta)