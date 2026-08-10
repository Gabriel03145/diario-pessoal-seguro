from rich import print

class Diario:
    def __init__(self, senha = 'tapo'):
        self.__segredos = [
            'gunter',
            'anna'
            ]
        self.__senha = senha

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, codigo):
        if codigo != self.__senha:
            raise PermissionError (f'[red]senha {codigo} é invalido[/]')
        else:
            print(self.__segredos)

    def trocar_senha(self, senha_atual, nova_senha):
        if senha_atual != self.__senha:
            raise PermissionError('senha inválida para a troca de senha. Digite a senha atual.')
        if not nova_senha:
            raise ValueError('a nova senha não pode ser vazia')
        if self.__senha == nova_senha:
            raise ValueError('a nova senha não pode ser a mesma que a antiga')
        self.__senha = nova_senha
        print(f'nova senha trocada com sucesso')