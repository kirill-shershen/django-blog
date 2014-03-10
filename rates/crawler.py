# -*- coding: utf-8 -*-
import os, urllib2, yql, sys, time
from decimal import Decimal
from djangoproject import settings
from rates.models import Bank, BankRate
import httplib2

class RateParser():

    def __init__(self, check_date):
        self.banks = []
        self.date = check_date

    def do_parse(self):
        banks = Bank.objects.all()
        for b in banks:
            self.banks.append(b)
        while (len(self.banks)>0):
            bank = self.banks.pop()
            self.get_from_bank(bank)

    def get_from_bank(self, bank):
        
        bank_info = bank
        if bank_info.URL == 'none' or bank_info.URL == '':
            exit
        if bank_info.xpath != 'none' and bank_info.xpath != '':
            try:
                site = y = yql.Public(httplib2.Http())
                query = 'select * from html where url="%s" and xpath="%s"' % (bank_info.URL, bank_info.xpath)
                result = y.execute(query)
                if result and result.results:
                    if  bank_info.name in ['Восточный экспресс'] :
                        val = result.results.values()[0][0]
                    elif  bank_info.name in ['КУРСКПРОМБАНК', 'Нордеа Банк', 'Банк Россия', 'ВТБ 24', 'Инвестторгбанк', 'Липецккомбанк', 'ЛОКО-БАНК', 'МАСТ-Банк',
                          'Газпромбанк', 'Мой Банк', 'Московский Индустриальный Банк', 'Пробизнесбанк',
                          'Промсвязьбанк', 'Райффайзенбанк', 'РосЕвроБанк', 'ХКФ Банк',
                          'Юниаструм Банк', 'ЮниКредит Банк', 'РУСНАРБАНК']:
                        val = result.rows[0]
                    else:
                        val = result.results.values()[0]
                    if type(val) == type(dict()):
                        if bank_info.name in ['ТРАНСКАПИТАЛБАНК', 'ВТБ 24'] :
                            val = val.get('p').get('content')[:5]
                        elif bank_info.name in ['Газпромбанк', 'Инвестторгбанк', 'МАСТ-Банк', 'РосЕвроБанк']:
                            val = val.get('content').strip()[:5]
                        elif bank_info.name in ['Банк Россия']:
                            val = val.get('strong')
                        else:
                            val = val.get('p')
                    if type(val) == type([]):
                        val = val[0][:5]
                    if val:
                        try:
                            val = val.replace('-','.').replace(',','.')[:5]
                            val = Decimal(val)
                        except:
                            val = 0
                        p = BankRate(bank=bank_info, rate="USD", value=val, checktime=self.date)
                        p.save()
                        
            except Exception, err:
                print '%s: error: %s'%(bank_info.name, err)