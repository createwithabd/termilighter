from typing import Tuple, Optional, Final

# from .color_converter import ColorConverter


# class Consoler(ColorConverter):
#     def __init__(self) -> None:
#         super().__init__()

print("\033[1m\033[38;2;95;175;215mHello\033[0m")


print("\033[1mBold\033[0m\n")  # Bold
print("\033[3mItalic\033[0m\n")  # Italic
print("\033[8mHello\033[0m\n")  # Hide
print("\033[9mStrikeThrough\033[0m\n")  # Strikethrough
print("\033[4mUnderline\033[0m\n")  # Underline

print("\033[48;2;95;175;215mHello\033[0m")  # Background
print("\033[38;2;95;0;215mHello\033[0m")  # Foreground

print("\033[48;2;95;175;215;38;2;95;0;215mCHECKING SOMETHING\033[0m")

print("\033[38;2;95;175;215;48;2;95;0;215mCHECKING SOMETHING\033[0m")
