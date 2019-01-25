# 使用redis统计活跃用户

import redis
from datetime import datetime


ACCOUNT_ACTIVE_KEY = 'account:active'
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.flushall()
now = datetime.utcnow()

def record_active(account_id, t=None):
	if t is None:
		t = datetime.utcnow()
	p = r.pipeline()
	key = ACCOUNT_ACTIVE_KEY
	for arg in ('year', 'month', 'day'):
		key = '{}:{}'.format(key, getattr(t, arg))
		p.setbit(key, account_id, 1)  # 设置年月日三种键
	p.execute()


def gen_records(max_days, population, k):
	"""
	随机生成一些数据
	population: 总用户数
	k: 登陆用户数
	"""
	for day in range(1, max_days):
		time_ = datetime(now.year, now.month, day)
		accounts = random.sample(range(population), k)
		for account_id in accounts:
			record_active(account_id, time_)
