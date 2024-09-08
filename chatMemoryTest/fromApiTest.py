# 使用API接口进行调用
import requests
import json
import logging

# 设置日志模版
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 1、模型相关配置
# # openai模型相关配置 根据自己的实际情况进行调整
MODEL_API_BASE = "https://api.wlai.vip/v1"
MODEL_CHAT_API_KEY = "sk-8B451N7cQ7r2QiXh60Df56714bC64678A42597789e53213a"
MODEL_CHAT_MODEL = "gpt-4o-mini"

# oneapi相关配置(通义千问为例) 根据自己的实际情况进行调整
# MODEL_API_BASE = "http://139.224.72.218:3000/v1"
# MODEL_CHAT_API_KEY = "sk-DoU00d1PaOMCFrSh68196328E08e443a8886E95761D7F4Bf"
# MODEL_CHAT_MODEL = "qwen-max"


# 2、prompt相关配置  引入外部的文件内容
sys_file_path = "prompt_template_system.txt"
user_file_path = "prompt_template_user.txt"
with open(sys_file_path, 'r', encoding='utf-8') as file:
    PROMPT_TEMPLATE_TXT_SYS = file.read()
with open(user_file_path, 'r', encoding='utf-8') as file:
    PROMPT_TEMPLATE_TXT_USER = file.read()

# 3、API请求相关配置  根据自己的实际情况进行调整
url = "http://127.0.0.1:7860/api/v1/run/chatMemory"
headers = {"Content-Type": "application/json"}


# 4、构造测试消息体
input_text = "有低于200元的套餐吗"
# input_text = "那给我详细介绍下经济套餐吧"
# input_text = "这个套餐是多少钱"
# input_text = "流量是多少"

data = {
    "input_value": input_text,
    "output_type": "chat",
    "input_type": "chat",
    "tweaks": {
        "OpenAIModel-HXl0Q": {
            "api_key": MODEL_CHAT_API_KEY,
            # "input_value": "",
            "json_mode": False,
            "max_tokens": None,
            "model_kwargs": {},
            "model_name": MODEL_CHAT_MODEL,
            "openai_api_base": MODEL_API_BASE,
            "output_schema": {},
            "seed": 1,
            "stream": False,
            "system_message": "",
            "temperature": 0.1
        },
        "Prompt-jwobs": {
            # "template": "你是一个推荐手机流量套餐的客服代表，你叫NanGe。\n你可以帮助用户选择最合适的流量套餐产品。可以选择的套餐包括：\n经济套餐，月费50元，10G流量；\n畅游套餐，月费180元，100G流量；\n无限套餐，月费300元，1000G流量；\n校园套餐，月费150元，200G流量，仅限在校生。\n\n下面是给你参考的多轮对话的例子：\n例子1:\n客服：有什么可以帮您\n用户：100G套餐有什么\n客服：我们现在有无限套餐，1000G流量，月费300元\n用户：这个套餐是多少钱\n客服：这个套餐是300元\n\n例子2:\n客服：有什么可以帮您\n用户：便宜的套餐有什么\n客服：我们现在有经济套餐，每月50元，10G流量\n用户：100G以上的有什么\n\n例子3:\n客服：有什么可以帮您\n用户：100G以上的套餐有什么\n客服：我们现在有畅游套餐，流量100G，月费180元\n用户：流量最多的呢\n\n例子4:\n客服：有什么可以帮您\n用户：1000元月费的套餐有吗\n客服：没有找到满足1000元价位的产品，是否选择其他套餐\n\n记住：回复时要求你使用口语，亲切一些。不用说“抱歉”。直接给出回答，不用在前面加“NanGe说：”。NO COMMENTS. NO ACKNOWLEDGEMENTS.\n\n"
            "template": PROMPT_TEMPLATE_TXT_SYS
        },
        "Prompt-pzIoo": {
            # "template": "用户问：\n{query}\n\n历史对话内容:\n{content}",
            "template": PROMPT_TEMPLATE_TXT_USER,
            "query": "",
            "content": ""
        },
        "ChatInput-0GC39": {
            "files": "",
            # "input_value": "多大的流量",
            "sender": "User",
            "sender_name": "User",
            "session_id": "",
            "should_store_message": True
        },
        "ChatOutput-VQ5Nb": {
            "data_template": "{text}",
            # "input_value": "",
            "sender": "Machine",
            "sender_name": "AI",
            "session_id": "",
            "should_store_message": True
        },
        "Memory-eI9M7": {
            "n_messages": 100,
            "order": "Ascending",
            "sender": "Machine and User",
            "sender_name": "",
            "session_id": "",
            "template": "{sender_name}: {text}"
        }
    }
}


# 5、发送post请求进行测试
response = requests.post(url, headers=headers, data=json.dumps(data))
# 检查响应状态码
if response.status_code == 200:
    try:
        logger.info(f"输出响应内容是: {response.status_code}\n")
        logger.info(f"输出响应内容是: {response.json()}\n")
        # 解析具体回复的内容
        content = response.json()['outputs'][0]['outputs'][0]['results']['message']['data']['text']
        logger.info(f"输出响应内容是: {content}\n")
    except requests.exceptions.JSONDecodeError:
        # 响应不是JSON格式
        logger.info("Response content is not valid JSON")
else:
    logger.info(f"Request failed with status code {response.status_code}")



