from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    '''домашная страница'''
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/one-unique-list-in-the-world/')
    return render(request, 'home.html')


def view_list(request):
    '''представление списка'''
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
