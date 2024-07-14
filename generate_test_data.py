import os
import django
from django.utils import timezone
import random
import string
from datetime import timedelta

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Holistic_Insight.settings')
django.setup()

# 导入模型
from backend.models import Usr, Number, React, Schulte, Session, Sight

# 创建用户
users = []
for i in range(10):  # 创建10个用户
    usr = Usr.objects.create(
        usr_id=i+62442,
        pass_field='pass',
        usr_name=f'User {i}',
        MBTI_type='NULL'
    )
    users.append(usr)

# 创建Number数据
for _ in range(100):
    Number.objects.create(
        usr=random.choice(users),
        level=random.randint(1, 10),
        play_time=timezone.now().date() - timedelta(days=random.randint(0, 365))
    )

# 创建React数据
for _ in range(100):
    React.objects.create(
        usr=random.choice(users),
        react_time=random.uniform(0.1, 5.0),
        play_time=timezone.now().date() - timedelta(days=random.randint(0, 365))
    )

# 创建Schulte数据
for _ in range(100):
    Schulte.objects.create(
        usr=random.choice(users),
        block_size=random.randint(3, 10),
        error_times=random.randint(0, 5),
        cost=random.uniform(0.5, 10.0),
        play_time=timezone.now().date() - timedelta(days=random.randint(0, 365))
    )

# 创建Session数据
for _ in range(10):
    Session.objects.create(
        usr=random.choice(users),
        session_key=''.join(random.choices(string.ascii_letters + string.digits, k=64)),
        expire_time=timezone.now() + timedelta(days=random.randint(1, 30)),
        create_time=timezone.now() - timedelta(days=random.randint(0, 365))
    )

# 创建Sight数据
for _ in range(100):
    Sight.objects.create(
        usr=random.choice(users),
        level=random.randint(1, 10),
        play_time=timezone.now().date() - timedelta(days=random.randint(0, 365))
    )

print("Successfully generated test data")