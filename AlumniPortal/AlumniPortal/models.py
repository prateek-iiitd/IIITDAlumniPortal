__author__ = 'Prateek'

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
DEGREE_TYPE_CHOICES = (('UG', 'Undergraduate'), ('PG', 'Postgraduate'), ('PhD', 'Doctoral'), ('Other', 'Other'))
WORK_TYPE_CHOICES = (
    ('Tech', 'Technical Profile'), ('Non-Tech', 'Non-Technical Profile'), ('Research', 'Research Profile'),
    ('Faculty', 'Teaching/Faculty'), ('Other', 'Other'))
MARITAL_STATUS_CHOICES = (('S', 'Single'), ('M', 'Married'))


def news_large_image(self, filename):
    return '/'.join(['news', 'full', filename])


def news_thumb_image(self, filename):
    return '/'.join(['news', 'thumb', filename])


def profile_picture(self, filename):
    return '/'.join(['profile', self.user.user.email])


class SpecialisationStream(models.Model):
    name = models.CharField(max_length=40, db_index=True)

    def __unicode__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=40, db_index=True)

    def __unicode__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=40, db_index=True)
    specialisation = models.ForeignKey(SpecialisationStream, null=True, blank=True)
    branch = models.ForeignKey(Branch)

    def __unicode__(self):
        if self.specialisation:
            return self.name + " - " + self.branch.name + " - " + self.specialisation.name
        else:
            return self.name + " - " + self.branch.name + " - "


class Student(models.Model):
    name = models.CharField(max_length=40, db_index=True)
    iiitd_email = models.EmailField(db_index=True)
    personal_email = models.EmailField(blank=True, null=True)
    graduation_year = models.PositiveSmallIntegerField(db_index=True)
    contact_number = models.BigIntegerField(null=True, blank=True)
    degree = models.ForeignKey(Degree, db_index=True)

    def __unicode__(self):
        return self.name + ": " + self.degree.__unicode__() + "(" + str(self.graduation_year) + ")"


class ContactPerson(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    contact_number = models.BigIntegerField()

    def __unicode__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=500, db_index=True)
    description = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=100)
    starts_at = models.DateTimeField(db_index=True, verbose_name="Date & Time")
    # starts_at=forms.DateTimeField(widget=forms.DateTimeField('%Y-%m-%dT%H:%M'),
    # input_formats =('%Y-%m-%dT%H:%M',))
    external_link = models.CharField(blank=True, null=True, max_length=100)

    def __unicode__(self):
        return self.title + " on " + str(self.starts_at) + " at " + self.venue


class NewsArticle(models.Model):
    headline = models.CharField(max_length=200, db_index=True)
    article = models.TextField()
    occurred_on = models.DateField(db_index=True)
    large_img = models.ImageField(blank=True, null=True, upload_to=news_large_image)
    thumbnail = models.ImageField(blank=True, null=True, upload_to=news_thumb_image)
    reporter = models.CharField(max_length=40, db_index=True, blank=True)
    gallery_link = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.headline + " - " + str(self.occurred_on)


class Award(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class ConvocationAward(models.Model):
    award = models.ForeignKey(Award)
    recipient = models.ForeignKey(Student)

    def __unicode__(self):
        return self.award.name + " awarded to " + self.recipient.name


class Coordinator(models.Model):
    student = models.ForeignKey(Student)

    def __unicode__(self):
        return self.student.name + " - " + str(self.student.graduation_year)


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    text_feedback = models.TextField()

    def __unicode__(self):
        return self.name + " - " + self.email


class Organisation(models.Model):
    name = models.CharField(max_length=100)
    linkedin_id = models.PositiveIntegerField(unique=True)

    def __unicode__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100)
    linkedin_id = models.PositiveIntegerField(unique=True)

    def __unicode__(self):
        return self.name


class DegreeType(models.Model):
    name = models.CharField(max_length=50, choices=DEGREE_TYPE_CHOICES)
    # if name is 'Other'
    desc = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        if not self.desc:
            return self.name
        else:
            return self.name + " - " + self.desc


class WorkType(models.Model):
    name = models.CharField(max_length=50, choices=WORK_TYPE_CHOICES)
    # if name is 'Other'
    desc = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        if not self.desc:
            return self.name
        else:
            return self.name + " - " + self.desc


class WorkDetail(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    work_type = models.ForeignKey(WorkType)
    organisation = models.ForeignKey(Organisation)

    def __unicode__(self):
        return self.title + " @ " + str(self.organisation.name)


class EducationDetail(models.Model):
    degree_name = models.CharField(max_length=100)
    degree_type = models.ForeignKey(DegreeType)
    field_of_study = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    school = models.ForeignKey(School)

    def __unicode__(self):
        return self.degree_name + " @ " + str(self.school.name)


class AlumniUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class AlumniUser(AbstractBaseUser):

    class Meta:
      swappable = 'AUTH_USER_MODEL'


    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    email = models.CharField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    personal_email = models.EmailField(blank=True, null=True)
    linkedin_profile = models.CharField(max_length=100, blank=True)
    facebook_profile = models.CharField(max_length=100, blank=True)
    google_profile = models.CharField(max_length=100, blank=True)
    twitter_profile = models.CharField(max_length=100, blank=True)
    homepage = models.CharField(max_length=100, blank=True)
    marital_status = models.CharField(max_length=100, blank=True, choices=MARITAL_STATUS_CHOICES)
    profile_photo = models.ImageField(upload_to=profile_picture, blank=True)
    graduation_year = models.PositiveSmallIntegerField(null=True, blank=True, db_index=True)

    education = models.ManyToManyField(EducationDetail, null=True, blank=True)
    work_experience = models.ManyToManyField(WorkDetail, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AlumniUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin