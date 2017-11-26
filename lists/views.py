from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect


from django.http import HttpResponse

from .models import Item, List
from .forms import ItemForm




def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})



def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        item = Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})

    
    # try:
    #     item.full_clean()
    #     item.save()
    # except ValidationError:
    #     list_.delete()
    #     error = "You can't have an empty list item"
    #     return render(request, 'home.html', {"error": error})
    # # return redirect('view_list', list_.id)
    # return redirect(list_)



# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     return redirect(f'/lists/{list_.id}/')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form':form})






