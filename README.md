# coc template for django
coc(convention over configuration)

## Requirements
* django 1.4 or higher

## URL and method bind rules
* last part of url is a method 
* part of url other than last one is a package name
* examples:
    * sample1 : http://<server name>/api/test/show
        * package name : coc.views.api.test
        * method : show
    * sample2 : http://<server name>/api/list
        * package name : coc.views.api
        * method : list

## How to use
* write your own app and store it into coc/views
* run django app
    * exp: python manage.py runserver
* access app from browser

## Samples
* sample view is stored in coc/views/test.py. run django app and access to http://<server name>/test/demo_test. you can see 'test success' message.
