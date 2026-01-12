from repositorios import (
    cadastrar_projeto, 
    cadastrar_aluno, 
    cadastrar_participacao,  
    listar_projetos, 
    listar_alunos, 
    buscar_participacao_aluno, 
    buscar_participacao_projeto, 
    preencher_dados
)

def menu():
    alunos, projetos, participacoes = preencher_dados()

    while True: 
        print("\n=== Menu Principal ===")
        print("1. Cadastrar Projeto")
        print("2. Cadastrar Aluno")
        print("3. Registrar Participação") 
        print("4. Listar Projetos")
        print("5. Listar Alunos")
        print("6. Listar Participacoes de um aluno")
        print("7. Listar Participacoes em um projeto")
        print("0. Sair")

        escolha = input("Escolha uma opcao: ")

        match escolha:
            case "1":
                print(">> Opcao 1: Cadastrar Projeto")
                if cadastrar_projeto(projetos):
                    print("Projeto cadastrado com sucesso!")

            case "2":
                print(">> Opcao 2: Cadastrar Aluno")   
                if cadastrar_aluno(alunos):
                    print("Aluno cadastrado com sucesso!")

            case "3":
                print(">> Opcao 3: Registrar Participação")
                if cadastrar_participacao(participacoes, alunos, projetos):
                    print("Participação registrada com sucesso!")

            case "4":
                print(">> Opcao 4: Listar Projetos")
                listar_projetos(projetos) 
                
            case "5":
                print(">> Opcao 5: Listar Alunos")
                listar_alunos(alunos)
                
            case "6":
                print(">> Opcao 6: Buscar por Aluno")
                input_prontuario = input("Digite o prontuario do aluno: ")
                if not buscar_participacao_aluno(participacoes, input_prontuario):
                    print("Nenhuma participação encontrada para este aluno.")

            case "7":
                print(">> Opcao 7: Buscar por Projeto")
                input_codigo = input("Digite o codigo do projeto: ")
                if not buscar_participacao_projeto(participacoes, input_codigo):
                    print("Nenhuma participação encontrada neste projeto.")
        
            case "0":
                print("Saindo do programa...")
                return 0 
            
            case _:
                print("Opcao invalida. Tente novamente.")