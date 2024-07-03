from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile,Profileskills,ProfileEducation,ProfileCertification,ProfileExperience
from usersapp.models import Users

# Create your views here.


def createprofile(request):
    form = ProfileForm()

    user_id = request.session.get('userid')
    user_details = Users.objects.get(id=user_id)

    if request.method == 'POST':
        profilexist = Profile.objects.filter(users=user_details).exists()
        if profilexist:
            profile = get_object_or_404(Profile, users=user_details)
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.save()

                profileid = profile.id

                skill_names = request.POST.getlist('skill')
                courses = request.POST.getlist('course')
                academic_years = request.POST.getlist('academicyear')
                percentages = request.POST.getlist('percentage')
                certificatename = request.POST.getlist('cerificatename')
                institutename = request.POST.getlist('institutename')
                completedyear = request.POST.getlist('completedyear')
                company = request.POST.getlist('company')
                location = request.POST.getlist('location')
                startyear = request.POST.getlist('startyear')
                endyear = request.POST.getlist('endyear')

                # return HttpResponse(certificatename)



                Profileskills.objects.filter(profile_id=profileid).delete()
                for skill_name in skill_names:
                    skill_obj, created = Profileskills.objects.get_or_create(skillname=skill_name, profile=profile)
                    profile.skills.add(skill_obj)

                ProfileEducation.objects.filter(profile_id=profileid).delete()
                for course, academic_year, percentage in zip(courses, academic_years, percentages):
                    education_obj,created = ProfileEducation.objects.get_or_create(course=course,year=academic_year,percentage=percentage,profile=profile)
                    profile.education.add(education_obj)

                ProfileExperience.objects.filter(profile_id=profileid).delete()
                for comp, location, styear, endyear in zip(company, location, startyear, endyear):
                    experience_obj, created = ProfileExperience.objects.get_or_create(companyname=comp,location=location,joinedyear=styear,resignedyear=endyear,profile=profile)
                    profile.experience.add(experience_obj)

                ProfileCertification.objects.filter(profile_id=profileid).delete()
                for certificate, institute, year in zip(certificatename, institutename, completedyear):
                    certificate_obj = ProfileCertification(
                        certificate=certificate,
                        institute=institute,
                        instituteyear=year,
                        profile=profile
                    )
                    certificate_obj.save()
                    profile.certificate.add(certificate_obj)


                messages.info(request, "Profile Updated Successfully")
                return redirect('createprofile')
        else:
            profile = ProfileForm(request.POST, request.FILES)
            if profile.is_valid():
                profileobj = profile.save(commit=False)
                profileobj.users_id = user_id
                profileobj.save()

                skill_names = request.POST.getlist('skill')

                courses = request.POST.getlist('course')
                academic_years = request.POST.getlist('academicyear')
                percentages = request.POST.getlist('percentage')

                certificatename = request.POST.getlist('cerificatename')
                institutename = request.POST.getlist('institutename')
                completedyear = request.POST.getlist('completedyear')

                company = request.POST.getlist('company')
                location = request.POST.getlist('location')
                startyear = request.POST.getlist('startyear')
                endyear = request.POST.getlist('endyear')

                for skill_name in skill_names:
                    skill_obj, created = Profileskills.objects.get_or_create(skillname=skill_name,profile=profileobj)
                    profileobj.skills.add(skill_obj)

                for course, academic_year, percentage in zip(courses, academic_years, percentages):
                    education_obj,created = ProfileEducation.objects.get_or_create(course=course,year=academic_year,percentage=percentage,profile=profileobj)
                    profileobj.education.add(education_obj)

                for comp,location,styear,endyear in zip(company,location,startyear,endyear):
                    experience_obj,created = ProfileExperience.objects.get_or_create(companyname=comp,location=location,joinedyear=styear,resignedyear=endyear,profile=profileobj)
                    profileobj.experience.add(experience_obj)

                for certificate, institute, year in zip(certificatename, institutename, completedyear):
                    certificate_obj,created = ProfileCertification.objects.get_or_create(certificate=certificate,institute=institute,instituteyear=year,profile=profileobj)
                    profileobj.certificate.add(certificate_obj)

            messages.info(request, "Profile Successfully Created")
            return redirect('createprofile')
    user_id = request.session.get('userid')
    user_details = Users.objects.get(id=user_id)
    profilexist = Profile.objects.filter(users=user_details).exists()
    if profilexist:
        profile = Profile.objects.get(users=user_details)
        editform = ProfileForm(instance=profile)

        profileId = profile.id

        skilllist = Profileskills.objects.filter(profile=profile)
        educationlist = ProfileEducation.objects.filter(profile=profile)
        certificatelist = ProfileCertification.objects.filter(profile=profile)
        experiencelist = ProfileExperience.objects.filter(profile=profile)

        context = {
            'form': editform,
            'profile': profile,
            'skills':skilllist,
            'education':educationlist,
            'experience':experiencelist,
            'certificate':certificatelist
        }
        return render(request, 'users/profile/updateprofile.html', context)


    return render(request,'users/profile/createprofile.html',{'form':form})




