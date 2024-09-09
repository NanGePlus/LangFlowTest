# 使用API接口进行调用
import requests
import json
import logging

from langchain_experimental.llms.anthropic_functions import prompt

# 设置日志模版
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 1、模型相关配置
# # 本地模型模型相关配置 根据自己的实际情况进行调整
# MODEL_API_BASE = "http://192.168.2.9:11434"
# # qwen2:latest  llama3.1:latest  gemma2:latest
# MODEL_CHAT_MODEL = "qwen2:latest"
# MODEL_Embedding_MODEL = "nomic-embed-text:latest"

# # 2、prompt相关配置  引入外部的文件内容
# prompt_file_path = "prompt_template.txt"
# with open(prompt_file_path, 'r', encoding='utf-8') as file:
#     PROMPT_TEMPLATE_TXT = file.read()

# 3、API请求相关配置  根据自己的实际情况进行调整
url = "http://127.0.0.1:7860/api/v1/run/ragtest"
headers = {"Content-Type": "application/json"}


# 4、构造测试消息体
input_text = "张三九有哪些生活方式和习惯"
# input_text = "张三九的工作是什么以及工作场所是在哪里"
# input_text = "张三九的配偶是谁以及其联系方式"
# input_text = "给李四六的健康建议是什么"
# input_text = "LangChain是什么，详细介绍下?"

data = {
    "input_value": input_text,
    "output_type": "chat",
    "input_type": "chat",
    "tweaks": {
        "ChatInput-3pLIH": {
            "files": "",
            # "input_value": "张三九的配偶是谁以及其联系方式",
            "sender": "User",
            "sender_name": "User",
            "session_id": "",
            "should_store_message": True
        },
        "ParseData-NEXx5": {
            "sep": "\n",
            "template": "{text}"
        },
        "Prompt-6wckX": {
            "context": "",
            "template": "你是一个针对健康档案进行问答的机器人。\n你的任务是根据下述给定的已知信息回答用户问题。\n\n已知信息:\n{context}\n\n用户问：\n{query}\n\n如果已知信息不包含用户问题的答案，或者已知信息不足以回答用户的问题，请直接回复\"我无法回答您的问题\"。\n请不要输出已知信息中不包含的信息或答案。\n请不要输出已知信息中不包含的信息或答案。\n请不要输出已知信息中不包含的信息或答案。\n请用中文回答用户问题。",
            "query": ""
        },
        "ChatOutput-xlwjc": {
            "data_template": "{text}",
            # "input_value": "",
            "sender": "Machine",
            "sender_name": "AI",
            "session_id": "",
            "should_store_message": True
        },
        "OpenAIModel-vYDNH": {
            "api_key": "sk-XmrIEFplNArLlYa0E8C5A7C5F82041FdBd923e9d115746D0",
            # "input_value": "",
            "json_mode": False,
            "max_tokens": None,
            "model_kwargs": {},
            "model_name": "gpt-4o-mini",
            "openai_api_base": "https://api.wlai.vip/v1",
            "output_schema": {},
            "seed": 1,
            "stream": False,
            "system_message": "",
            "temperature": 0.1
        },
        "Chroma-cRb29": {
            "allow_duplicates": False,
            "chroma_server_cors_allow_origins": "",
            "chroma_server_grpc_port": None,
            "chroma_server_host": "",
            "chroma_server_http_port": None,
            "chroma_server_ssl_enabled": False,
            "collection_name": "langflow02",
            "limit": None,
            "number_of_results": 10,
            "persist_directory": "ChromaDB02",
            "search_query": "",
            "search_type": "Similarity"
        },
        "OpenAIEmbeddings-YEiqb": {
            "chunk_size": 1000,
            "client": "",
            "default_headers": {},
            "default_query": {},
            "deployment": "",
            "dimensions": None,
            "embedding_ctx_length": 1536,
            "max_retries": 3,
            "model": "text-embedding-3-small",
            "model_kwargs": {},
            "openai_api_base": "https://api.wlai.vip/v1",
            "openai_api_key": "sk-XmrIEFplNArLlYa0E8C5A7C5F82041FdBd923e9d115746D0",
            "openai_api_type": "",
            "openai_api_version": "",
            "openai_organization": "",
            "openai_proxy": "",
            "request_timeout": None,
            "show_progress_bar": False,
            "skip_empty": False,
            "tiktoken_enable": True,
            "tiktoken_model_name": ""
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



