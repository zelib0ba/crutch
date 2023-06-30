# Alexey Surin | https://surin.ru | a@surin.ru | t.me/zelib0ba | +7(903) 153-51-56
# удаление пустых папок на диске
import os
def del_empty_dirs(path):
    
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)
                print (f'папка {a} удалена')

del_empty_dirs("p:\\")
