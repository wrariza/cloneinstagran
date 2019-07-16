# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime


def say_time(request):
    return HttpResponse('Oh, hi!: current server time is, {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H-%M hrs'))
    )


def say_hi(request):
    return HttpResponse('hello-world ...')


def sorted_number(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)

    return HttpResponse(JsonResponse({
        'message': 'number order',
        'status': 'OK',
        'numbers': sorted_ints
    }))

