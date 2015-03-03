from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from sample1.forms import createJobForm
import sample1
import crowdflower
import crowdflower.client
import numpy as np
# Create your views here.

key = 'gL34yyLa5W3fHwRqgbtS'
#conn = crowdflower.Connection(api_key=key)
client = crowdflower.client.Client(key)


data = [
    {'id':    '1',    'link':    'http://i.imgur.com/wqCw6iS.png', 'color_gold': 'Red'},
    {'id':    '2',    'link':    'http://i.imgur.com/gYY10E8.png'},
    {'id':    '3',    'link':    'http://i.imgur.com/Ma6SUUU.png'},
    {'id':    '4',    'link':    'http://i.imgur.com/xxasDu4.png'},
    {'id':    '5',    'link':    'http://i.imgur.com/FNr2W4d.png'},
    {'id':    '6',    'link':    'http://i.imgur.com/2HXm57q.png'},
    {'id':    '7',    'link':    'http://i.imgur.com/wSK1pKv.png'},
    {'id':    '8',    'link':    'http://i.imgur.com/PGqPwSN.png'},
    {'id':    '9',    'link':    'http://i.imgur.com/IuC09Ep.png'},
    {'id':    '10',    'link':    'http://i.imgur.com/qeC6oVe.png'},
    {'id':    '11',    'link':    'http://i.imgur.com/sitniyO.png'},
    {'id':    '12',    'link':    'http://i.imgur.com/UGxUgcF.png'}
]

def submitjob(request):
  return HttpResponse("Done")
  
def createjob(request):
    form = createJobForm(request.POST, request.FILES)
    if form.is_valid():
        confidence_fields = np.asarray(form.cleaned_data['confidence_fields'].split(' '))
        included_countries = np.asarray(form.cleaned_data['included_countries'])
        excluded_countries = np.asarray(form.cleaned_data['excluded_countries'])
        job = client.create_job(
                            {
                            'title': form.cleaned_data['title'],
                            'payment_cents': form.cleaned_data['payment_cents'],
                            'judgments_per_unit': form.cleaned_data['judgments_per_unit'],
                            'instructions': form.cleaned_data['instructions'],
                            'cml': form.cleaned_data['cml'],
                            'confidence_fields': confidence_fields,
                            'max_judgments_per_unit': form.cleaned_data['max_judgments_per_unit'],
                            'min_unit_confidence': form.cleaned_data['min_unit_confidence'],
                            'auto_order': form.cleaned_data['auto_order'],
                            'auto_order_threshold': form.cleaned_data['auto_order_threshold'],
                            'auto_order_timeout': form.cleaned_data['auto_order_timeout'],
                            'units_per_assignment': form.cleaned_data['units_per_assignment'],
                            'included_countries': included_countries,
                            'excluded_countries': excluded_countries,
                            })
        job.upload(data)
        #job.set_job_channels('cf_internal')
        job.launch(2, channels=['cf_internal'])
    return render(request, 'sample1/newJob.html', {'form': form})

