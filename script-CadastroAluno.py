cadast = list()
while True:
    nomeA = str(input("Qual é o nome do aluno a ser cadastrado? \n"))
    nt1 = float(input("Qual é a nota #1 do aluno? "))
    nt2 = float(input("Qual é a nota #2 do aluno? "))
    nt3 = float(input("Qual é a nota #3 do aluno? "))
    nt4 = float(input("Qual é a nota #4 do aluno? "))
    media = (nt1+nt2+nt3+nt4)/4
    cadast.append([nomeA, [nt1, nt2, nt3, nt4], media])
    cont = str(input("Deseja prosseguir? S/N "))
    if cont in "Nn":
        break
print("Média(s) do(s) aluno(s)")    
for i, a in enumerate(cadast):
    print(f"Aluno: {a[0]} Média: {a[2]}")    