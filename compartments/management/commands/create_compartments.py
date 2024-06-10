# File: compartments/management/commands/create_compartments.py

from django.core.management.base import BaseCommand
from compartments.models import Compartment

class Command(BaseCommand):
    help = 'Generate 100 compartments with empty status'

    def handle(self, *args, **kwargs):
        compartments = []
        for i in range(1, 101):
            compartments.append(Compartment(number=i, is_empty=True))

        Compartment.objects.bulk_create(compartments)
        self.stdout.write(self.style.SUCCESS('Successfully created 100 compartments with empty status.'))
