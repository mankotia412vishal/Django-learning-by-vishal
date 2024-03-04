from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples=[
        {'name':"Vishal Singh",'age':21},
        {'name':"Rahul Singh",'age':22},
        {'name':"Gurmeet Singh","age":21},
       
    ]
    for people in peoples:
        print(people)
    text="""Lorem ipsum dolor sit, amet consectetur adipisicing elit. Minus nulla eum placeat molestiae inventore labore tenetur nostrum vel similique. Labore numquam facere unde praesentium, eaque similique voluptates maiores nihil exercitationem impedit animi officia, perferendis modi maxime cum minus cumque itaque totam nobis doloribus quae obcaecati delectus. Provident iusto quam alias quos quibusdam aut labore voluptates quis praesentium, reprehenderit vel architecto ex facere numquam sed quo cumque eaque neque iure recusandae possimus doloremque similique modi laboriosam! Enim laudantium odio quibusdam officiis sequi tempora explicabo, expedita ad facere porro ut nemo tenetur illum voluptas voluptates aliquid et in ducimus iusto. Blanditiis, sed!"""
    vegtable=['potato','tomato','ladyfinger']
    return render(request,"home/index.html",context={'peoples':peoples,'text':text,'vegetables':vegtable,'page':"Index Page"})

def success_page(request):
    print("start "*10)
    return HttpResponse("<h1> Hey I am Intern at MSCI </h1>")

def about(request):
    context={'page':"About"}
    return render(request,"home/about.html",context)
def contact(request):
    context={'page':'contact'}
    return render(request,"home/contact.html",context)
