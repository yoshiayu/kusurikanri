from django.core.management.base import BaseCommand, CommandError
from kusuriapp.models import Question as KusuriData
class Command(BaseCommand):
    help = 'Closes the specified KusuriData for voting'

    def add_arguments(self, parser):
        parser.add_argument('kusuri_datas', nargs='+', type=int)

    def handle(self, *args, **options):
        for kusuri_datas in options['kusuri_datas']:
            try:
                kusuri_datas = KusuriData.objects.get(pk=kusuri_datas)
            except KusuriData.DoesNotExist:
                raise CommandError('KusuriData "%s" does not exist' % kusuri_datas)

            KusuriData.opened = False
            KusuriData.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed KusuriData "%s"' % kusuri_datas))