__author__ = 'Prateek'

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added
from datetime import date

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
    return '/'.join(['profile', self.email[:self.email.find('@')] + "_" + filename])


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


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=75, db_index=True)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.city + " in " + str(self.country.name)


class Organisation(models.Model):
    name = models.CharField(max_length=100)
    linkedin_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    location = models.ForeignKey(Location, null=True, blank=True)

    def __unicode__(self):
        return self.name + " @ " + str(self.location)


class School(models.Model):
    name = models.CharField(max_length=100)
    linkedin_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    location = models.ForeignKey(Location, null=True, blank=True)

    def __unicode__(self):
        return self.name + " @ " + str(self.location)


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
    current_location = models.ForeignKey(Location, null=True)
    # education = models.ManyToManyField(EducationDetail, null=True, blank=True)
    # work_experience = models.ManyToManyField(WorkDetail, null=True, blank=True)

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


class WorkDetail(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    work_type = models.ForeignKey(WorkType, null=True)
    organisation = models.ForeignKey(Organisation)
    user = models.ForeignKey(AlumniUser, related_name="work_details")
    is_current = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title + " @ " + str(self.organisation.name)


class EducationDetail(models.Model):
    degree_name = models.CharField(max_length=100)
    degree_type = models.ForeignKey(DegreeType, null=True)
    field_of_study = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    school = models.ForeignKey(School)
    user = models.ForeignKey(AlumniUser, related_name="educations")
    is_current = models.BooleanField(default=False)

    def __unicode__(self):
        return self.degree_name + " @ " + str(self.school.name)


@receiver(social_account_added)
def populate_using_linkedin(request, sociallogin, **kwargs):
    extra_data = sociallogin.account.extra_data
    user = sociallogin.account.user
    provider = sociallogin.account.provider

    # Try to set the gender using information available from google sign-up.
    try:
        gender = user.socialaccount_set.filter(provider='google')[0].extra_data['gender']
        if gender == 'male':
            user.gender = 'M'

        elif gender == 'female':
            user.gender = 'F'

        else:
            user.gender = 'O'

    except Exception:
        pass

    # Populate user data with linkedin data.
    if provider == 'linkedin':

        # If email id is not same as iiitd-gmail id, set it as personal_email.
        if extra_data['email-address'] is not None:
            if extra_data['email-address'] != user.email:
                user.personal_email = extra_data['email-address']

        # Set linkedin_profile using public-profile-url
        if extra_data['public-profile-url'] is not None:
            user.linkedin_profile = extra_data['public-profile-url']


        # Add educations.

        if extra_data['educations'] is not None:
            educations_list = extra_data['educations']['education']

            # Check if educations_list is an actual list.
            # For a single education, linkedin returns a dictionary-type, not a list.
            # We see if the 'id' key is present.
            if 'id' not in educations_list:
                # Implies that it is an actual list.
                for education in educations_list:
                    edu_obj = EducationDetail()
                    edu_obj.user = user
                    if 'school-name' in education:
                        school_name = education['school-name']

                        # Check if school already exists, if not - create.
                        edu_obj.school, created = School.objects.get_or_create(name=school_name)

                    if 'start-date' in education:
                        if 'year' in education['start-date']:
                            start_year = int(education['start-date']['year'])
                            edu_obj.start_date = date(start_year, 1, 1)

                    if 'end-date' in education:
                        if 'year' in education['end-date']:
                            end_year = int(education['end-date']['year'])
                            edu_obj.end_date = date(end_year, 12, 31)

                    if 'field-of-study' in education:
                        edu_obj.field_of_study = education['field-of-study']

                    if 'degree' in education:
                        edu_obj.degree_name = education['degree']

                        if edu_obj.degree_name.lower().__contains__(
                                'bachelor') or edu_obj.degree_name.lower().startswith('b.'):
                            edu_obj.degree_type = DegreeType.objects.get(name="UG")

                        elif edu_obj.degree_name.lower().__contains__(
                                'master') or edu_obj.degree_name.lower().startswith('m.'):
                            edu_obj.degree_type = DegreeType.objects.get(name="PG")

                        elif edu_obj.degree_name.lower().__contains__(
                                'philosophy') or edu_obj.degree_name.lower().startswith('ph'):
                            edu_obj.degree_type = DegreeType.objects.get(name="PhD")

                    if edu_obj.start_date and edu_obj.end_date:
                        if edu_obj.start_date <= date.today() <= edu_obj.end_date:
                            edu_obj.is_current = True

                    edu_obj.save()

            # Only a single education.
            else:
                education = educations_list
                edu_obj = EducationDetail()
                edu_obj.user = user
                if 'school-name' in education:
                    school_name = education['school-name']

                    # Check if school already exists, if not - create.
                    edu_obj.school, created = School.objects.get_or_create(name=school_name)

                if 'start-date' in education:
                    if 'year' in education['start-date']:
                        start_year = int(education['start-date']['year'])
                        edu_obj.start_date = date(start_year, 1, 1)

                if 'end-date' in education:
                    if 'year' in education['end-date']:
                        end_year = int(education['end-date']['year'])
                        edu_obj.end_date = date(end_year, 12, 31)

                if 'field-of-study' in education:
                    edu_obj.field_of_study = education['field-of-study']

                if 'degree' in education:
                    edu_obj.degree_name = education['degree']

                    if edu_obj.degree_name.lower().__contains__(
                            'bachelor') or edu_obj.degree_name.lower().startswith('b.'):
                        edu_obj.degree_type = DegreeType.objects.get(name="UG")

                    elif edu_obj.degree_name.lower().__contains__(
                            'master') or edu_obj.degree_name.lower().startswith('m.'):
                        edu_obj.degree_type = DegreeType.objects.get(name="PG")

                    elif edu_obj.degree_name.lower().__contains__(
                            'philosophy') or edu_obj.degree_name.lower().startswith('ph'):
                        edu_obj.degree_type = DegreeType.objects.get(name="PhD")

                if edu_obj.start_date and edu_obj.end_date:
                    if edu_obj.start_date <= date.today() <= edu_obj.end_date:
                        edu_obj.is_current = True

                edu_obj.save()

        if extra_data['three-current-positions'] is not None:
            current_positions_list = extra_data['three-current-positions']['position']

            # Check if current_positions_list is an actual list.
            # For a single position, linkedin returns a dictionary-type, not a list.
            # We see if the 'id' key is present.
            if 'id' not in current_positions_list:
                # Implies that it is an actual list.
                for position in current_positions_list:
                    position_obj = WorkDetail()
                    position_obj.user = user
                    if 'company' in position:
                        if 'id' in position['company']:
                            linkedin_id = int(position['company']['id'])
                        else:
                            linkedin_id = -1

                        try:
                            position_obj.organisation = Organisation.objects.get(linkedin_id=linkedin_id)
                        except:
                            company_name = position['company']['name']
                            position_obj.organisation, created = Organisation.objects.get_or_create(name=company_name)


                    if 'start-date' in position:
                        if 'year' in position['start-date']:
                            start_year = int(position['start-date']['year'])
                        if 'month' in position['start-date']:
                            start_month = int(position['start-date']['month'])
                        else:
                            start_month = 1
                            edu_obj.start_date = date(start_year, start_month, 1)

                    if 'end-date' in position:
                        if 'year' in position['end-date']:
                            end_year = int(position['end-date']['year'])
                        if 'month' in position['end-date']:
                            end_month = int(position['end-date']['month'])
                        else:
                            end_month = 12
                            edu_obj.start_date = date(end_year, end_month, 1)

                    if 'title' in position:
                        position_obj.title = position['title']

                    if 'is-current' in position:
                        if position['is-current'] == "true":
                            position_obj.is_current = True

                    position_obj.save()

            else:
                position = current_positions_list
                position_obj = WorkDetail()
                position_obj.user = user
                if 'company' in position:
                    if 'id' in position['company']:
                        linkedin_id = int(position['company']['id'])
                    else:
                        linkedin_id = -1

                    try:
                        position_obj.organisation = Organisation.objects.get(linkedin_id=linkedin_id)
                    except:
                        company_name = position['company']['name']
                        position_obj.organisation, created = Organisation.objects.get_or_create(name=company_name)


                if 'start-date' in position:
                    if 'year' in position['start-date']:
                        start_year = int(position['start-date']['year'])
                    if 'month' in position['start-date']:
                        start_month = int(position['start-date']['month'])
                    else:
                        start_month = 1
                        edu_obj.start_date = date(start_year, start_month, 1)

                if 'end-date' in position:
                    if 'year' in position['end-date']:
                        end_year = int(position['end-date']['year'])
                    if 'month' in position['end-date']:
                        end_month = int(position['end-date']['month'])
                    else:
                        end_month = 12
                        edu_obj.start_date = date(end_year, end_month, 1)

                if 'title' in position:
                    position_obj.title = position['title']

                if 'is-current' in position:
                    if position['is-current'] == "true":
                        position_obj.is_current = True
                position_obj.save()

        if extra_data['three-past-positions'] is not None:
            past_positions_list = extra_data['three-past-positions']['position']

            # Check if past_positions_list is an actual list.
            # For a single position, linkedin returns a dictionary-type, not a list.
            # We see if the 'id' key is present.
            if 'id' not in past_positions_list:
                # Implies that it is an actual list.
                for position in past_positions_list:
                    position_obj = WorkDetail()
                    position_obj.user = user
                    if 'company' in position:
                        if 'id' in position['company']:
                            linkedin_id = int(position['company']['id'])
                        else:
                            linkedin_id = -1

                        try:
                            position_obj.organisation = Organisation.objects.get(linkedin_id=linkedin_id)
                        except:
                            company_name = position['company']['name']
                            position_obj.organisation, created = Organisation.objects.get_or_create(name=company_name)


                    if 'start-date' in position:
                        if 'year' in position['start-date']:
                            start_year = int(position['start-date']['year'])
                        if 'month' in position['start-date']:
                            start_month = int(position['start-date']['month'])
                        else:
                            start_month = 1
                            edu_obj.start_date = date(start_year, start_month, 1)

                    if 'end-date' in position:
                        if 'year' in position['end-date']:
                            end_year = int(position['end-date']['year'])
                        if 'month' in position['end-date']:
                            end_month = int(position['end-date']['month'])
                        else:
                            end_month = 12
                            edu_obj.start_date = date(end_year, end_month, 1)

                    if 'title' in position:
                        position_obj.title = position['title']

                    if 'is-current' in position:
                        if position['is-current'] == "true":
                            position_obj.is_current = True

                    position_obj.save()

            else:
                position = past_positions_list
                position_obj = WorkDetail()
                position_obj.user = user
                if 'company' in position:
                    if 'id' in position['company']:
                        linkedin_id = int(position['company']['id'])
                    else:
                        linkedin_id = -1

                    try:
                        position_obj.organisation = Organisation.objects.get(linkedin_id=linkedin_id)
                    except:
                        company_name = position['company']['name']
                        position_obj.organisation, created = Organisation.objects.get_or_create(name=company_name)


                if 'start-date' in position:
                    if 'year' in position['start-date']:
                        start_year = int(position['start-date']['year'])
                    if 'month' in position['start-date']:
                        start_month = int(position['start-date']['month'])
                    else:
                        start_month = 1
                        edu_obj.start_date = date(start_year, start_month, 1)

                if 'end-date' in position:
                    if 'year' in position['end-date']:
                        end_year = int(position['end-date']['year'])
                    if 'month' in position['end-date']:
                        end_month = int(position['end-date']['month'])
                    else:
                        end_month = 12
                        edu_obj.start_date = date(end_year, end_month, 1)

                if 'title' in position:
                    position_obj.title = position['title']

                if 'is-current' in position:
                    if position['is-current'] == "true":
                        position_obj.is_current = True
                position_obj.save()


        user.save()
                        # print extra_data, user.first_name, provider, extra_data['first-name']