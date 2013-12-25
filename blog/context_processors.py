from blog.models import Post
from calendar import month_name, monthrange
import time 
import datetime

def get_month_list(request):
    if not Post.publics.count():
        return []

    to_year, to_month = time.localtime()[:2]
    from_year = to_year - 1
    from_month = to_month
    months = []

    for y in range(to_year, from_year-1, -1):
        start, end = 12, 0
        if y == to_year: start = to_month
        if y == from_year: end = from_month-1

        for m in range(start, end, -1):
            ed = monthrange(y, m)[1]
            post_count = Post.publics.filter(created__range = (datetime.date(y,m,1),datetime.date(y,m,ed))).count()
            if post_count >= 1:
                months.append((y, m, month_name[m], post_count))

    return {'month_list': months}