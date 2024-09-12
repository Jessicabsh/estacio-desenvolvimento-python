from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        idade = int(request.form['idade'])
        local_nascimento = request.form['local_nascimento']
        estado_civil = request.form['estado_civil']
        nome_pai = request.form['nome_pai']
        nome_mae = request.form['nome_mae']
        qtd_filhos = int(request.form['qtd_filhos'])
        renda_pessoal = float(request.form['renda_pessoal'])
        renda_familiar = float(request.form['renda_familiar'])
        doencas = request.form['doencas']
        medicamentos = request.form['medicamentos']

        conn = sqlite3.connect('cadastro.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pessoas (nome, sobrenome, idade, local_nascimento, estado_civil, nome_pai, nome_mae, qtd_filhos, renda_pessoal, renda_familiar, doencas, medicamentos)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, sobrenome, idade, local_nascimento, estado_civil, nome_pai, nome_mae, qtd_filhos, renda_pessoal, renda_familiar, doencas, medicamentos))
        conn.commit()
        conn.close()

        return redirect('/consulta')

    return render_template('cadastro.html')

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        nome = request.form['nome']
        cursor.execute('SELECT * FROM pessoas WHERE nome = ?', (nome,))
    else:
        cursor.execute('SELECT * FROM pessoas')
    pessoas = cursor.fetchall()
    conn.close()
    return render_template('consulta.html', pessoas=pessoas)

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
