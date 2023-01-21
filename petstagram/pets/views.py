from django.shortcuts import render, redirect

from petstagram.common.forms import PhotoCommentForm
from petstagram.core.photo_likes import apply_likes_count, apply_user_liked_photo
from petstagram.pets.forms import PetForm, PetEditForm
from petstagram.pets.models import Pet


def pet_details(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()
    photos_count = pet.photo_set.count()
    photos = [apply_likes_count(photo) for photo in pet.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'pet': pet,
        'photos_count': photos_count,
        'pet_photos': photos,
        'comment_form': PhotoCommentForm(),
    }
    return render(request, 'pets/pet-details-page.html', context=context)


def add_pet(request):
    if request.method == 'GET':
        form = PetForm()
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)  # TODO: fix this when auth

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def edit_pet(request, username, pet_slug):
    # TODO: use `username` when auth
    pet = Pet.objects.filter(slug=pet_slug).get()

    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug).get()

    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, 'pets/pet-delete-page.html', context)
