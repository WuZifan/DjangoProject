from django.http import HttpResponse
import threading as tdg
import time



def hello(request):
	
	print(tdg.currentThread().getName())

	#for i in range(10):
	#	time.sleep(1)
	res=HttpResponse('Hello World'+':::'+tdg.currentThread().getName())
	print(str(res))
	return res

def nonsense(request):
	print(tdg.currentThread().getName())
	res=HttpResponse('Hello World2222'+'::  '+tdg.currentThread().getName())
	print(str(res))
	return res
	
