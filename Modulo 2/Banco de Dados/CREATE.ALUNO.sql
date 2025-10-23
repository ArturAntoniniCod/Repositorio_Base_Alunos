CREATE TABLE aluno(
id INTEGER   PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
data_de_nascimento date NOT NULL,
telefone INTEGER NOT NULL,
email TEXT NOT NULL,
itinerario TEXT NOT NULL
)