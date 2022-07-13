'''
Telefone
'''
class Agenda_Poo():
  def __init__(self, nome, telefone):
    self.__nome = nome
    self.__telefone = telefone

  def getNome(self):
    return self.__nome
  
  def getTelefone(self):
    return self.__telefone


'''
controller
'''
class Controller():
  def adicionarContato(nome, telefone):
    return Agenda_Poo(nome, telefone)

  def mostrarTodosContatos(listaTelefone):
    for tel in listaTelefone:
      print('{} | {}'.format(tel.getNome(), tel.getTelefone()))

  def procurarContato(listaTelefone, nome):
    cont = 0
    for tel in listaTelefone:
      if tel.getNome() == nome:
        print('{} | {}'.format(tel.getNome(), tel.getTelefone()))
        break
      cont += 1

  def excluirTudo(listaTelefica):
    if len(listaTelefica) != 0:
      listaTelefica.clear()
      return 'Todos os contatos foram excluidos!'
    else:
      return 'A lista de contatos esta vazia!'

  def excluirContato(listaTelefone, nome):
    if len(listaTelefone) != 0:
      cont = 0
      for tel in listaTelefone:
        if tel.getNome() == nome:
          listaTelefone.pop(cont)
          return 'Contado {} removido com sucesso!'.format(nome)
        else:
          return 'Nome não encontrado!'
    else:
      return 'Lista está vazia!'


'''
main
'''
agenda = []

print('='*30)
print('AGENDA TELEFONICA')
print('='*30)

while True:

  print('')
  print('='*30)  
  print('1 - Adicionar contato')
  print('2 - Pesquisar contato')
  print('3 - Mostrar todos os contatos')
  print('4 - Excluir contato')
  print('5 - Excluir todos os contatos')
  print('6 - Sair da Agenda')
  print('='*30)

  op = int(input('Entre com a opção desejada: '))

  if op == 1:
    nome = input('Digite o nome: ')
    tel = int(input('Digite o número de telefone: '))
    agenda.append(Controller.adicionarContato(nome, tel))
  elif op == 2:
    nome = input('Digite o nome que deseja procurar: ')
    Controller.procurarContato(agenda, nome)
  elif op == 3:
    Controller.mostrarTodosContatos(agenda)
  elif op == 4:
    nome = input('Digite o nome para a pesquisa: ')
    print(Controller.excluirContato(agenda, nome))
  elif op == 5:
    print(Controller.excluirTudo(agenda))
  elif op == 6:
    break
  else:
    print('[ERRO]Digite a opção correta!')

print('Obrigado por usar a Agenda POO!!!')
print('='*30)    