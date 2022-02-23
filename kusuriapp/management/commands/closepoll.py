from django.core.management.base import BaseCommand, CommandError
from kusuriapp.models import Question as Kusuri_Data
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for kusuri_data in options['poll_ids']:
            try:
                kusuri_data = Kusuri_Data.objects.get(pk=kusuri_data)
            except kusuri_data.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % kusuri_data)

            kusuri_data.opened = False
            kusuri_data.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % kusuri_data))