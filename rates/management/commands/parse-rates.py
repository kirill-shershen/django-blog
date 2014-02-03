from django.core.management.base import BaseCommand, CommandError
from rates.crawler import RateParser

class Command(BaseCommand):
    args = ''
    help = 'parse bank sites'

    def handle(self, *args, **options):
        self.stdout.write('start crawler')
        try:
            cr = RateParser()
            cr.do_parse()
        except Exception, e:
            CommandError('parse error: %s' % e)
            raise e
        self.stdout.write('parsing done')
