from django.shortcuts import render, redirect

from petstagram.common.forms import PhotoCommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from petstagram.photos.models import Photo


def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # TODO: fix this when auth

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.photolike_set.all()
    comments = photo.photocomment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': PhotoCommentForm(),
    }
    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    pk = None
    if request.method == 'GET':
        form = PhotoEditForm()
    else:
        form = PhotoEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # TODO: fix this when auth

    context = {
        'form': form,
        'photo': photo,
        'pk': pk,
    }
    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    # photo.delete()
    # return redirect('index')
    if request.method == 'GET':
        form = PhotoDeleteForm()
    else:
        form = PhotoDeleteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # TODO: fix this when auth

    context = {
        'form': form,
        'photo': photo,
        'pk': pk,
    }
    return render(request, 'photos/photo-delete-page.html', context)
