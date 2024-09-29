from flask import Flask, render_template, request, flash
import smtplib
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置一个秘钥用于flash消息

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

# 获取邮件配置
smtp_server = config['SMTP']['server']
smtp_port = config['SMTP']['port']
smtp_username = config['SMTP']['username']
smtp_password = config['SMTP']['password']
sender_email = config['SMTP']['sender_email']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        receiver_email = request.form['receiver_email']
        subject = request.form['subject']
        body = request.form['body']

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, int(smtp_port), context=context) as server:
                server.set_debuglevel(1)  # 启用调试模式
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                try:
                    server.quit()
                except smtplib.SMTPServerDisconnected:
                    pass  # 忽略服务器断开连接的错误
            flash('邮件发送成功!', 'success')
        except smtplib.SMTPAuthenticationError:
            flash('认证失败，请检查用户名和密码', 'error')
        except smtplib.SMTPException as e:
            if str(e) == "(-1, b'\\x00\\x00\\x00')":
                flash('邮件发送成功!', 'success')  # 将这种特殊情况视为成功
            else:
                flash(f'发送邮件时出现问题: {e}', 'error')
        except ssl.SSLError as e:
            flash(f'SSL错误: {e}', 'error')
        except Exception as e:
            if str(e) == "(-1, b'\\x00\\x00\\x00')":
                flash('邮件发送成功!', 'success')  # 将这种特殊情况视为成功
            else:
                flash(f'发送邮件时出错: {e}', 'error')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)