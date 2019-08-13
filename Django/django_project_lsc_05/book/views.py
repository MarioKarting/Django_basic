from django.shortcuts import render
from django.views import View
# from book.models import BookInfo, HeroInfo
from django.http import JsonResponse


# Create your views here.

class BookView(View):
    def get(self, request,version):

    #     if version == '1.0':
    #         book = BookInfo.objects.get(id=1)
    #         return render(request, 'index.html', {'name': book.btitle})
    #
    #     elif version == '2.0':
    #         return JsonResponse({'name':book.btitle})
    #     else:
    #         return JsonResponse({'name':book.btitle})
    #
    #
    # def get(self):
        pass

class HeroView(View):
    # def get(self, request):
    #     hero = HeroInfo.objects.get(id=1)
    #     # return render(request, 'hero.html', {'name': hero.hname})
    #     return JsonResponse({'name':hero.hname})
    pass