from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import os
from datetime import datetime
import logging
import requests
from werkzeug.middleware.proxy_fix import ProxyFix  # 添加这行


app = Flask(__name__)

# 添加代理支持 - 在应用定义后立即添加
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)
# 配置日志
LOG_FILE = 'ai_conversations.log'

# API配置
API_CONFIG = {
    'url': "https://maas-cn-southwest-2.modelarts-maas.com/v1/infers/271c9332-4aa6-4ff5-95b3-0cf8bd94c394/v1/chat/completions",
    'key': "YUT5g-tg7_9iJk4w6frKZYq4EHhSU7D7EMZ4Z23NQcZ9nmIp9ZpvsgInlah7FQaIhJZuhWCRwtIJZU9iXxlYpw"
}


def setup_logging():
    """设置日志配置"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )


def log_conversation(user_message, ai_response, user_ip=None, api_data=None):
    """记录对话到日志文件"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = {
        'timestamp': timestamp,
        'user_ip': user_ip or 'unknown',
        'user_message': user_message,
        'ai_response': ai_response,
        'api_data': api_data  # 记录API请求和响应数据
    }

    # 记录到文件
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')

    # 同时使用logging记录
    logging.info(f"用户消息: {user_message}")
    logging.info(f"AI回复: {ai_response}")
    if api_data:
        logging.info(f"API状态码: {api_data.get('status_code')}")
        logging.info(f"Token使用: {api_data.get('usage', {})}")
    logging.info("-" * 50)


def call_ai_api(user_message, conversation_history):
    """调用实际的AI API"""
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_CONFIG["key"]}'
        }

        # 构建消息历史
        messages = [
            {"role": "system", "content": "你是一个乐于助人的AI助手。"}
        ]
        messages.extend(conversation_history)
        messages.append({"role": "user", "content": user_message})

        data = {
            "model": "DeepSeek-V3",
            "messages": messages
        }

        # 发送请求
        response = requests.post(
            API_CONFIG["url"],
            headers=headers,
            data=json.dumps(data),
            verify=False
        )

        api_data = {
            'status_code': response.status_code,
            'request_data': data
        }

        if response.status_code == 200:
            result = response.json()
            ai_response = result['choices'][0]['message']['content']
            api_data['usage'] = result.get('usage', {})
            api_data['response_id'] = result.get('id')
            return ai_response, api_data
        else:
            error_msg = f"API错误: {response.status_code} - {response.text}"
            return error_msg, api_data

    except Exception as e:
        error_msg = f"API调用异常: {str(e)}"
        return error_msg, None


# ========== 主要页面路由 ==========

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/case/')
def case():
    return render_template('case.html')


@app.route('/service/')
def service():
    return render_template('service.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/news/')
def news():
    return render_template('news.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


# ========== 案例详情页路由 ==========

@app.route('/ethiotelecomcloud/')
def ethiotelecomcloud():
    return render_template('ethiotelecomcloud.html')

@app.route('/xg/')
def xg():
    return render_template('xg.html')

@app.route('/southwest/')
def southwest():
    return render_template('southwest.html')

@app.route('/eerduosi/')
def eerduosi():
    return render_template('eerduosi.html')

@app.route('/sanxia/')
def sanxia():
    return render_template('sanxia.html')

@app.route('/shenzhenjichang/')
def shenzhenjichang():
    return render_template('shenzhenjichang.html')
@app.route('/insight/')
def insight():
    return render_template('insight.html')

# ========== 新闻详情页路由 ==========

@app.route('/20250702/')
def news_20250702():
    return render_template('20250702.html')


@app.route('/20250626/')
def news_20250626():
    return render_template('20250626.html')


@app.route('/20250625/')
def news_20250625():
    return render_template('20250625.html')


@app.route('/20250624/')
def news_20250624():
    return render_template('20250624.html')


@app.route('/20250621/')
def news_20250621():
    return render_template('20250621.html')


@app.route('/20250620/')
def news_20250620():
    return render_template('20250620.html')


@app.route('/20250612/')
def news_20250612():
    return render_template('20250612.html')


@app.route('/20250604/')
def news_20250604():
    return render_template('20250604.html')


@app.route('/20250529/')
def news_20250529():
    return render_template('20250529.html')


# ========== 案例页面路由 ==========

@app.route('/mnft/')
def mnft():
    return render_template('mnft.html')


@app.route('/gonc/')
def gonc():
    return render_template('gonc.html')


@app.route('/smarthealthcare/')
def smarthealthcare():
    return render_template('smarthealthcare.html')


@app.route('/bank/')
def bank():
    return render_template('bank.html')


@app.route('/car/')
def car():
    return render_template('car.html')


# ========== MaaS 相关路由 ==========

@app.route('/maas/')
def maas_page():
    """MaaS主页面 - 集成聊天界面"""
    return render_template('maas.html')


@app.route('/api/maas/chat', methods=['POST'])
def maas_chat():
    """处理AI聊天请求并记录日志"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        conversation_history = data.get('history', [])
        user_ip = request.remote_addr

        if not user_message:
            return jsonify({'error': '消息不能为空'}), 400

        # 调用实际的AI API
        ai_response, api_data = call_ai_api(user_message, conversation_history)

        # 记录对话到日志
        log_conversation(user_message, ai_response, user_ip, api_data)

        return jsonify({
            'success': True,
            'response': ai_response
        })

    except Exception as e:
        error_msg = f"处理请求时出错: {str(e)}"
        logging.error(error_msg)
        return jsonify({'error': error_msg}), 500


# ========== 日志查看路由 ==========

@app.route('/api/maas/logs')
def get_conversation_logs():
    """获取对话日志（可选功能，用于查看日志）"""
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                logs = [json.loads(line) for line in f.readlines() if line.strip()]
            return jsonify({'logs': logs[-50:]})  # 返回最近50条记录
        else:
            return jsonify({'logs': []})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ========== 静态文件路由 ==========

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')


# ========== 错误处理  ==========

@app.errorhandler(404)
def page_not_found(e):
    return "页面未找到", 404


@app.errorhandler(500)
def internal_server_error(e):
    return "服务器内部错误", 500


if __name__ == "__main__":
    setup_logging()
    print(f"对话日志将保存到: {os.path.abspath(LOG_FILE)}")
    app.run(debug=True, host='0.0.0.0', port=1626)
