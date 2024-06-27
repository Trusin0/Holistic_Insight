import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.conf import settings
import backend.models as models

# Create your views here.


# test:hello world
def hello(request):
    response = JsonResponse({'message': 'Hello, World!'})
    return response


def oauth(request):
    # 获取授权码
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'Missing authorization code'}, status=400)

    print(code)
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
    print("asking for token")
    access_token = response_json.get('access_token')
    print(access_token)

    if not access_token:
        return JsonResponse({'error': 'Failed to retrieve access token'}, status=400)

    # 使用访问令牌请求用户信息
    user_info_url = 'https://api.github.com/user'
    auth_headers = {'Authorization': f'token {access_token}'}
    user_response = requests.get(user_info_url, headers=auth_headers)
    user_json = user_response.json()
    username = user_json.get('login')
    print(username)

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
    print(session_key)

    # set cookie in response
    response = JsonResponse({'message': 'Login successful',
                             'username': username})
    response.set_cookie('session_key', session_key)
    
    return response
