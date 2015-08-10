# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
def here(request):
	return HttpResponse("My first Django home work _ 我的名字是繼銘")
def plus(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(str(s))
def math(request, a , b):
	s = int(a) + int(b)
	d = int(a) - int(b)
	p = int(a) * int(b)
	q = int(a) / int(b)
	return render_to_response('math.html',locals())
	
	
#	t = get_template('math.html')
#	c = template.Context({'s':s,'d':d,'p':p,'q':q})	
#	return HttpResponse(t.render(c))
#	with open('templates/math.html','r') as reader:
#		t = template.Template(reader.read())
#		c = template.Context({'s':s,'d':d,'p':p,'q':q})	
#	return HttpResponse(t.render(c))
		  
	