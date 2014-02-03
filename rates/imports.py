import os
from rates.models import Bank
        
class ImportBank():
    def __init__(self):
        self.fn = 'banks.csv'

    def do_import(self):
        if os.path.exists(self.fn):
            try:
                csv = open(self.fn, 'r')
                for line in csv:
                    info = line.split(';')
                    # bname = unicode(line[0].decode('cp1251'))
                    # bURL = line[1]
                    print info[0]
                    print info[1]
                    print info[2]
                    bank = Bank(name = info[0].decode('cp1251'), URL = info[1], xpath = info[2])
                    if Bank.objects.filter(name=info[0].decode('cp1251')).count() == 0:
                        bank.save()
            except Exception, e:
                print e
            finally:
                csv.close()

