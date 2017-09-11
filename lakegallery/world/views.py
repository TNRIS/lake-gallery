from django.shortcuts import render

from django.core.serializers import serialize
from .models import WorldBorder
# Create your views here.


def index(request):
    data = serialize('geojson', WorldBorder.objects.all(), geometry_field='mpoly', fields=('name'))
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))
    # print(data)
    context = {'data': data}
#     return render(request, 'polls/index.html', context)
    return render(request, 'world/index.html', context)
