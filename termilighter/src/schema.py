from pydantic import BaseModel
from typing import Optional, Tuple


class RgbToXterm(BaseModel):
    rgb: Tuple[int, int, int]
    xterm_string: Optional[str]


class FormattingConfig(BaseModel):
    bold: Optional[bool] = False
    underline: Optional[bool] = False
    strikethrough: Optional[bool] = False
    italic: Optional[bool] = False
