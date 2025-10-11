from eaglewrapper import Eagle as eg
from pathlib import Path
from typing import Any

class Eagle:

    def __init__(self, ) -> None:
        self.LIBRARY_PATH = Path(r"F:\eagle_librarys\Illusion.library\images")
        self.eagle = eg()

    def list_items_path(self, folder:str = 'ME2U2JT8S0WU8') -> list:
        """
        获取文件夹中的所有文件路径（递归包含所有子文件夹）
        默认获取 temp 文件夹中的文件
        """
        items_id = self.list_items(folder)
        return [self.LIBRARY_PATH / f"{item_id}.info" for item_id in items_id]

    def list_items(self, folder:str = 'ME2U2JT8S0WU8') -> list:
        """
        获取文件夹中的所有itemid (递归包含所有子文件夹)
        默认获取 temp 文件夹中的文件
        """
        folders = self.eagle.list_folders()
        all_folder_ids = self._collect_subfolder_ids(folders, folder)
        items = self.eagle.list_items(limit=99999, folders=all_folder_ids)
        return [x.get("id") for x in items]

    def _collect_subfolder_ids(self,folders: list[dict[str, Any]], root_id: str) -> list[str]:
        """递归收集 root_id 下的所有子文件夹 id（包含 root_id 自身）."""

        def find_folder_by_id(
            folder_list: list[dict[str, Any]],
            target_id: str,
        ) -> dict[str, Any] | None:
            """在文件夹树中查找目标文件夹."""
            for f in folder_list:
                if f["id"] == target_id:
                    return f
                found = find_folder_by_id(f.get("children", []), target_id)
                if found:
                    return found
            return None

        def collect_ids(folder: dict[str, Any], result: list[str]) -> None:
            """递归收集文件夹 id."""
            result.append(folder["id"])
            for child in folder.get("children", []):
                collect_ids(child, result)

        # 找到 root_id 对应的文件夹
        root_folder = find_folder_by_id(folders, root_id)
        if not root_folder:
            raise ValueError(f"未找到指定 root_id: {root_id}")

        result: list[str] = []
        collect_ids(root_folder, result)
        return result




