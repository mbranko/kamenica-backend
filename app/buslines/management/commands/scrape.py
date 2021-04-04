import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
import requests
from ...scraper import get_all_bus_lines


class Command(BaseCommand):
    help = 'Scrape gspns.co.rs website'

    def handle(self, *args, **options):
        bus_lines = get_all_bus_lines()
        file_name = os.path.join(settings.MEDIA_ROOT, 'bus-lines.json')
        with open(file_name, 'w') as output_file:
            output_file.write(json.dumps(bus_lines, indent=2))
        self.stdout.write(f'Podaci sacuvani u {file_name}')
