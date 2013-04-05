from django.http import HttpResponse, HttpResponseRedirect
import re, subprocess

safe_filename = re.compile('^([0-9\-\/]+\.[0-9]+)\.xml$')

def split(request, filename):
    m = safe_filename.match(filename)
    if not m:
        return HttpResponse('invalid filename')
    rootdir = u'/home/bjwebb/iati/CSV-IATI-Converter/csviati/static/'
    subprocess.Popen(['xsltproc', '--stringparam', 'outprefix', rootdir+m.group(1)+'/iati-activities', '/home/bjwebb/iati/IATI-XSLT/templates/xml/iati-split.xsl', rootdir+filename])
    return HttpResponseRedirect(u'http://csv.iati.bjwebb.co.uk/static/'+m.group(1))
