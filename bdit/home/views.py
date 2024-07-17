from django.shortcuts import render

from django.http import HttpResponse

def home(request):
   
    peoples=[
       {'first':'Rahul','last':'gupta','age':20},
       {'first':'Jay','last':'singh','age':23},
       {'first':'Amit','last':'shah','age':12},
    ]


    text =  '''Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officia, vero natus! Ex nesciunt, aliquid doloremque, magni nihil velit veritatis, officiis rem quisquam dolores nemo mollitia repellendus illo. Qui eum alias dolores exercitationem itaque enim fugiat est, molestiae quaerat quod, ad maxime at, earum voluptatem? Dolore similique doloremque maxime quas necessitatibus?'''
 
    fruits = ['apple','mango','grapes']
    


    return render(request, 'home/index.html',context={'page':'Bdit','peoples' : peoples,'text' : text,'fruits':fruits})


def aboutus(request):
    context =   {'page': 'aboutus'}
    return render(request, 'home/aboutus.html',context)


def contact(request):
    context = {'page' : 'contact'}
    return render(request, 'home/contact.html',context)