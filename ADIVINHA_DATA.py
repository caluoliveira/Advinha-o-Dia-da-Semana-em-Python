#Faça um algoritmo que lê uma data informada pelo usuário (ano, mês e dia) e informe qual o dia da
#semana dessa data (Segunda, Terça, Quarta, Quinta, Sexta, Sábado ou Domingo).
#Para isso, siga as etapas a seguir.
#Faça um algoritmo que lê uma data informada pelo usuário (ano, mês e dia)
dia=int(input("Informe o dia: \n"));
mes=int(input("Informe o mês: \n"));
ano_atual=int(input("Informe o ano: \n"));
#Passo 1) Calcule quantos anos se passaram desde 1900 até o ano informado;
ano_base=1900;
passo1=ano_atual-ano_base
#Passo 2) Calcule quantos dias “29 DE FEVEREIRO” existiram depois de 1900.
# Para isto, basta dividir por 4 o número obtido na 1° etapa, sem considerar o resto da divisão.
passo2=(passo1//4)
#Passo 3) Pegue o seu dia informado
passo3=dia
#Passo 4) Obtenha o número associado ao mês informado, a partir da tabela:
#Janeiro 0  Fevereiro 3 Março 3
#Abril 6    Maio 1       Junho 4
#Julho 6    Agosto 2     Setembro 5
#Outubro 0  Novembro 3  Dezembro 5
if (mes == 1):
    passo4=0
elif (mes == 2):
    passo4 = 3
elif (mes == 3):
    passo4 = 3
elif (mes == 4):
    passo4 = 6
elif (mes == 5):
    passo4 = 1
elif (mes == 6):
    passo4 = 4
elif (mes == 7):
    passo4 = 6
elif (mes == 8):
    passo4 = 2
elif (mes == 9):
    passo4 = 5
elif (mes == 10):
    passo4 = 0
elif (mes == 11):
    passo4 = 3
elif (mes == 12):
    passo4 = 5
else:
    print ("Entrada inválida! \n")
# Passo 5) Some os números obtidos nas quatro etapas anteriores eobtenha o resto da divisão por 7.
passo6=(passo1+passo2+passo3+passo4)%7
#Passo 6) Procure na tabela abaixo o número obtido na etapa 5 e você terá o dia da semana informado pelo cliente.
# #0 Domingo 1 Segunda 2 Terça  3 Quarta 4 Quinta 5 Sexta 6 Sábado
if (passo6 == 0):
    print("A data informada corresponde a: DOMINGO \n")
elif (passo6 == 1):
    print("A data informada corresponde a: SEGUNDA-FEIRA \n")
elif  (passo6 == 2):
    print("A data informada corresponde a: TERÇA-FEIRA \n")
elif  (passo6 == 3):
    print("A data informada corresponde a: QUARTA-FEIRA \n")
elif  (passo6 == 4):
    print("A data informada corresponde a: QUINTA-FEIRA \n")
elif  (passo6 == 5):
    print("A data informada corresponde a: SEXTA-FEIRA \n")
elif  (passo6 == 6):
    print("A data informada corresponde a: SÁBADO \n")
else:
    print ("Entrada inválida! \n")

