import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('\nVerificando o ip: ', ip)
        print('*' * 60)
        os.system('ping -c 3 ' + ip)
        print('*' * 60)
        time.sleep(5)
