from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^register', views.register, name='register'),
    url(r'^login', LoginView.as_view(template_name='todo_list/login.html'), name='login'),
    url(r'^home', views.home, name='home'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^add', views.addTodo, name='add'),
    url(r'^toggle/(?P<todo_id>\d+)', views.toggleTodo, name='complete'),
    url(r'^delete/(?P<todo_id>\d+)', views.deleteSelected, name='delete'),
    url(r'^edit/(?P<todo_id>\d+)', views.editTodo, name='edit'),
]