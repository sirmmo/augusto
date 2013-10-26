from django.http import HttpResponse
from django.shortcuts import render_to_response

from core.models import *

modes = {
	"SO":"Supplemento Ordinario",
	"IMT":"Indice Annuale per Materia",
	"IMD":"Indice Annuale o Mensile",
	"P1":"Parte 1",
	"P2":"Parte 2",
	"PM":"Parte ufficiale e Parte non ufficiale",
	"FI":"Foglio delle Inserzioni",

}

def index(request):
	query = request.REQUEST.get('q')
	if query is not None:
		the_list = list(Issue.objects.filter(text__contains = query).values('filename', 'year', 'number', 'mode'))
		for el in the_list:
			el['mode'] = modes.get(el['mode'], el['mode'])
			el['filename'] = el['filename'].split('/')[-1].split('.')[0]
		the_list_count = len(the_list)
		return render_to_response('search.html', {"list":the_list, "count":the_list_count})
	return render_to_response('search.html')
