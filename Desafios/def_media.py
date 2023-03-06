# Função de media dos alunos 

def calcular_media():
    soma = 0
    for i in range(1, 5):
        nota = float(input(f"Informe a nota da prova {i}: "))
        soma += nota
    media = soma / 4
    return media
media = calcular_media()

print(f"A média do aluno foi de {media:.2f}")   

if media >= 7: 
    print(f'O Aluno está aprovado')
elif media >= 5:
    print(('O Aluno está na prova final '))
else: 
    print(f'O Aluno está reprovado')  