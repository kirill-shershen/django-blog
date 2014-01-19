from django.core.management.base import BaseCommand, CommandError
from blog.models import Post
from django.contrib.sitemaps import ping_google

class Command(BaseCommand):
    args = ''
    help = 'ping google'

    def handle(self, *args, **options):
        self.stdout.write('ping google')
        try:
            ping_google()
        except Exception, e:
            CommandError('error: %s' % e)
            raise e
        self.stdout.write('done')
