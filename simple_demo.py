# -*- coding: utf-8 -*-

import xinge_push
import json

from xinge_push import Message, constant, Style, ClickAction, TimeInterval, MessageIOS
from xinge_push import XingeApp

# 信鸽推送demo

# 推送单个安卓设备
xinge_push.PushTokenAndroid('accessId', 'secretKey', 'title', 'content', 'token')

# 推送到安卓单个账号
xinge_push.PushAccountAndroid(000, "myKey", "标题", "大家好!", "nickName")

# 推送给所有安卓设备
xinge_push.PushAllAndroid(000, "myKey", "标题", "大家好!")

# 安卓推送给标签选中设备
xinge_push.PushTagsAndroid(000, "myKey", "标题", "大家好!", "beijing")

# ios推送给单个设备
xinge_push.PushTokenIos(000, "myKey", "你好!", "3dc4gcd98sdc", xinge_push.ENV_PROD)

# ios推送单个账号
xinge_push.PushAccountIos(000, "myKey", "你好", "nickName", xinge_push.ENV_PROD)

#ios推送所有设备
xinge_push.PushAllIos(000, "myKey", "大家好!", xinge_push.ENV_PROD)

# ios推送给标签选中设备
xinge_push.PushTagsIos(000, "myKey", "大家好!", "beijing", xinge_push.ENV_PROD)

# 推送的时间闭区间
accept_time = xinge_push.TimeInterval(0, 0, 23, 59)

# 消息点击事件
action = xinge_push.ClickAction()
action.actionType = xinge_push.ClickAction.TYPE_ACTIVITY
action.url = 'http://www.yimeijian.cn'

# 定义消息如何展现
style = xinge_push.Style(0, 1, 1, 0)    # 依次为 builderId,ring,vibrate,clearable,nId

# 定义通用推送消息
mess = Message()
mess.type = constant.MESSAGE_TYPE_ANDROID_NOTIFICATION
mess.title = "title"
mess.content = "中午"
mess.expireTime = 86400
#含义:样式编号0,响铃,震动,不可从通知栏清除
mess.style = Style(0,1,1,0)
action = ClickAction()
action.actionType = ClickAction.TYPE_URL
action.url = "http://xg.qq.com"
mess.custom = {'key1':'value1', 'key2':'value2'}
t1 = TimeInterval(12, 0, 13, 59)
t2 = TimeInterval(19, 0, 20, 59)
mess.acceptTime = (t1, t2)

# ios 推送消息
mess = MessageIOS()
mess.expireTime = 86400
mess.alert = "ios test"
mess.badge = 1
mess.sound = "beep.wav"
mess.custom = {'key1':'value1', 'key2':'value2'}
t1 = TimeInterval(0, 0, 23, 59)
mess.acceptTime = (t1,)
raw = {
"aps" : {
"sound" : "beep.wav",
"alert" : "ios test",
"badge" : 1,
"content-available" : 1
}
}
mess.raw = json.dumps(raw)

# 注册app
push = XingeApp('accessId', 'secretKey')
mess = Message()  # or mess = MessageIos()
# 推送消息给单个设备
ret = push.PushSingleDevice('token', mess)
# 推送给单个账户或别名
ret2 = push.PushSingleDevice('token', mess)
# 推送给单个app的所有设备
ret3 = push.PushAllDevices(0, mess)
# 推送给tags指定设备
ret4 = push.PushTags(0, ('1', '2'), 'AND', mess)
# 推送大批量消息
ret5 = push.CreateMultipush(mess)
# 推送消息给大批量账号
push_id = ret5[2]
ret6 = push.PushAccountListMultiple(push_id, ('1', '2'))

# 查询群发状态
q1 = push.QueryPushStatus(('1', '2'))
# 查询应用覆盖设备数
q2 = push.QueryDeviceCount()
# 查询应用tags
q3 = push.QueryTags(0, 100)
# 取消尚未推送的定时消息
c1 = push.CancelTimingPush('111')
# 查询tags绑定的设备数
q4 = push.QueryTagTokenNum('beijing')
# 查询account绑定的token
q5 = push.QueryTokensOfAccount('account')
# 删除account绑定的token
push.DeleteAllTokensOfAccount('account')
push.DeleteTokenOfAccount('account', 'token')