import sqlalchemy as db
import pymysql
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Numeric

engine = db.create_engine("mysql+pymysql://root@localhost:3306/loja")
Base = declarative_base()

class Produtos(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60))
    preco = Column(Numeric)

Base.metadata.create_all(engine)

p1 = Produtos(nome = "sabonete", preco = 5.00)
p2 = Produtos(nome = "desodorante", preco = 10.00)
p3 = Produtos(nome = "perfume", preco = 20.00)
p4 = Produtos(nome = "shampoo", preco = 15.00)

Session = sessionmaker(bind=engine)
session = Session()

# session.add_all([p1, p2, p3, p4])
# session.commit()

print("MENU DE OPÇÕES:\n"
      "- Digite 1 para consulota\n"
      "- Digite 2 para adicionar\n"
      "- Digite 3 para deletar\n"
      "- Digite 4 para inserir\n")

opcao = int(input("Informe a opção desejada: "))


def consultar():
    produtos = session.query(Produtos).filter(Produtos.nome.like("%D%"))
    for produto in produtos:
        print(produto.nome)

def alterar():
    produtos = session.query(Produtos).filter(Produtos.id == 2).one()
    produtos.preco =17.00
    session.add(produtos)
    session.commit()

def deletar():
    produtos = session.query(Produtos).filter(Produtos.id == 4).one()
    session.delete(produtos)
    session.commit()

def inserir():
    N_produto =input('digite o nome')
    preco = int(input('digite o preço'))
    new_produto = Produtos(nome=N_produto, preco=preco)
    session.add(new_produto)
    session.commit()


if opcao == 1:
    print("Você quer consultar.")
    consultar()
elif opcao == 2:
    print("Você quer alterar.")
    alterar()
elif opcao == 3:
    print("Você quer deletar.")
    deletar()
elif opcao == 4:
    print("Você quer inserir.")
    inserir()
