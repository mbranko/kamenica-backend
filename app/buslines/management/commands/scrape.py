import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from ...scraper import get_all_bus_lines


class Command(BaseCommand):
    help = 'Scrape gspns.co.rs website'

    def handle(self, *args, **options):
        bus_lines = get_all_bus_lines()
        text = json.dumps(bus_lines, sort_keys=True, indent=2, cls=DjangoJSONEncoder)
        file_name = os.path.join(settings.MEDIA_ROOT, 'bus-lines.json')
        with open(file_name, 'w') as output_file:
            output_file.write(text)
        self.stdout.write(f'Podaci sacuvani u {file_name}')
