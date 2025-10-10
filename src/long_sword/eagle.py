from ast import List
from eaglewrapper import Eagle as eg
from pathlib import Path

class Eagle:

    def __init__(self, ) -> None:
        self.LIBRARY_PATH = Path(r"F:\eagle_librarys\Illusion.library\images")

    def list_items_path(self, folder:str = 'ME2U2JT8S0WU8') -> list:
        """
        获取文件夹中的所有文件路径
        默认获取 temp 文件夹中的文件
        """
        eagle = eg()
        items = eagle.list_items(folders=[folder])
        paths = []
        for item in items:
            item_id = item.get("id")
            info_dir = self.LIBRARY_PATH / f"{item_id}.info"
            paths.append(info_dir)
        return paths



