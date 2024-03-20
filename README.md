# Student Grades Calculator / Calculadora de Notas de Estudantes

This repository contains a Python script to calculate the average grades of students in multiple classes. The script prompts the user to input the grades of each student for a specified number of evaluations across multiple classes, and then calculates and displays the average grade for each student.

Este repositório contém um script em Python para calcular as médias das notas dos alunos em várias turmas. O script solicita ao usuário que insira as notas de cada aluno para um número especificado de avaliações em várias turmas e, em seguida, calcula e exibe a média das notas de cada aluno.

## Usage / Uso

1. Clone the repository to your local machine / 
   Clone o repositório para sua máquina local:

   ```
   git clone https://github.com/your-username/student-grades-calculator.git
   ```

2. Run the Python script / 
   Execute o script Python:

   ```
   python main.py
   ```

3. Follow the prompts to input the grades for each student in each class.
   Siga as instruções para inserir as notas de cada aluno em cada turma.

## How it Works / Como Funciona

The Python script `grades_calculator.py` contains the following functions:

- `calcular_media_aluno(notas)`: Calculates the average grade for a student based on the given list of grades.
- `main()`: The main function of the script where the user inputs the grades for each student in each class, and then the script calculates and displays the average grade for each student.

O script Python `grades_calculator.py` contém as seguintes funções:

- `calcular_media_aluno(notas)`: Calcula a média das notas de um aluno com base na lista de notas fornecida.
- `main()`: A função principal do script onde o usuário insere as notas de cada aluno em cada turma, e então o script calcula e exibe a média das notas de cada aluno.

The script prompts the user to input grades for a specified number of evaluations for each student in each class. After inputting all the grades, it calculates and displays the average grade for each student in each class.

O script solicita ao usuário que insira notas para um número especificado de avaliações para cada aluno em cada turma. Depois de inserir todas as notas, ele calcula e exibe a média das notas de cada aluno em cada turma.

## Inputs / Entradas

- Number of classes (`NUM_TURMAS`): Specify the number of classes for which grades need to be calculated.
- Number of students per class (`NUM_ALUNOS`): Specify the number of students in each class.
- Number of evaluations (`NUM_AVALIACOES`): Specify the number of evaluations for which grades need to be inputted for each student.

- Número de turmas (`NUM_TURMAS`): Especifique o número de turmas para as quais as notas precisam ser calculadas.
- Número de alunos por turma (`NUM_ALUNOS`): Especifique o número de alunos em cada turma.
- Número de avaliações (`NUM_AVALIACOES`): Especifique o número de avaliações para as quais as notas precisam ser inseridas para cada aluno.

## Outputs / Saídas

The script outputs the average grade for each student in each class.

O script exibe a média das notas de cada aluno em cada turma.

## Contributing / Contribuindo

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request. 🎉

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, por favor, abra uma issue ou crie um pull request. 🎉

## License / Licença

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
