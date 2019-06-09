from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    '''домашная страница'''
    return render(request, 'home.html')


def new_list(request):
    '''новый список'''
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/one-unique-list-in-the-world/')


def view_list(request):
    '''представление списка'''
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
