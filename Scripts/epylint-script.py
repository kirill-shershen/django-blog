#!G:\work\py\django-blog\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pylint==1.0.0','console_scripts','epylint'
__requires__ = 'pylint==1.0.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pylint==1.0.0', 'console_scripts', 'epylint')()
    )
