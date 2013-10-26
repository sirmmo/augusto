from django.core.management.base import BaseCommand, CommandError
from core.models import *
from core.tasks import * 

import os
import re

class Command(BaseCommand):
    args = '<folder>'
    help = 'loads all pdf files from folder'

    def handle(self, *args, **options):
        num = 1
        files = [f for f in os.listdir(args[0]) if f.endswith('.pdf')] 
        for f in files:
			print num, f
			num += 1
			name = f.split('/')[-1].split('.')[0]
			part = " ".join(name.split('_')[1:])
			name = name.split('_')[0]
			year = name[0:4]
			nyear = int(year)
			number = name[4:]
			int_list = [int(s) for s in re.findall('\\d+', number)]
			nnumber = int_list[0]
			i = IssueDetails.objects.create(filename=f, year=year, nyear = nyear, number=number, nnumber = nnumber, mode=part)
			print i

