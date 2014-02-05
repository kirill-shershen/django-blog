from django.core.management.base import BaseCommand, CommandError
from rates.crawler import RateParser
import datetime

class Command(BaseCommand):
    args = ''
    help = 'parse bank sites'

    def handle(self, *args, **options):
        self.stdout.write('start crawler')
        try:
            cr = RateParser(datetime.datetime.now())
            cr.do_parse()
        except Exception, e:
            CommandError('parse error: %s' % e)
            raise e
        self.stdout.write('parsing done')
