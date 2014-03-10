from rates.crawler import RateParser
import datetime

def main():
    print 'start crawler'
    cr = RateParser(datetime.datetime.now())
    cr.do_parse()
    print 'done'
    
if __name__ == '__main__':
    main()