from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import Userform
from .models import Users
from profileapp.models import Profile,Profileskills,ProfileEducation,ProfileCertification,ProfileExperience

# Create your views here.

def Homepage(request):
    profile = Profile.objects.all()
    return  render(request,'users/landingpage.html',{'profile':profile})

def registeruser(request):

    if request.method == 'POST':
        form = Userform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registeruser')
    else:
        form = Userform()
        return render(request,'users/register.html',{'form':form})



def userlogin(request):
    #users = Users()

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = Users.objects.filter(email=email,password=password).exists()

        if user is not None:
            user_details = Users.objects.get(email=email, password=password)
            name = user_details.name
            usertype = user_details.usertype
            userid = user_details.id
            if usertype == 'user':
                    request.session['username'] = name
                    request.session['usertype'] = usertype
                    request.session['userid'] = userid
                    return redirect('userpanel')
            elif usertype == 'admin':
                    request.session['username'] = name
                    request.session['usertype'] = usertype
                    return redirect('adminpanel')
            else:
                messages.error(request, "invalid username/password")
        else:
            messages.error(request, "Invalid Role:")

    return render(request, 'users/login.html')

def userpanel(request):
    return render(request,'users/userpanel.html')

def adminpanel(request):
    profilecount = Profile.objects.count()
    return render(request,'admin/adminpanel.html',{'profile':profilecount});

def logoutuser(request):
    logout(request)
    return redirect('userlogin')



#admin fn

def profilelist(request):
    profile = Profile.objects.all()
    return render(request,'admin/profile/profilelist.html',{'profile':profile})


def profiledetails(request,profile_id):
    profile = Profile.objects.get(id=profile_id)
    skills = Profileskills.objects.filter(profile_id=profile_id)
    educations = ProfileEducation.objects.filter(profile_id=profile_id)
    certifications = ProfileCertification.objects.filter(profile_id=profile_id)
    experience = ProfileExperience.objects.filter(profile_id=profile_id)

    context = {
        'profile': profile,
        'skills': skills,
        'education':educations,
        'experience': experience,
        'certification':certifications

        }
    return render(request,'admin/profile/profiledetails.html',context)

def deleteprofile(request,profile_id):

    profile = Profile.objects.get(id=profile_id)
    users_id = profile.users_id
    users = Users.objects.get(id=users_id)

    certifications = ProfileCertification.objects.filter(profile_id=profile_id)
    certifications.delete()

    educations = ProfileEducation.objects.filter(profile_id=profile_id)
    educations.delete()

    skills = Profileskills.objects.filter(profile_id=profile_id)
    skills.delete()

    profile.delete()
    users.delete()

    messages.info(request, "Profile Successfully Deleted")
    return redirect('profilelist')


