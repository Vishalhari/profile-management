from django.db import models
from usersapp.models import Users

# Create your models here.

class Profile(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    profilepic = models.ImageField(null=True, upload_to="profile_media/")
    users = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    phoneno = models.CharField(max_length=200)
    address = models.TextField()
    skills = models.ManyToManyField('Profileskills', related_name='Profile')
    education = models.ManyToManyField('ProfileEducation', related_name='education')
    experience = models.ManyToManyField('ProfileExperience',related_name='experience')
    certificate = models.ManyToManyField('ProfileCertification', related_name='certification')

    def __str__(self):
        return '{}'.format(self.firstname)


class Profileskills(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    skillname = models.TextField()

    def __str__(self):
        return '{}'.format(self.skillname)


class ProfileEducation(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    year = models.IntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return '{}'.format(self.course)


class ProfileCertification(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    certificate = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    instituteyear = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.certificate)


class ProfileExperience(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    companyname = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    joinedyear = models.CharField(max_length=200)
    resignedyear = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.companyname)
