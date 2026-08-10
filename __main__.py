from diario import Diario
from rich import print, inspect

def main():
    d = Diario()
    d.escrever('matheus')
    d.escrever('anna')
    d.escrever('eu gosto de pizza')

    d.ler('tapo')
    
    d.trocar_senha('tapo', 'anna')
    inspect(d, private=True, methods=True)

if __name__ == '__main__':
    main()