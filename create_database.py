import sqlite3

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

if __name__ == "__main__":
    criar_tabela()
    print("Banco de dados criado com sucesso!")
