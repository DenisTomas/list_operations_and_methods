def calcular_media_aluno(notas):
    return sum(notas) / len(notas)

def main():
    NUM_TURMAS = 9
    NUM_ALUNOS = 24
    NUM_AVALIACOES = 5

    lista_de_turmas = []
    
    for num_turma in range(NUM_TURMAS):
        turma = []

        for num_aluno in range(NUM_ALUNOS):
            notas_aluno = []

            for num_avaliacao in range(NUM_AVALIACOES):
                nota = float(input(f"Digite a nota do aluno {num_aluno+1} da turma {num_turma+1} na avaliação {num_avaliacao+1}:"))
                notas_aluno.append(nota)
            turma.append(notas_aluno)
        lista_de_turmas.append(turma)
    
    for num_turma, turma in enumerate(lista_de_turmas):
        print(f"\nTurma {num_turma+1}:")

        for num_aluno, notas_aluno in enumerate(turma):
            media_aluno = calcular_media_aluno(notas_aluno)
            print(f"Média do aluno {num_aluno+1}: {media_aluno: .2f}")

if __name__ == "__main__":
    main()