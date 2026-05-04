def receber_salario():
    try:
        salario = float(input('digite seu salario:'))
        return salario
    except:
        print('erro digite apenas valores numericos')

def par_ou_impar():
    try:
        idade = int(input('digite sua idade:'))
        if idade % 2 == 0:
            print(f'idade {idade} par')
        else:
            print(f'idade {idade} impar')
    except:
        print('erro digite apenas valores numericos')
        
        
def positivo_ou_negativo(salario):
    if salario < 0 :
        print('salario negativo')
    else:
        print('salario positivo')
        
def cadastrar_funcionario():
    funcionarios = {}
    while True:
        opc = input('quer continuar s/n:')
        if opc == 'n':
            break
        elif opc != 's':
            print('selecione uma opçao valida')
            continue
        nome = input('digite seu nome:')
        if not nome.replace(' ','').isalpha():
            print('nao pode digitar valores numericos ou espaços mas pode usar nomes compostos')
            continue
        par_ou_impar()
        valor_salario = receber_salario()
        if valor_salario < 0 :
            print('proibido cadastrar salarios negativos')
            continue
        funcionarios.update({nome:valor_salario})
    return funcionarios
            
        
try:
    cadastrados = cadastrar_funcionario()
    print(f'{cadastrados}')
    print(f'valor maximo salarial R${max(cadastrados.values())}')
    print(f'valor mínimo salarial R${min(cadastrados.values())}')
    print(f'media salarial R${sum(cadastrados.values())/len(cadastrados.values())}')
except:
    print('nenhum valor digitado')



