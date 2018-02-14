
from socket import *

if __name__ == '__main__':
    target = input('Enter host to scan: ')
    targetIP = gethostbyname(target)
    print ('Starting scan on host ', targetIP)

    #scan reserved ports
    while True:
        for i in (80, 110):
            s = socket(AF_INET, SOCK_STREAM)

            result = s.connect_ex((targetIP, i))

            if(result == 0) :
                print ('Port %d: OPEN' % (i,))
            s.close()