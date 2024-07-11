import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.conf import settings
import backend.models as models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your views here.


# test:hello world
def hello(request):
    cookie = request.COOKIES.get('session_key')
    response = JsonResponse({'cookie': cookie})
    return response


# def check_session(request):
#     cookie = request.COOKIES.get('session_key')
#     response = JsonResponse({'cookie': cookie})
#     return response

def login(request): 
    oauth_url = settings.GITHUB_OAUTH_URL 
    client_id = settings.GITHUB_CLIENT_ID 
    redirect_uri = settings.GITHUB_REDIRECT_URI 
    return JsonResponse({'redirect_url': f'{oauth_url}?client_id={client_id}&redirect_uri={redirect_uri}'})

def logout(request):
    pass

def check_session(request):
    session_key = request.COOKIES.get('session_key')
    print(session_key)
    try:
        session = models.Session.objects.get(session_key=session_key)
        usr = session.usr
        return JsonResponse({'usr_name': usr.usr_name})
    except models.Session.DoesNotExist:
        return JsonResponse({'error': 'Session not found'}, status=404)
    except models.Session.MultipleObjectsReturned:
        return JsonResponse({'error': 'Multiple sessions with the same key'}, status=500)
    

def get_login_status(request):
    session_key = request.COOKIES.get('session_key')
    login_status = {'is_login': False,
                    'session_status': 'invalid',
                    'usr_name': None,
                    'usr_id': None,}
    
    if session_key:
        try:
            session = models.Session.objects.get(session_key=session_key)
            if session.expire_time > timezone.now():
                login_status['is_login'] = True
                login_status['session_status'] = 'valid'
                login_status['usr_name'] = session.usr.usr_name
                login_status['usr_id'] = session.usr.usr_id
        except Exception as e:
            login_status['error'] = str(e)

    return JsonResponse(login_status)


def save_game_data(request):
    # other logic
    # ...
    # other logic

    game_name = request.GET.get('game_name')
    # call the corresponding save function
    if game_name == 'schulte':
        return schulte_save(request)
    elif game_name == 'react':
        return react_save(request)
    

def react_save(request):
    try:
        # 测试时使用GET请求
        print(request.GET)
        react_time = float(request.GET.get('react_time'))
        play_time = request.GET.get('play_time')
        usr_name = request.GET.get('usr_name')
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    try:
        user = models.Usr.objects.get(usr_name=usr_name)
    except models.Usr.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

        # 确认 play_time 是时间戳，并将其转换为整数
    timestamp = int(play_time)

    # 将时间戳转换为秒（通常时间戳是毫秒）
    timestamp /= 1000

    # 将时间戳转换为 datetime 对象
    play_time_dt = datetime.fromtimestamp(timestamp)

    # 将 datetime 对象转换为日期字符串
    formatted_play_time = play_time_dt.strftime('%Y-%m-%d')
    print(formatted_play_time)

    react = models.React(usr=user, react_time=react_time, play_time=formatted_play_time)
    try:
        react.save()
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'message': 'Save successful'})

def schulte_save(request):
    try:
        # 测试时使用GET请求
        print(request.GET)
        block_size = int(request.GET.get('block_size'))
        error_times = int(request.GET.get('error_times'))
        cost = float(request.GET.get('cost'))
        play_time = request.GET.get('play_time')
        usr_name = request.GET.get('usr_name')
        print('Parse request success!')
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    try:
        user = models.Usr.objects.get(usr_name=usr_name)
        print('user get success!')
    except models.Usr.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    # 确认 play_time 是时间戳，并将其转换为整数
    timestamp = int(play_time)

    # 将时间戳转换为秒（通常时间戳是毫秒）
    timestamp /= 1000

    # 将时间戳转换为 datetime 对象
    play_time_dt = datetime.fromtimestamp(timestamp)

    # 将 datetime 对象转换为日期字符串
    formatted_play_time = play_time_dt.strftime('%Y-%m-%d')
    print(formatted_play_time)

    schulte = models.Schulte(usr=user, block_size=block_size, error_times=error_times, cost=cost, play_time=formatted_play_time)

    # schulte = models.Schulte(usr=user, block_size=block_size, error_times=error_times, cost=cost)
    print('schulte get success!')
    try:
        schulte.save()
        print('Schulte save successful!')
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'message': 'Save successful'})




def oauth(request):
    # 获取授权码
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'Missing authorization code'}, status=400)

    # 请求访问令牌
    token_url = 'https://github.com/login/oauth/access_token'
    payload = {
        'client_id': settings.GITHUB_CLIENT_ID,
        'client_secret': settings.GITHUB_CLIENT_SECRET,
        'code': code,
        'state': request.GET.get('state')  # Optional: Verify the state parameter if you use it
    }
    headers = {'Accept': 'application/json'}
    response = requests.post(token_url, data=payload, headers=headers)
    response_json = response.json()
    access_token = response_json.get('access_token')

    if not access_token:
        return JsonResponse({'error': 'Failed to retrieve access token'}, status=400)

    # 使用访问令牌请求用户信息
    user_info_url = 'https://api.github.com/user'
    auth_headers = {'Authorization': f'token {access_token}'}
    user_response = requests.get(user_info_url, headers=auth_headers)
    user_json = user_response.json()
    username = user_json.get('login')

    if not username:
        return JsonResponse({'error': 'Failed to retrieve username'}, status=400)

    # 下面进入创建用户或登录用户的逻辑

    # check if user exists
    try:
        user = models.Usr.objects.get(usr_name=username)
    except models.Usr.DoesNotExist:
        # create
        user = models.Usr(usr_name=username)
        user.save()
    except models.Usr.MultipleObjectsReturned:
        # theoretically impossible
        return JsonResponse({'error': 'Multiple users with the same username'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    # create session
    session_key = user.create_session()
    response = redirect('/#/index')
    # set cookie in response
    response.set_cookie('session_key', session_key,max_age=604800)
    
    return response
