'''
Created on 2013/09/16

@author: samuraitaiga
'''
# -*- coding: utf-8 -*-

from django.http import HttpResponse

def demo_test(request):
    return HttpResponse("test success")
