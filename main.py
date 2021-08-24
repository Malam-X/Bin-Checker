# MODULES
import requests
from os import system as SYSS
from sys import exit as EXT

"""main checker"""
class main(object):

    """untuk mengecheck bin ada atau tidak"""
    @classmethod
    def check(cls, bins):
        if bins == '':
            EXT('[!] Bin not found!')
        else:
            cls.main(bins)

    """requests data json"""
    @classmethod
    def main(cls, x):
        x = {
            'author': 'DR4G0N5',
            'url': 'https://bin-check-dr4g.herokuapp.com/api/'+x,
            'version': '0.1.1'
        }
        req = requests.get(x['url'])
        requests_json = req.json()

        """untuk check binnya valid / tidak"""
        if requests_json['result'] == 'false':
            EXT('[!] Bin Error.')
        else:
            r = requests_json['data']
            cls.main_check(r, x)

    """pengeluaran data"""
    @classmethod
    def main_check(cls, r, xx):
        full_data = r

        """datanya"""
        data = {
            'Bin': full_data['bin'],
            'Vendor': full_data['vendor'],
            'Type': full_data['type'],
            'Level': full_data['level'],
            'Bank': full_data['bank'],
            'Country': full_data['country']
        }
        print("""
 [+] Author: {}
 [+] Version: {}""".format(xx['author'],xx['version']))
        print("""
 [+] Bin: {}
 [+] vendor: {}
 [+] Type: {}
 [+] Level: {}
 [+] Bank: {}
 [+] Country: {}""".format(data['Bin'],
 data['Vendor'],
 data['Type'],
 data['Level'],
 data['Bank'],
 data['Country']))

if __name__ == '__main__':

    """pemanggil bin"""
    BINS = input('[+] Bin: ')
    main.check(BINS)
