from django.core.management.base import BaseCommand, CommandError
from core.models import *
from core.tasks import * 

import os

class Command(BaseCommand):
    args = '<folder>'
    help = 'loads all pdf files from folder'

    def handle(self, *args, **options):
        num = 1
        files = [f for f in os.listdir(args[0]) if f.endswith('.pdf')] 
        for f in files:
                print num, f
                num += 1
		store_issue(os.path.join(args[0],f))
