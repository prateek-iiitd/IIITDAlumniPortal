__author__ = 'Prateek'

from django.db import models

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))


def news_large_image(self, filename):
    return '/'.join(['news', 'full', self.id, filename])


def news_thumb_image(self, filename):
    return '/'.join(['news', 'thumb', self.id, filename])

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
    starts_at = models.DateTimeField(db_index=True)

    def __unicode__(self):
        return self.title + " on " + str(self.starts_at) + " at " + self.venue


class NewsArticle(models.Model):
    headline = models.CharField(max_length=200, db_index=True)
    article = models.TextField()
    occurred_on = models.DateField(db_index=True)
    large_img = models.ImageField(blank=True, null=True, upload_to=news_large_image)
    thumbnail = models.ImageField(blank=True, null=True, upload_to=news_thumb_image)
    reporter = models.CharField(max_length=40, db_index=True)


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