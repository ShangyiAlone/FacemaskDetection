# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import random

my_sender = '3371860357@qq.com'  # 填写发信人的邮箱账号
my_pass = 'xhhxpdqabhagdagc'  # 发件人邮箱授权码
my_user = '804343808@qq.com'  # 收件人邮箱账号

def mail(email):
    ret = True
    my_user = email
    random_numbers = "".join([str(random.randint(0, 9)) for _ in range(4)])
    code = random_numbers
    try:
        msg = MIMEText(random_numbers, 'plain', 'utf-8')  # 填写邮件内容
        msg['From'] = formataddr(["晓宜工作室", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["test", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "口罩识别系统验证码"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:
        ret = False
    return ret,code


