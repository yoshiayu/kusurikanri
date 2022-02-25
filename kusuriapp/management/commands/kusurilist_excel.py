from django.core.management.base import BaseCommand
from kusuriapp.models import KusuriData
import sys

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        sys.stderr.write("*** start ***\n")
#
        for h in KusuriData.objects.all():
            print(h.company_id,"\t", end="")
            print(h.company_name,"\t", end="")
            print(h.medicine_id,"\t", end="")
            print(h.medicine_name,"\t", end="")
            print(h.initials)
#
        sys.stderr.write("*** end ***\n")