import logging
from openai import OpenAI
import httpx
from dotenv import load_dotenv
import os

# -------------------------
# 初始化 logger
# -------------------------
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# -------------------------
# 加载环境变量
# -------------------------
load_dotenv("D:/utils/long_sword/src/long_sword/.env")

# -------------------------
# 构建客户端配置
# -------------------------
client_kwargs = {
    "api_key": os.getenv("OPENAI_API_KEY"),
    "base_url": os.getenv("BASE_URL"),
}

# 代理适配
proxy = os.getenv("PROXY")
if proxy:
    client_kwargs["http_client"] = httpx.Client(proxy=proxy)
    logger.info(f"使用代理: {proxy}")

client = OpenAI(**client_kwargs)


def ask_openai(prompt:str) -> str|None:
    """
    """
    response = client.chat.completions.create(
        model=str(os.getenv("MODEL", "gemini-2.0-flash")),
        messages=[{"role": "user", "content": prompt}],
    )

    content = response.choices[0].message.content
    return content
