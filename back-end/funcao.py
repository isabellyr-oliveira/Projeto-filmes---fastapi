from conexao import conector

def criar_tabela():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS filmes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INT NOT NULL,
                nota FLOAT
                )           
            """)
            conexao.commit()
        except Exception as erro:
            print("Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()
            
def cadastrar_filme(titulo, genero, ano, nota):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO filmes (titulo, genero, ano, nota) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, nota)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao cadastrar filme {erro}")
        finally:
            cursor.close()
            conexao.commit()
            
def listar_filmes():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM filmes ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os filmes {erro}")
            return[]
        finally:
            cursor.close()
            conexao.close()
listar_filmes()

