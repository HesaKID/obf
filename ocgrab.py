import requests as r
import os
import sys
from platform import system
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


if system() == 'Linux':
	os.system('clear')
if system() == 'Windows':
	os.system('cls')

def grab(url):
    if "//" not in url:
        url = "%s%s" % ('http://', url)
    url = url.strip()
    head = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}
    cek = r.get(url + '/admin/index.php', headers = head)
    if "common/login" in cek.text:
        print(url + " [OK]")
        open('ocg_result.txt', 'a').write(url + '\n')
    else:
        print(url + " [BAD]")

def main():
    listsite = open(sys.argv[1], 'r').readlines()
    for x in listsite:
        try:
            x = x.strip()
            grab(x)
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python " + sys.argv[0] + " list.txt")
    else:
        main()