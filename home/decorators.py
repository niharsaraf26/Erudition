from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group

'''def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            query_set = Group.objects.filter(user = request.user)


            if query_set[0].name == "student":
                    return view_func(request, *args, **kwargs)
            else:
                return redirect('t_homepage')
        return wrapper_func
    return decorator'''

def admin_only(view_func):
    def wrapper_func(request , *args, **kwargs):
        group = None
        if request.user.groups.exists():
            groups = Group.objects.filter(user = request.user)

        if request.user.groups[0].name == 'teacher':
            return redirect('t_homepage')

        if group == 'student':
            return view_func(request, *args, **kwargs)

        else:
            return HttpResponse("bhag bsdk")

    return wrapper_func
