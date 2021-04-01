from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(id='0', nome='Rafael', idade=24)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Fernando').first()
    pessoa.nome = 'Jose'
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Fernando').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    consulta_pessoas()
