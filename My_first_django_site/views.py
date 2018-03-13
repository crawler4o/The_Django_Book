from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render

import datetime



def hello(request):
    return HttpResponse('Hello World!')


def time_one(request):
    return HttpResponse('The current time is %s' % datetime.datetime.now().time())


def time_one_plus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    t_now = datetime.datetime.now()
    fin_time = t_now + datetime.timedelta(hours = offset)
    ret_resp = 'Now is %s and in %s hours will be %s' %(t_now.time(), offset, fin_time.time())

    return HttpResponse(ret_resp)


def time_two(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render({'current_date':now})

    return HttpResponse(html)


def time_three(request):
    now = datetime.datetime.now()

    return render(request, 'current_datetime.html', {'current_date':now})


def time_two_plus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
            raise Http404()

    now = datetime.datetime.now()
    future = now + datetime.timedelta(hours = offset)

    return render(request, 'hours_ahead.html', {'now':now, 'future':future, 'offset':offset})


def request_meta(request):
    try:
        values = request.META
        html = []
        for x in sorted(values):
            html.append('<tr><td>%s</td><td>%s</td></tr>' % (x, values[x]))

        return HttpResponse('<table>%s</table>' % '\n'.join(html))
    except:
        return HttpResponse('Sorry, no meta data is available.')
