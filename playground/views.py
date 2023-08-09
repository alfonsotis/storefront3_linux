from django.shortcuts import render

from playground.tasks import notify_customer


def say_hello(request):

    notify_customer.delay('Hello')

    return render(request, 'hello.html', {'name': 'Super Alfonso'})
