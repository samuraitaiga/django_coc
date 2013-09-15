# -*- coding: utf-8 -*-
from django.http import HttpResponse
import sys

BASE_CLASS = 'coc.views'

def get_view_method(request, url):
    def get_package_name(splitted_package_name_list):
        package_name = BASE_CLASS
        for splitted_package_name in splitted_package_name_list:
            package_name = '.'.join((package_name, splitted_package_name))
        return package_name
    
    splitted_url = url.split('/')
    package_name = get_package_name(splitted_url[:-1])
    method_name = str(splitted_url[-1])
    
    __import__(package_name)
    view_method = getattr(sys.modules[package_name], method_name)

    return view_method(request)

def dispatch(request, **kwargs):    
    if 'url' in kwargs:
        result = get_view_method(request, kwargs['url'])
        return result
    else:
        return HttpResponse('404 not found')
