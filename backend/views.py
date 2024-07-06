import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.conf import settings
import backend.models as models
from django.utils import timezone

# Create your views here.


# test:hello world
def hello(request):
    response = JsonResponse({'message': 'Hello, World!'})
    return response

def login(request):
    oauth_url = settings.GITHUB_OAUTH_URL
    client_id = settings.GITHUB_CLIENT_ID
    redirect_uri = settings.GITHUB_REDIRECT_URI
    return redirect(f'{oauth_url}?client_id={client_id}&redirect_uri={redirect_uri}')

def logout(request):
    pass

def schulte_save(request):
    try:
        # 测试时使用GET请求
        print(request.GET)
        block_size = int(request.GET.get('block_size'))
        error_times = int(request.GET.get('error_times'))
        cost = float(request.GET.get('cost'))
        play_time = request.GET.get('play_time')
        usr_name = request.GET.get('usr_name')
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    try:
        user = models.Usr.objects.get(usr_name=usr_name)
    except models.Usr.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
    schulte = models.Schulte(usr=user, block_size=block_size, error_times=error_times, cost=cost, play_time=play_time)
    try:
        schulte.save()
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
    response = JsonResponse({'message': 'Login successful',
                             'username': username,
                             'id': user.usr_id,
                             'respCode': '000000',
                             'session_key': session_key})
    # set cookie in response
    # response.set_cookie('session_key', session_key)
    
    return response
