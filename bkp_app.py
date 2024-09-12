import sqlite3

class Pessoa:
    def __init__(self, nome, sobrenome, idade, local_nascimento, estado_civil, nome_pai, nome_mae, qtd_filhos, renda_pessoal, renda_familiar, doencas, medicamentos):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.local_nascimento = local_nascimento
        self.estado_civil = estado_civil
        self.nome_pai = nome_pai
        self.nome_mae = nome_mae
        self.qtd_filhos = qtd_filhos
        self.renda_pessoal = renda_pessoal
        self.renda_familiar = renda_familiar
        self.doencas = doencas
        self.medicamentos = medicamentos

    def __str__(self):
        return f"Nome: {self.nome} {self.sobrenome}\nIdade: {self.idade}\nLocal de Nascimento: {self.local_nascimento}\nEstado Civil: {self.estado_civil}\nNome do Pai: {self.nome_pai}\nNome da Mãe: {self.nome_mae}\nQuantidade de Filhos: {self.qtd_filhos}\nRenda Pessoal: {self.renda_pessoal}\nRenda Familiar: {self.renda_familiar}\nDoenças em Tratamento: {self.doencas}\nMedicamentos Utilizados: {self.medicamentos}"

def criar_tabela():
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sobrenome TEXT,
            idade INTEGER,
            local_nascimento TEXT,
            estado_civil TEXT,
            nome_pai TEXT,
            nome_mae TEXT,
            qtd_filhos INTEGER,
            renda_pessoal REAL,
            renda_familiar REAL,
            doencas TEXT,
            medicamentos TEXT
        )
    ''')
    conn.commit()
    conn.close()

def cadastrar_pessoa():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    idade = int(input("Idade: "))
    local_nascimento = input("Local de Nascimento: ")
    estado_civil = input("Estado Civil: ")
    nome_pai = input("Nome do Pai: ")
    nome_mae = input("Nome da Mãe: ")
    qtd_filhos = int(input("Quantidade de Filhos: "))
    renda_pessoal = float(input("Renda Pessoal: "))
    renda_familiar = float(input("Renda Familiar: "))
    doencas = input("Doenças em Tratamento: ")
    medicamentos = input("Medicamentos Utilizados: ")

    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pessoas (nome, sobrenome, idade, local_nascimento, estado_civil, nome_pai, nome_mae, qtd_filhos, renda_pessoal, renda_familiar, doencas, medicamentos)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, sobrenome, idade, local_nascimento, estado_civil, nome_pai, nome_mae, qtd_filhos, renda_pessoal, renda_familiar, doencas, medicamentos))
    conn.commit()
    conn.close()

def buscar_pessoa(nome):
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pessoas WHERE nome = ?', (nome,))
    pessoa = cursor.fetchone()
    conn.close()
    if pessoa:
        return Pessoa(*pessoa[1:])
    return None

def listar_pessoas():
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pessoas')
    pessoas = cursor.fetchall()
    conn.close()
    return [Pessoa(*pessoa[1:]) for pessoa in pessoas]

def main():
    criar_tabela()
    while True:
        print("\nMenu Principal")
        print("1. Cadastrar nova pessoa")
        print("2. Buscar pessoa cadastrada")
        print("3. Sair")
        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            nome_busca = input("Digite o nome da pessoa que deseja buscar: ")
            pessoa_encontrada = buscar_pessoa(nome_busca)
            if pessoa_encontrada:
                print("\nPessoa Encontrada:")
                print(pessoa_encontrada)
            else:
                print("Pessoa não encontrada.")
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

    pessoas = listar_pessoas()
    if pessoas:
        print("\nPessoas Cadastradas:")
        for pessoa in pessoas:
            print(pessoa)
            print("-" * 30)

if __name__ == "__main__":
    main()
