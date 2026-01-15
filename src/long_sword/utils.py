import json
import msvcrt
import os
import shutil
import time
from dataclasses import dataclass
from typing import Any


# -------------------------------------------------------------
# 通用结果封装
# -------------------------------------------------------------
@dataclass
class Result:
    success: bool
    data: Any | None = None
    error: str | None = None

    @staticmethod
    def ok(data: Any = None) -> "Result":
        return Result(success=True, data=data)

    @staticmethod
    def fail(error: str) -> "Result":
        return Result(success=False, error=error)


def is_valid_text_file(file_path):
    """
    判断文件是否是文本类型
    @param file_path:
    @return:
    """
    try:
        # 尝试以文本模式打开文件并读取一些内容
        with open(file_path, encoding="utf-8") as f:
            # 读取
            content = f.read()
        if content.strip():
            # 如果读取成功，且内容包含文本，则返回 True
            # 空文件或只含空白文本的文件不算文本文件
            return True
        return False
    except Exception as e:
        # 发生异常，可能是因为文件不是文本文件或者无法被正确读取
        return False


def is_valid_code_file(file_path):
    """
    判断文件是否是有效的代码文件
    @return:
    """
    if any(file_path.endswith(ext) for ext in auxiliary_extensions):
        return False
    if not is_valid_text_file(file_path):
        return False
    if os.path.basename(file_path).startswith("."):
        return False
    return True


comment_sign_list = {
    ".c": "// ❓",
    ".h": "// ❓",
    ".cpp": "// ❓",
    ".cc": "// ❓",
    ".cxx": "// ❓",
    ".C": "// ❓",
    ".c++": "// ❓",
    ".cs": "// ❓",
    ".java": "// ❓",
    ".py": "# ❓",
    ".pyi": "# ❓",
    ".html": "<!-- ❓ -->",
    ".xml": "<!-- ❓ -->",
    ".sevelet": "<!-- ❓ -->",
    ".css": "/* ❓ */",
    ".scss": "/* ❓ */",
    ".js": "// ❓",
    ".sql": "-- ❓",
    ".vb": "' ❓",
    ".asm": "; ❓",
    ".pl": "# ❓",
    ".m": "% ❓",
    ".r": "# ❓",
    ".rs": "// ❓",
    ".sh": "# ❓",
    ".proto": "// ❓",
    ".rst": ".. ❓",
    ".bat": "@REM ❓",
    ".nsi": "; ❓",
    ".nsh": "; ❓",
    ".nsh": "; ❓",
    ".lock": "# ❓",
    ".bzl": "# ❓",
    ".in": "# ❓",
    ".cfg": "# ❓",
    ".tex": "% ❓",
    ".ts": "// ❓",
    ".env": "; ❓",
    ".mjs": "// ❓",
    ".kt": "// ❓",
    ".aidl": "// ❓",
}

auxiliary_extensions = [
    ".md",
    ".properties",
    ".xml",
    ".yaml",
    ".ui",
    ".config",
    ".ipynb_checkpoints",
    ".DS_Store",
    ".idea",
    ".txt",
    ".env",
    ".json",
    # '.toml',
    ".scss",
    "LICENSE",
    "CONTRIBUTORS",
    ".svg",
    ".pdf",
]


def get_input_in_one_second(timeout=0.5):
    """
    获取一秒钟内的用户输入。只在windows Terminal中有效，在pyCharm Terminal中无效
    """
    start_time = time.time()
    _input = ""
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getch().decode("utf-8")
            if char == "\r":  # 如果输入回车键，结束输入
                break
            _input += char
        if (time.time() - start_time) > timeout:
            break
    return _input


def list_extensions(folder_path):
    """
    辅助开发，用于列出所有后缀名
    """
    # 用于存储后缀名的集合
    extensions = set()
    # 遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 分离文件名和后缀名
            ext = os.path.splitext(file)[1]
            # 添加到集合中
            extensions.add(ext)
    # 返回后缀名列表
    return list(extensions)


if __name__ == "__main__":
    # 指定要遍历的文件夹路径
    folder_path = "D:\\git_1"
    # 获取后缀名列表
    extensions = list_extensions(folder_path)
    # 打印所有不同的后缀名
    print(extensions)
