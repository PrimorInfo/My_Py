# testando se sites estão acessíveis ou não
import  urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print('\033[31mSite Indisponível!\033[m')
else:
    print("Site online!")
    print(site.read()) # acessar site com todo o código fonte