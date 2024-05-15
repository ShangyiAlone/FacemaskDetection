from flask import Flask, request, jsonify
import sqlite3
import sendEmail

app = Flask(__name__)

# 连接到 SQLite 数据库
conn = sqlite3.connect('database.db',check_same_thread=False)
cursor = conn.cursor()

global code
code = ''

@app.route('/login', methods=['POST'])
def login():
    # 定义查询语句
    query = "SELECT username, password,level FROM users"
    # 执行查询
    cursor.execute(query)
    # 获取所有结果
    rows = cursor.fetchall()
    # 将结果转换为字典
    users = {username: (password, level) for username, password, level in rows}

    data = request.json

    username = data.get('username')
    password = data.get('password')


    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    if username not in users or users[username][0] != password:
        return jsonify({'error': 'Invalid username or password'}), 401

    return jsonify({'message': 'Login successful'}), 200

@app.route('/send_code', methods=['POST'])
def send_verification_code():
    try:
        data = request.get_json()
        email = data.get('email')
        global code
        result,code = sendEmail.mail(email)
        print(result,code)
    except Exception:
        return result
    response = {
        'code': 1 if code!='' else 0
    }
    return response


@app.route('/register', methods=['POST'])
def register():
    print(request)
    # 从请求中获取姓名、密码和邮箱
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # 校验验证码
    global code
    print(code,data.get('code'))
    if code!=data.get('code'):
        return {'code': 0}

    print(username, password,0, email)

    # 将用户信息插入数据库
    cursor.execute("INSERT INTO users (username, password,level ,email) VALUES (?, ?, ?, ?)", (username, password,0, email))
    conn.commit()

    response = {
        'message': 'User registered successfully!',
        'username': username,
        'email': email,
        'code': 1
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

