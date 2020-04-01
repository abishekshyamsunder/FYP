import django
from django.shortcuts import render
from django.db.models import Q
from django.apps import apps
from django.http import JsonResponse
from django.core import serializers
from .forms import PostForm
from .models import Post, Requirements
import UI.random.summa
import UI.summa
import UI.dsm.parent
from UI.pos5 import returns_testcase

# Create your views here.


class viewClass:
    def page(self, request):
        form = PostForm()
        if request.method == "POST":
            suggestion = request.POST['hidden']
            form = PostForm(request.POST)
            header = form.data['header']
            name = form.data['name']
            id_number = form.data['id_number']
            tester = form.data['tester']
            date = form.data['date']
            urgency = form.data['urgency']
            types = form.data['types']
            test_object = form.data['test_object']
            description = form.data['description']
            version = form.data['version']
            remarks = form.data['remarks']
            file1 = open('temp','w')
            file1.write(description + "\t" + suggestion[21:])
            file1.close()
            print(header + name + id_number + tester + date + urgency + types + test_object
                  + description + version + remarks)
            if form.is_valid:
                print("OK")
                info = Post(header=header, name=name, id_number=id_number, tester=tester,
                            date=date, urgency=urgency, types=types, test_object=test_object,
                            description=description, version=version, remarks=remarks)
                info.save()
                form = PostForm()
                return render(request, 'UI/page_form.html', {'form': form})
        else:
            # Post.objects.all().delete()
            form = PostForm()

        return render(request, 'UI/page_form.html', {'form': form})

    def search(self, request):
        form = PostForm()
        print("In Display")
        x = Post.objects.all()
        print(x)
        if request.method == "POST":
            form = PostForm(request.POST)
            search_query = form.data['name']
            post = apps.get_model('UI', 'Post')
            # Add your models here, in any way you find best.
            search_models = [post]
            search_results = []
            for model in search_models:
                fields = [x for x in model._meta.fields if isinstance(
                    x, django.db.models.CharField)]
                search_queries = [
                    Q(**{x.name + "__contains": search_query}) for x in fields]
                q_object = Q()
                for query in search_queries:
                    q_object = q_object | query

            results = model.objects.filter(q_object)
            search_results.append(results)
            print(search_results)
            content = {'form': form, 'search_results': search_results}
            return render(request, 'UI/page_display.html', content)
        return render(request, 'UI/page_display.html', {'form': form})

    def search_status(self, request):
        if request.method == "GET":
            search_text = request.GET.get('search_text')
            print(search_text)
            if search_text is not None and search_text != u"":
                search_text = request.GET.get('search_text')
                statuss = Post.objects.filter(
                    description__icontains=search_text)
                print(statuss.values('description'))
            else:
                statuss = []
            data = serializers.serialize('json', statuss)
            return JsonResponse(data, safe=False)

    def func2(self,request):
        search_text = ""
        if request.method == "GET":
            search_text = request.GET.get('search_text')
            print(search_text)
        data = UI.dsm.parent.check(search_text)
        # data = " Summa"
        return JsonResponse({'data':data})

    def func3(self,request):
        if request.method == "GET":
            # data = UI.dsm.parent.check(search_text)
            print("OIK")
            data = request.GET.get('search_text')
            print(data)
            data = data.replace('<td>','')
            data = data.replace('</td>','')
            #data = data.replace('\n','')
            #data = data.replace(' ','')
            data = data.split("\n")[2]
            
            print(data)

            testcase = returns_testcase(data)
            return JsonResponse({'data':testcase})
        return JsonResponse({'data':"No possible Testcase"})

    
    def testcase(self, request):
        data = Requirements.objects.all()
        return render(request, 'UI/page_testcase.html', {'data': data})