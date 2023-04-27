import os
ver = "py --list"
status = os.system(ver)

lista = [1,2,3,4,5]
for i in lista:
    print(i)
    
print(f'Termino de correr ListVer.py return = {status}')
