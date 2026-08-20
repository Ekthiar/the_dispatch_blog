from django.shortcuts import render, redirect
from . import forms


def add_category(request):
    if request.method == "POST":
        form = forms.CetagoryForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_post')
    else:
        form = forms.CetagoryForm()
    return render(request, 'cetagories/cetagories.html', {'form': form})
