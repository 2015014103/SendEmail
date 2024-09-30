# 邮件发送器

这是一个使用 Flask 后端的邮件发送器应用。

## 本地设置

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 创建 `config.ini` 文件并填写以下内容：
   ```ini
   [SMTP]
   server = your_smtp_server
   port = your_smtp_port
   username = your_email
   password = your_email_password
   sender_email = your_email
   ```

3. 运行应用：
   ```bash
   python app.py
   ```

## Vercel 部署

1. 在 GitHub 上创建一个新的仓库，并将项目文件推送到该仓库。
2. 在 Vercel 上注册账户并连接您的 GitHub 账户。
3. 在 Vercel 中创建一个新项目，选择您的 GitHub 仓库。
4. 在 Vercel 的环境变量设置中添加以下变量：
   - SMTP_SERVER
   - SMTP_PORT
   - SMTP_USERNAME
   - SMTP_PASSWORD
   - SENDER_EMAIL
5. 部署完成后，您将获得一个可访问的 URL。

## 使用

1. 访问应用 URL（本地或 Vercel 部署的 URL）。
2. 填写收件人邮箱、邮件主题和内容。
3. 点击"发送邮件"按钮。
4. 等待发送结果提示。

## 注意事项

- 确保您的 SMTP 服务器允许应用程序访问。
- 对于 Gmail，您可能需要启用"不太安全的应用程序访问"或使用应用程序密码。
- 在生产环境中，建议使用环境变量而不是配置文件来存储敏感信息。