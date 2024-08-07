from django.shortcuts import render, get_object_or_404, redirect

from dolist.forms import StoreForm
from dolist.models import Store, Category


def home(request):
    stores = Store.objects.all()
    if 'search' in request.GET:
        query = request.GET['search']
        stores = stores.filter(name__icontains=query)
    return render(request, 'dolist/home.html', {'stores': stores})

def store_detail(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    categories = store.categories.all()
    return render(request, 'dolist/store_detail.html', {'store': store, 'categories': categories})

def category_detail(request, store_id, category_id):
    category = get_object_or_404(Category, pk=category_id, store_id=store_id)
    products = category.products.all()
    return render(request, 'dolist/category_detail.html', {'category': category, 'products': products})

def add_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StoreForm()
    return render(request, 'dolist/add_store.html', {'form': form})

def edit_store(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store_detail', store_id=store.id)
    else:
        form = StoreForm(instance=store)
    return render(request, 'dolist/edit_store.html', {'form': form, 'store': store})

def delete_store(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    if request.method == 'POST':
        store.delete()
        return redirect('home')
    return render(request, 'dolist/confirm_delete_store.html', {'store': store})
