__author__ = 'ankur'

import xlrd
from django.core.management.base import BaseCommand, CommandError
from AlumniPortal.models import Student, SpecialisationStream, Degree, Branch

class Command(BaseCommand):
    help = 'Adds the data of Alumni till 2013 given file as input'

    def handle(self, *args, **options):
        try:
            inpfile = xlrd.open_workbook(args[0])
        except:
            print "cannot open file, please provide file path as argument"
            return

        for sheetname in inpfile.sheet_names():
            sheet_data = sheetname.split('-')
            year,degree,branch,specialization = sheet_data[0], sheet_data[1], sheet_data[2],sheet_data[3]

            branch = Branch.objects.get(name=branch)
            if (specialization == ''):  #only BTechs
                degree = Degree.objects.get(name=degree,branch=branch,specialisation=None)
            else:
                stream = SpecialisationStream.objects.get(name=specialization)
                degree = Degree.objects.get(name=degree,branch=branch, specialisation=stream)

            worksheet = inpfile.sheet_by_name(sheetname)
            num_rows = worksheet.nrows - 1
            curr_row = 1
            while curr_row < num_rows:
                curr_row += 1
                row = worksheet.row(curr_row)
                name = worksheet.cell_value(curr_row, 2)
                email = worksheet.cell_value(curr_row, 3)
                student = Student(name=name, iiitd_email=email, graduation_year=int(year), degree=degree)
                student.save()
        print "data imported"
