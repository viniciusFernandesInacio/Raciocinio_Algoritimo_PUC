while True:
    login = input('LOGIN: ')
    senha = input('SENHA: ')
    if (login == 'vinicius') and (senha == 'fernandes'):
        print('Bem-vindo ao sistema!')
        break
    else:
        print('[ERRO] Login ou senha incorrretos!') 
        break