from django.urls import path
from .views import viewClass

urlpatterns = [
    path('',viewClass().page,name='page'),
    path('search',viewClass().search,name='search'),
    path('current',viewClass().search_status,name='current'),
    path('helloworld',viewClass().func2,name='helloworld'),
    path('current',viewClass().search_status,name='current'),
	path('testcase_button',viewClass().func3,name='testcase_BUTTON'),
    path('testcase',viewClass().testcase,name='testcase'),

]