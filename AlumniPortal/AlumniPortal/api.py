__author__ = 'ankur'

from tastypie.resources import ModelResource
from models import *
from tastypie.authentication import SessionAuthentication, Authentication
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from django.db.models import Q
import base64
import os
from tastypie.fields import FileField
from django.core.files.uploadedfile import SimpleUploadedFile
import mimetypes
from tastypie.serializers import Serializer
import datetime
from django.utils import dateformat

# AUTHENTICATION_OBJECT = SessionAuthentication()
AUTHENTICATION_OBJECT = Authentication()
AUTHORIZATION_OBJECT = Authorization()


class Base64FileField(FileField):
    """
    A django-tastypie field for handling file-uploads through raw post data.
    It uses base64 for en-/decoding the contents of the file.
    Usage:

    class MyResource(ModelResource):
        file_field = Base64FileField("file_field")

        class Meta:
            queryset = ModelWithFileField.objects.all()

    In the case of multipart for submission, it would also pass the filename.
    By using a raw post data stream, we have to pass the filename within our
    file_field structure:

    file_field = {
        "name": "myfile.png",
        "file": "longbas64encodedstring",
        "content_type": "image/png" # on hydrate optional
    }
    """

    def dehydrate(self, bundle, for_list):
        if not bundle.data.has_key(self.instance_name) and hasattr(bundle.obj, self.instance_name):
            file_field = getattr(bundle.obj, self.instance_name)
            if file_field:
                try:
                    content_type, encoding = mimetypes.guess_type(file_field.file.name)
                    b64 = open(file_field.file.name, "rb").read().encode("base64")
                    ret = {
                        "name": os.path.basename(file_field.file.name),
                        "file": b64,
                        "content-type": content_type or "application/octet-stream"
                    }
                    return ret
                except:
                    pass
        return None

    def hydrate(self, obj):
        value = super(FileField, self).hydrate(obj)
        if value:
            value = SimpleUploadedFile(value["name"], base64.b64decode(value["file"]), getattr(value, "content_type", "application/octet-stream"))
        return value


class CustomDateSerializer(Serializer):
    def format_date(self, data):
        return data.strftime("%b '%y")

class CountryResource(ModelResource):
    class Meta:
        queryset = Country.objects.all()
        resource_name = 'country'
        authentication = AUTHENTICATION_OBJECT
        authorization = AUTHORIZATION_OBJECT

        fields = ['name']
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']

        ordering = ['name']

        filtering = {
            'name': ('iexact',),
        }

class CityResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'city'
        authentication = AUTHENTICATION_OBJECT
        authorization = AUTHORIZATION_OBJECT

        fields = ['city']
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']

        ordering = ['city']

        filtering = {
            'name': ('icontains',),
        }

class LocationResource(ModelResource):
    country = fields.ForeignKey(CountryResource, 'country', full=True)

    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        authentication = AUTHENTICATION_OBJECT
        authorization = AUTHORIZATION_OBJECT

        fields = ['city', 'country']
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']

        filtering = {
            "city": ('icontains', ),
            "country": ALL_WITH_RELATIONS,
        }
        ordering = ['city', 'country']

class OrganisationResource(ModelResource):
    location = fields.ForeignKey(LocationResource, 'location', full=True, null=True)

    class Meta:
        queryset = Organisation.objects.all()
        resource_name = 'organisation'
        authentication = AUTHENTICATION_OBJECT
        authorization = AUTHORIZATION_OBJECT

        fields = ['name', 'location']
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get', 'patch']
        max_limit = 0

        filtering = {
            "name": ('icontains', ),
            "location": ALL_WITH_RELATIONS,
        }

        ordering = ['name']


class SchoolResource(ModelResource):
    location = fields.ForeignKey(LocationResource, 'location', full=True, null=True)

    class Meta:
        queryset = School.objects.all()
        resource_name = 'school'
        authentication = AUTHENTICATION_OBJECT
        authorization = AUTHORIZATION_OBJECT

        fields = ['name']
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        max_limit = 0

        filtering = {
            "name": ('icontains', ),
            "location": ALL_WITH_RELATIONS,
        }

        ordering = ['name']


class DegreeTypeResource(ModelResource):
    class Meta:
        queryset = DegreeType.objects.all()
        resource_name = 'degreetype'
        authentication = AUTHENTICATION_OBJECT
        authorization = AUTHORIZATION_OBJECT

        fields = ['name', 'desc']
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        max_limit = 0

        filtering = {
            'name': ('iexact',),
        }


