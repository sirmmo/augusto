from celery import task
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from cStringIO import StringIO
from core.models import *
 
def scrap_pdf(path):
    """From http://stackoverflow.com/a/8325135/39040."""
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr)
    fp = file(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str	


@task
def store_issue(filename):
    ji = Issue.objects.create(filename=filename, text=scrap_pdf(filename))
    name = filename.split('/')[-1].split('.')[0]
    part = " ".join(name.split('_')[1:])
    name = name.split('_')[0]
    year = name[0:4]
    nyear = int(year)
    number = name[4:]
    int_list = [int(s) for s in re.findall('\\d+', number)]
    nnumber = int_list[0]
    i = IssueDetails.objects.create(issue = ji, filename=f, year=year, nyear = nyear, number=number, nnumber = nnumber, mode=part)
    print ji.id, i.id

	
