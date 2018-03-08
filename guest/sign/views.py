from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')  # username为form <input>name属性，如何参数没有提交，返回一个空字符串
        password = request.POST.get('password', '')
        '''接下来用的是Django自带的认证系统'''
        user = auth.authenticate(username=username,
                                 password=password)  # authenticate()认证给出的用户名跟密码，正确返回一个user对象，不正确返回None
        if user is not None:
            auth.login(request, user)  # 调用Django自带的认证系统的login()
            request.session['user'] = username
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


@login_required  # 限制视图必须登录才能访问
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request, 'event_manage.html', {'user': username, 'events': event_list})


def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    search_name_bytes = search_name.encode(encoding="utf-8")
    event_list = Event.objects.filter(name__contains=search_name_bytes)
    return render(request, "event_manage.html", {"user": username, "events": event_list})


def guest_manage(request):
    guest_list = Guest.objects.all()
    username = request.session.get('username', '')
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})


def search_phone(request):
    username = request.session.get('user', '')
    search_phone = request.GET.get("phone", "")
    search_name_bytes = search_name.encode(encoding="utf-8")
    guest_list = Guest.objects.filter(phone__contains=search_name_bytes)
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})


@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response


@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})


@login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    #    guest_list = Guest.objects.filter(event_id=event_id)
    #    sign_list = Guest.objects.filter(sign="1", event_id=event_id)
    #    guest_data = str(len(guest_list))
    #    sign_data = str(len(sign_list))

    phone = request.POST.get('phone', '')

    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'phone error.'})

    result = Guest.objects.filter(phone=phone, event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.'})

    result = Guest.objects.get(event_id=event_id, phone=phone)

    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': "user has sign in."})
    else:
        Guest.objects.filter(event_id=event_id, phone=phone).update(sign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success!', 'guest': result,
                                                   })
