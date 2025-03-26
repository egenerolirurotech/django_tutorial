from django.http import HttpRequest, HttpResponse
from django.template import loader

# Create your views here.
def myapp(request: HttpRequest) -> HttpResponse:
    """
    baby's first view
    """
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
