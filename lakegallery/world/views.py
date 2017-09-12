from django.shortcuts import render
from .models import WorldBorder
# Create your views here.


def index(request):
    data = WorldBorder.objects.filter(name='United States')
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))
    print(data)
    context = {'q': data[0]}
#     return render(request, 'polls/index.html', context)
    return render(request, 'world/index.html', context)