class WorkTypeResource(ModelResource):
    class Meta:
        queryset = WorkType.objects.all()
        resource_name = 'worktype'
        authentication = AUTHENTICATION_OBJECT
        authorization = AUTHORIZATION_OBJECT

        fields = ['name', 'desc']
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        max_limit = 0

        filtering = {
            'name': ('iexact',),
        }


class WorkDetailResource(ModelResource):
    work_type = fields.ForeignKey(WorkTypeResource, 'work_type', full=True, null=True)
    organisation = fields.ForeignKey(OrganisationResource, 'organisation', full=True)

    class Meta:
        queryset = WorkDetail.objects.all()
        resource_name = 'workdetail'
        authentication = AUTHENTICATION_OBJECT
        authorization = AUTHORIZATION_OBJECT

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        max_limit = 0
        excludes = ['id']
        serializer = CustomDateSerializer(formats=['json'])

        filtering = {
            'work_type': ALL_WITH_RELATIONS,
            'organisation': ALL_WITH_RELATIONS,
            'is_current': ('exact', ),
        }


class EducationResource(ModelResource):
    school = fields.ForeignKey(SchoolResource, 'school', full=True)
    degree_type = fields.ForeignKey(DegreeTypeResource, 'degree_type', full=True)

    class Meta:
        queryset = EducationDetail.objects.all()
        resource_name = 'education'
        # authentication = SessionAuthentication()
        authentication = Authentication()
        authorization = Authorization()

        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        serializer = CustomDateSerializer(formats=['json'])

        filtering = {
            'degree_type': ALL_WITH_RELATIONS,
            'school': ALL_WITH_RELATIONS,
            'is_current': ('exact', ),
        }


# Resource for the logged in user.
class CurrentProfileResource(ModelResource):
    educations = fields.ToManyField('AlumniPortal.api.EducationResource', "educations", full=True, null=True)
    work_details = fields.ToManyField('AlumniPortal.api.WorkDetailResource', "work_details", full=True, null=True)
    current_location = fields.ForeignKey(LocationResource, 'current_location', full=True, null=True)
    profile_photo = Base64FileField("profile_photo", null=True)

    class Meta:
        queryset = AlumniUser.objects.all()
        resource_name = 'current'
        # authentication = SessionAuthentication()
        authentication = Authentication()
        authorization = Authorization()
        detail_allowed_methods = ['get', 'put']
        list_allowed_methods = ['get', 'put']

        excludes = ['created_at', 'is_admin', 'is_active', 'last_login', 'password']

    # filter to allow only `user` object.
    def get_object_list(self, request):
        return super(CurrentProfileResource, self).get_object_list(request).filter(pk=request.user.pk)

    def hydrate_current_location(self, bundle):
        country_obj = Country.objects.get_or_create(name=bundle.data['current_location']['country']['name'])
        city_obj = Location.objects.get_or_create(city=bundle.data['current_location']['city'], country=country_obj[0])
        bundle.data['current_location'] = city_obj[0]
        return bundle

    def hydrate_educations(self, bundle):
        if bundle.obj.pk:
            for education in bundle.data['educations']:
                location = education.data['school']['location']
                country_obj = Country.objects.get_or_create(name=location['country']['name'])
                location_obj = Location.objects.get_or_create(city=location['city'],
                                                              country=country_obj[0])
                school_obj = School.objects.get_or_create(location=location_obj[0],
                                                          name=education.data['school']['name'])
                degree_type_obj = DegreeType.objects.get_or_create(name=education.data['degree_type']['name'],
                                                                   desc=education.data['degree_type']['desc']
                )
                education_obj = EducationDetail.objects.get_or_create(degree_name=education.data['degree_name'],
                                                                   school=school_obj[0],
                                                                   end_date=education.data['end_date'],
                                                                   field_of_study=education.data[
                                                                       'field_of_study'],
                                                                   degree_type=degree_type_obj[0],
                                                                   start_date=education.data['start_date'],
                                                                   is_current=education.data['is_current'],
                                                                   user_id=bundle.request.user.id
                )
                education.obj = education_obj[0]
        return bundle


    def hydrate_work_details(self, bundle):
        if bundle.obj.pk:
            for work_detail in bundle.data['work_details']:
                location = work_detail.data['organisation']['location']
                country_obj = Country.objects.get_or_create(name=location['country']['name'])[0]
                location_obj = Location.objects.get_or_create(city=location['city'],
                                                              country=country_obj)[0]
                organisation_obj = Organisation.objects.get_or_create(location=location_obj,
                                                          name=work_detail.data['organisation']['name'])[0]
                work_type_obj = WorkType.objects.get_or_create(name=work_detail.data['work_type']['name'],
                                                                   desc=work_detail.data['work_type']['desc']
                )[0]
                work_detail_obj = WorkDetail.objects.get_or_create(title = work_detail.data['title'],
                                                                   start_date=work_detail.data['start_date'],
                                                                   end_date=work_detail.data['end_date'],
                                                                   work_type=work_type_obj,
                                                                   organisation=organisation_obj,
                                                                   user_id=bundle.request.user.id,
                                                                   is_current=work_detail.data['is_current']
                )[0]
                work_detail.obj = work_detail_obj
        return bundle


