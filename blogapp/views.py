from django.shortcuts import render,redirect
from blogapp.models import Blog
from blogapp.forms import BlogForm
from django.views.generic import DetailView
from django.core.paginator import Paginator
# Create your views here.


def fetch_data(request):
    all_blog=Blog.objects.all()

    p=Paginator(all_blog,2)#2 posts per page
    page_number=request.GET.get('page')
    print(page_number)
    page_obj=p.get_page(page_number)
    print(page_obj)
    context={
        'page_obj':page_obj
    }
    return render(request,'blog.html',context)

def insert_data(request):
    form=BlogForm()
    if request.method == "POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/blog")

    return render(request,"insert.html",{'form':form})
    

class DisplayOneData(DetailView):
    model = Blog