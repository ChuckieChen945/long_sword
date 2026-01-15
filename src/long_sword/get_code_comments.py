from pathlib import Path

from long_sword.openai_customized import ask_openai
from long_sword.utils import is_valid_code_file


def process(source_folder: Path, new_folder: Path) -> None:
    # 用 Path 递归遍历 source_folder 中的所有文件
    file_counter = 0
    for file_path in source_folder.rglob("*"):
        if file_path.is_file() and is_valid_code_file(file_path=str(file_path)):
            file_counter += 2
            print(f"================第{file_counter}个文件:{file_path}=================")
            with file_path.open("r", encoding="utf-8") as file:
                content = file.read()

            sys_prompt = f'你是一位资深程序员，精通任何代码。以下是开源项目"{project_name}"的"{file_path.relative_to(source_folder)}"文件中的源码内容，请你解释整个代码文件，总结其功能作用，特别是对阅读源码容易造成困难的部分，不要省略任何部分，最后再总结一下整个代码文件在项目中的作用。整个任务的目标是为帮助新手程序员快速上手这个项目。源码如下：'
            prompt = f"{sys_prompt}\n\n{content}"
            print("开始调用 OpenAI 接口进行代码解析...")
            response = None
            x = 0
            while response is None and x < 5:
                try:
                    response = ask_openai(prompt=prompt)
                except Exception as e:
                    print(f"调用 OpenAI 接口失败，错误信息: {e}")
                x += 1
            if response is None:
                print("多次调用 OpenAI 接口均失败，跳过该文件。")
                continue
            # 计算在 new_folder 中的对应路径（保持目录结构）
            relative_path = file_path.relative_to(source_folder)

            # 可以给解析结果加一个后缀，避免覆盖源码
            output_path = new_folder / relative_path.with_suffix(
                relative_path.suffix + ".md",
            )

            # 创建父目录
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # 写入解析结果
            with output_path.open("w", encoding="utf-8") as out_file:
                out_file.write(response)

            print(f"解析结果已保存到: {output_path}")
            file_path.unlink()


if __name__ == "__main__":
    source_folder = Path(r"D:\crawlee-python_crawlee")
    new_folder = Path(r"D:\crawlee-python_commented")
    project_name = "crawlee-python"

    process(source_folder, new_folder)