# Resource for list of basic profiles
class BasicProfileResource(ModelResource):
    work_details = fields.ToManyField('AlumniPortal.api.WorkDetailResource', "work_details", full=True, null=True)
    current_location = fields.ForeignKey(LocationResource, 'current_location', full=True, null=True)

    class Meta:
        queryset = AlumniUser.objects.all()
        resource_name = 'basic'
        # authentication = SessionAuthentication()
        authentication = Authentication()
        authorization = Authorization()

        detail_allowed_methods = ['get']
        list_allowed_methods = ['get']

        fields = ['first_name', 'last_name', 'profile_photo', 'graduation_year', 'id', 'email', 'work_details',
                  'current_location']


# Resource individual profile view
class FullProfileResource(ModelResource):
    educations = fields.ToManyField('AlumniPortal.api.EducationResource', "educations", full=True, null=True)
    work_details = fields.ToManyField('AlumniPortal.api.WorkDetailResource', "work_details", full=True, null=True)
    current_location = fields.ForeignKey(LocationResource, 'current_location', full=True)

    class Meta:
        queryset = AlumniUser.objects.all()
        resource_name = 'full'
        # authentication = SessionAuthentication()
        # authentication = Authentication()
        # authorization = Authorization()

        detail_allowed_methods = ['get']
        list_allowed_methods = []
        serializer = CustomDateSerializer(formats=['json'])

        fields = ['first_name', 'last_name', 'profile_photo', 'graduation_year', 'gender', 'marital_status',
                  'email', 'personal_email', 'work_details', 'current_location',
                  'facebook_profile', 'google_profile', 'linkedin_profile', 'twitter_profile', 'homepage', ]


class testProfileResource(ModelResource):
    educations = fields.ToManyField('AlumniPortal.api.EducationResource', "educations", full=True, null=True)
    work_details = fields.ToManyField('AlumniPortal.api.WorkDetailResource', "work_details", full=True, null=True)
    current_location = fields.ForeignKey(LocationResource, 'current_location', full=True)
    full_name = fields.CharField(attribute='get_full_name', readonly=True)

    def dehydrate(self, bundle):
        bundle.data.pop("educations")
        # bundle.data.pop("work_details")
        bundle.data = bundle.data
        return bundle

    class Meta:
        queryset = AlumniUser.objects.all()
        resource_name = 'filter'
        # authentication = SessionAuthentication()
        authentication = Authentication()
        authorization = Authorization()
        detail_allowed_methods = ['get', 'put']
        list_allowed_methods = ['get']

        excludes = ['created_at', 'is_admin', 'is_active', 'last_login', 'password', 'educations']

        filtering = {
            "first_name": ('istartswith', ),
            "last_name": ('istartswith', ),
            #"full_name": ALL_WITH_RELATIONS,
            "gender": ('iexact', ),
            "graduation_year": ('lte', 'gte'),
            "educations": ALL_WITH_RELATIONS,
            "work_details": ALL_WITH_RELATIONS,
            "current_location": ALL_WITH_RELATIONS,
        }

    def dehydrate(self, bundle):
        bundle.data.pop("educations")
        bundle.data = bundle.data
        return bundle

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        orm_filters = super(testProfileResource, self).build_filters(filters)

        if('full' in filters):
            name_search_string = filters['full'].strip()
            name_parts = name_search_string.split()

            queries = [Q(first_name__istartswith=value) | Q(last_name__istartswith=value) for value in name_parts]
            query = queries.pop()

            for item in queries:
                query &= item

            orm_filters.update({'full': (query)})

        return orm_filters

    def apply_filters(self, request, applicable_filters):
        if 'full' in applicable_filters:
            custom = applicable_filters.pop('full')
        else:
            custom = None

        semi_filtered = super(testProfileResource, self).apply_filters(request, applicable_filters)

        return semi_filtered.filter(custom) if custom else semi_filtered