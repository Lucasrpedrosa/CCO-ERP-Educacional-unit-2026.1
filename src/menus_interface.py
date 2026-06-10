
def menu_principal():
        print('=============================================================')
        print('                     [ERP EDUCACIONAL]  ')
        print('=============================================================')
        print('[1] ALOCAÇÃO DE PROFESSOR/TURMAS')
        print('[2] DIÁRIO DE CLASSE')
        print('[0] Encerrar\n')
        print('=============================================================')
        
        
def menu_opcao():
    while True:
        try:
            menu_principal()
            menu = int(input('Escolha uma das opções: ').strip())
            if menu < 0 or menu > 2:
                 print('[ERRO] Informe um número entre as opção a seguir')
                 continue
            return menu
        except ValueError:
                print("[ERRO] Digite apenas números!")
                continue
def verifica_notas(nome_avaliacao):
    while True:
        try:
            valor = float(input(f"Digite a nota da {nome_avaliacao} (0 a 10): "))
            if valor >= 0 and valor <= 10:
                return valor
            print("@@@ A nota deve estar entre 0 e 10. @@@")
        except ValueError:
            print("@@@ Valor invalido! Digite um numero. @@@")


class Menu:

    def exibir_principal(self):
        print("\n=============================")
        print("       ERP EDUCACIONAL")
        print("=============================")
        print("[1] Cadastrar Professor")
        print("[2] Cadastrar Aluno")
        print("[3] Alocar Aula")
        print("[4] Lançar Notas")
        print("[5] Gerar Relatório")
        print("[0] Encerrar Programa")
        while True:
            opicao = input("=> ").strip()
            if opicao in ["0","1","2","3","4","5"]:
                return opicao
            print("[ERRO] Opção inválida!")

    def coletar_dados_professor(self):
        nome  = input("Nome do professor: ").strip()
        cpf   = input("CPF: ").strip()
        while True:
            try:
                carga = int(input("Carga horaria maxima (h): "))
                if 1 <= carga <= 40:
                    return nome, cpf, carga
                print("[ERRO] Entre 1 e 40h")
            except ValueError:
                print("[ERRO] Digite penas números!")

    def coletar_dados_aluno(self):
        nome      = input("Nome do aluno: ").strip()
        matricula = input("Matricula: ").strip()
        return nome, matricula

    def coletar_nota(self, nome):
        while True:
            try:
                v = float(input(f"  {nome} (0-10): "))
                if 0 <= v <= 10:
                    return v
                print("[ERRO] Nota fora do intervalo!")
            except ValueError:
                print("[ERRO] Digite um número!")

    def fluxo_alocacao(self, motor):
        print("\n--- Alocar Aula ---")
        nome_prof  = input("Nome do professor: ").strip()
        cod_turma  = input("Código da turma  : ").strip()
        cod_disc   = input("Código da disciplina: ").strip()
        slot       = input("Slot (ex: SEG_MANHA): ").strip().upper()
        horas      = int(input("Horas da disciplina: "))
        sucesso, mensagem = motor.alocar(nome_prof, cod_turma, cod_disc, slot, horas)
        print(f"{'===' if sucesso else '[ERRO]'} {mensagem} {'===' if sucesso else '[ERRO]'}")

    def fluxo_notas(self, diario):
        print("\n--- Lançar Notas ---")
        matricula = input("Matrícula do aluno: ").strip()
        disciplina = input("Disciplina: ").strip()
        av1 = self.coletar_nota("AV1")
        av2 = self.coletar_nota("AV2")
        av3 = self.coletar_nota("AV3")
        sucesso, mensagem = diario.lancar_notas(matricula, disciplina, av1, av2, av3)
        print(f"{'===' if sucesso else '[ERRO]'} {mensagem} {'===' if sucesso else '[ERROR]'}")



     



  
