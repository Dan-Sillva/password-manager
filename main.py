from random import randint
from time import sleep

path = '/home/widdley/Backup-2/.secret/.passwd.txt'
passwd = ''
rangee = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
          'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
          '8', '9', '!', '@', 'ç', 'Ç', '&', '#', '%', '*', '+', '?']

softName = input('Informe a qual software a senha irá pertencer: ')
login = input('Informe o login da senha: ')

print('\n{} \033[34mGERANDO SENHA ...\033[m {}'.format('<'*5,'>'*5))
sleep(1)

for i in range(18):
    passwd = passwd + rangee[randint(0, 71)]

print('\n \033[31m !!! Senha Gerada com sucesso !!!\033[m\n')
line = '[ {} ]:[ {} ]:[ {} ]\n\n'.format(softName, login, passwd)

print('      {}'.format(line))

with open(path, 'a+') as file:
    file.write(line)
    #file.read()
    #print('TEST_____')
