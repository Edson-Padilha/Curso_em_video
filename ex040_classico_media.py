print('\033[1;34m-=\033[m'*20)
print(' '*12,'\033[4;34m Média Notas \033[m')
n1 = float(input('\033[1;34m Primeira nota: \033[m'))
n2 = float(input('\033[1;34m Segunda nota: \033[m'))
n3 = float(input('\033[1;34m Terceia nota: \033[m'))
media = (n1 + n2 + n3) / 3
print('\033[1;34mTirando a nota {:.1f}, {:.1f} e {:.1f} a média do aluno é: {:.1f}\033[m'.format(n1, n2, n3, media))
if media >= 7:
    print('\033[4;34mAluno está APROVADO!\033[m')
elif media >= 5:
    print('\033[4;34mAluno em RECUPERAÇÃO\033[m')
elif media >= 0:
    print('\033[4;34mAluno REPROVADO\033[m')
