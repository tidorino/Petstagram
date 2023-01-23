from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import PhotoCommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from petstagram.photos.models import Photo


@login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()

            return redirect('photo details', pk=photo.pk)

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.photolike_set.all()
    comments = photo.photocomment_set.all()
    user_like_photos = Photo.objects.filter(pk=pk, user_id=request.user.pk)

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': PhotoCommentForm(),
        'user_like_photos': user_like_photos,
        'is_owner': photo.user == request.user,
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
