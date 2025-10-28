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
