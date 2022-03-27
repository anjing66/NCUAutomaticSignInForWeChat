import requests
import json
import smtplib
from email.mime.text import MIMEText
import time

header = {
    'Host': 'jc.ncu.edu.cn',
    'Origin': 'http://jc.ncu.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63060012)',
    'token': ''
}
cookies = {
    'ncu_rygk_work_weixin_token': '',
    'ncu_rygk_work_weixin_userData': ''
}
NowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
msg_from = ''
msg_to = ''
subject = '今日打卡情况'
content = ''
password = ''
s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
dataDict = {
    'inChina': '是',
    'addressProvince': '江西省',
    'addressCity': '南昌市',
    'temperatureStatus': '正常',
    'temperature': '0',
    'isIll': '否',
    'closeHb': '否',
    'closeIll': '否',
    'healthDetail': '无异常',
    'isIsolation': '否',
    'isolationPlace': '无',
    'userId': '',
    'addressInfo': '',
    'isGraduate': '否',
    'healthStatus': '无异常',
    'isIsolate': '否',
    'isolatePlace': '无'
}


def send_email(content):
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s.connect("smtp.qq.com")
        s.login(msg_from, password)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("邮件发送成功-->" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except:
        print("发送失败-->" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    finally:
        s.quit()


# r  = requests.post('http://jc.ncu.edu.cn/gate/visitor/getVerifyDept', headers=header)
# time.sleep(1)
# s  = requests.post('http://jc.ncu.edu.cn/gate/user/isSchoolCounsellor', headers=header, cookies=cookies)
# time.sleep(3)
# p = requests.get('http://jc.ncu.edu.cn/system/auth/getTicket?url=http%3A%2F%2Fjc.ncu.edu.cn%2F%3Fcode%3D7FSabGWfS0nomaBddPXh2WHsuUHU3wiJ4x8TVbk-qtY%26state%3DSTATE',headers=header,cookies=cookies)
# time.sleep(3)
def send_data_to_school_server():
    global d
    try:
        d = requests.post('http://jc.ncu.edu.cn/gate/student/signIn', headers=header, cookies=cookies, data=dataDict)
        if d.status_code == 200 and json.loads(d.text)['message'] == '打卡成功':
            print(f'打卡成功({NowTime})')
            send_email(f'云服务端自动打卡成功({NowTime})')
            return True
    except Exception as e:
        return e
    return d.text


for i in range(0, 4):
    returnData = send_data_to_school_server()
    if returnData == True:
        break
    if i == 0:
        send_email(f'云服务端自动打卡失败，返回数据为{returnData}({NowTime})。20分钟后将再次进行打卡(将尝试3次，期间打卡成功自动结束)')
    elif i == 3:
        send_email(f'第3次云服务端自动打卡失败，返回数据为{returnData}({NowTime})。3次尝试打卡结束，请前往小程序手动打卡')
        break
    else:
        send_email(f'第{i}次尝试云服务端自动打卡失败，返回数据为{returnData}({NowTime})')
    time.sleep(1200)
