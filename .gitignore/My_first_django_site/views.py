from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse('Hello World!')


def time_cur(request):
    return HttpResponse('The current time is %s' % datetime.datetime.now().time())

def time_add(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    t_now = datetime.datetime.now()
    fin_time = t_now + datetime.timedelta(hours = offset)
    ret_resp = 'Now is %s and in %s hours will be %s' %(t_now.time(), offset, fin_time.time())
    
    return HttpResponse(ret_resp)
