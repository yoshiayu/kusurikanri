from django.core.management.base import BaseCommand
from kusuriapp.models import Kusuri_Data
import openpyxl
import sys

file_xlsx = "static/kusuriapp/link.xlsx"

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
#
        sys.stderr.write("*** start ***\n")
        fp = open(file_xlsx, 'r')
        reader = openpyxl.reader(fp)
        for rr in reader:
            print(rr)
            hh = Kusuri_Data()
            hh.company_id = rr[0]
            hh.ccompany_name = rr[1]
            hh.medicine_id = rr[2]
            hh.medicine_name = rr[3]
            hh.initials = rr[4]
            hh.save()
#
        sys.stderr.write("*** end ***\n")
        fp.close()