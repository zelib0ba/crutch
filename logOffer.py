# Alexey Surin | https://surin.ru | a@surin.ru | t.me/zelib0ba | +7(903) 153-51-56
import os 
os.system ('query session > session.txt')

with open ('./session.txt',encoding='866') as f:
    a = f.readlines()

for i in a[3:-1]:
    out = i.split()
    if out[-1] == 'Диск':
        os.system(f'logoff {out[1]}')
        print (f'сеанс пользователя - {out[0]} завершен')

os.remove ('./session.txt')
