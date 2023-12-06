import os

from django.shortcuts import render,redirect
from .models import Profile
from django.db.models import Q
# Create your views here.


def Home(request):
   all_profile = Profile.objects.all().first()
   if request.method=='GET':
      src= request.GET.get('search')
      if src:
        all_profile = Profile.objects.filter(Q(name__icontains=src) | Q(email__icontains= src))

      else:
          all_profile = Profile.objects.all()

   context = {
       'all_prof': all_profile
   }
   return render(request, 'home.html', context)
def Create(request):

    if request.method == 'POST':
        name= request.POST ['name']
        email = request.POST['email']
        image = request.FILES.get('image')
        address = request.POST['address']
        number= request.POST['number']
        age = request.POST['age']
        gender = request.POST['gender']
        religion= request.POST['religion']
        division = request.POST['division']
        color = request.POST['color']

        if image:
            prof=Profile (name=name, email=email, image=image, address=address, number=number,age=age, gender=gender,religion=religion, division=division, color=color)
            prof.save()
            return redirect('home')
        else:
            prof = Profile (name=name, email=email,address=address, number=number, age=age, gender=gender,
                           religion=religion, division=division, color=color)
            prof.save()
        return redirect('home')

    return render(request,'create.html')
def delete(request, id):
    delete_prof = Profile.objects.get(id=id)
    if delete_prof:
        if delete_prof.image != 'def.png':
             os.remove(delete_prof.image.path)
        delete_prof.delete()
    return redirect('home')



def update(request, id):
    prof = Profile.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        image = request.FILES.get('image')
        address = request.POST['address']
        number = request.POST['number']
        age = request.POST['age']
        gender = request.POST['gender']
        religion = request.POST['religion']
        division = request.POST['division']
        color = request.POST['color']

        if image:
            if prof.image != 'def.png':
                os.remove(prof.image.path)

            prof.name = name
            prof.email = email
            prof.image = image
            prof.address = address
            prof.number = number
            prof.age = age
            prof.gender = gender
            prof.religion = religion
            prof.division = division
            prof.color = color
            # prof = Profile(name=name, email=email, image=image, address=address, number=number, age=age, gender=gender, religion=religion, division=division, color=color)
            prof.save()
            return redirect('home')
        else:
            prof.name = name
            prof.email = email
            prof.address = address
            prof.number = number
            prof.age = age
            prof.gender = gender
            prof.religion = religion
            prof.division = division
            prof.color = color
            # prof = Profile(name=name, email=email, address=address, number=number, age=age, gender=gender, religion=religion, division=division, color=color)
            prof.save()
            # print('Your Profile is Updated', prof.name)
            # prof_obj.save()
            return redirect('home')

    return render(request, 'update.html', locals())

    # return render(request, 'update.html', locals())











