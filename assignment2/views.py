from django.shortcuts import redirect

def login_redirect(request):
    return redirect('todo_list/login')