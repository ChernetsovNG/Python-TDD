from django.http import HttpResponse


def home_page(request):
    '''домашная страница'''
    return HttpResponse('<html><title>To-Do lists</title></html>')
