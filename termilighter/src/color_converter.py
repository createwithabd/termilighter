"""module for converting colors from one type to another."""

from typing import Tuple, Optional, Final, Literal, Union
from ._color_constants import XTERM_HEX
from .schema import FormattingConfig


class ColorConverter:
    """Convert color from one type to another."""

    def __init__(self) -> None:
        pass

    def rgb_to_hex(self, rgb: Tuple[int, int, int]) -> str:
        """Convert rgb color tuple to hex color code.

        Args:
            rgb (Tuple[int, int, int], optional): rgb color tuple. Defaults to None.

        Raises:
            TypeError: Trigger when rgb is not a correct tuple.

        Returns:
            str: Six digit hex color code.
        """
        if not isinstance(rgb, tuple):
            raise TypeError("Need rgb color tuple. For Example: (int, int, int) ")
        hex = "#%02x%02x%02x" % rgb
        if len(hex) == 7:
            return hex.upper()

    def hex_to_rgb(self, hex: str) -> Tuple[int, int, int]:
        """Convert hex color digits to rgb color tuple.

        Args:
            hex (str): Six digit hex color code.

        Raises:
            TypeError: Trigger when type of hex is wrong.
            ValueError: Trigger when hex value is an empty string.
            ValueError: Trigger when hex value is not a valid six digit hex code.

        Returns:
            Tuple[int, int, int]: rgb color tuple.
        """
        if not isinstance(hex, str):
            raise TypeError("Need a hex color code. For Example: #000000 or 000000 ")
        if len(hex) == 0:
            raise ValueError("Can not convert an empty string to rgb tuple.")

        if hex[0] == "#":
            hex = hex.split("#")[1]

        if len(hex) == 6:
            return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))
        else:
            raise ValueError("Need a six digit hex color code.")

    @staticmethod
    def color_distance(c1: Tuple[int, int, int], c2: Tuple[int, int, int]):
        """Return color distance between two rgb color tuples.

        Args:
            c1 (Tuple[int, int, int]): rgb color tuple one.
            c2 (Tuple[int, int, int]): rgb color tuple two.

        Raises:
            TypeError: Trigger, when c1 is not a valid rgb tuple.
            TypeError: Trigger, when c2 is not a valid rgb tuple.

        Returns:
            float: color distance value between two rgb tuples.
        """
        if not isinstance(c1, tuple):
            raise TypeError("Need rgb color tuple. For Example: (int, int, int) ")
        if not isinstance(c2, tuple):
            raise TypeError("Need rgb color tuple. For Example: (int, int, int) ")

        r1, g1, b1 = c1
        r2, g2, b2 = c2

        return ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5

    def rgb_to_xterm256(self, rgb: Tuple[int, int, int]) -> int:
        """Convert rgb color tuple to xterm256 color number.

        Args:
            rgb (Tuple[int, int, int]): rgb color tuple.

        Raises:
            TypeError: Trigger, when rgb is not a valid color tuple.

        Returns:
            int: xterm256 color code number.
        """
        if not isinstance(rgb, tuple):
            raise TypeError("Need rgb color tuple. For Example: (int, int, int) ")

        colors = list(
            map(
                self.hex_to_rgb,
                XTERM_HEX,
            )
        )
        closest_color = min(colors, key=lambda x: ColorConverter.color_distance(rgb, x))
        return colors.index(closest_color)

    def hex_to_xterm256(self, hex: str) -> int:
        """Convert six digit hex code to xterm256 number.

        Args:
            hex (str): Six digit hex color code.

        Returns:
            int: xterm256 color number.
        """
        rgb = self.hex_to_rgb(hex)
        return self.rgb_to_xterm256(rgb)

    def rgb_to_ANSI_color_string(self, rgb: Tuple[int, int, int]) -> str:
        """Convert rgb color tuple to ANSI color string

        Args:
            rgb (Tuple[int, int, int]): rgb color tuple.

        Raises:
            TypeError: If rgb is not a valid tuple.

        Returns:
            str: ANSI color string.
        """
        if not isinstance(rgb, tuple):
            raise TypeError("Need rgb color tuple. For Example: (int, int, int) ")
        return f"{rgb[0]};{rgb[1]};{rgb[2]}"

    def hex_to_ANSI_color_string(self, hex: str) -> str:
        """Convert Hex color code to ANSI color string.

        Args:
            hex (str): six digit hex color code.

        Returns:
            str: ANSI color string.
        """
        rgb_color = self.hex_to_rgb(hex)
        return self.rgb_to_ANSI_color_string(rgb=rgb_color)

    @staticmethod
    def validate_xtermType(xTerm: int) -> int:
        """Validate xTerm value and return it.

        Args:
            xTerm (int): xTerm color value.

        Raises:
            TypeError: When xTerm is not an in value.
            ValueError: When xTerm value is not in between 0 and 255.

        Returns:
            int: xTerm color int value after validating it.
        """
        if not isinstance(xTerm, int):
            raise TypeError(f"Need an int value not {type(xTerm)}.")
        if xTerm > 255 or xTerm < 0:
            raise ValueError(f"xTerm value should be in range between 0 and 255.")
        return xTerm

    def get_fgColor_from_xterm256(self, xTerm: int) -> str:
        """Return foreground color from xterm 256 color value.

        Args:
            xTerm (int): xTerm color, value ranges between `0` and `255`

        Returns:
            str: Foreground color string from xTerm value.
        """
        xTerm = ColorConverter.validate_xtermType(xTerm)
        return f"\033[38;2;{xTerm}m"

    def get_bgColor_from_xterm256(self, xTerm: int) -> str:
        """Return background color from xterm 256 color value.

        Args:
            xTerm (int): xTerm color, value ranges between `0` and `255`

        Returns:
            str: Background color string from xTerm value.
        """
        xTerm = ColorConverter.validate_xtermType(xTerm)
        return f"\033[48;2;{xTerm}m"

    def get_full_color_from_xterm256(self, fg_xterm: int, bg_xterm: int) -> str:
        """Return complete color with custom background and foreground from xterm color value.

        Args:
            fg_xterm (int): Foreground xTerm color value.
            bg_xterm (int): Background xTerm color value.

        Returns:
            str: Complete color string with custom background and foreground color.
        """
        fg_xterm = ColorConverter.validate_xtermType(fg_xterm)
        bg_xterm = ColorConverter.validate_xtermType(bg_xterm)
        return f"\033[48;2;{bg_xterm};38;2;{fg_xterm}m"

    def get_fgColor_from_hex(self, hex: str) -> str:
        """Return foreground color from hex color value.

        Args:
            hex (str): Hex color value. For Example: #111D13.

        Returns:
            str: Foreground color string from hex value.
        """
        color_string = self.hex_to_ANSI_color_string(hex)
        return f"\033[38;2;{color_string}m"

    def get_bgColor_from_hex(self, hex: str) -> str:
        """Return background color from hex color value.

        Args:
            hex (str): Hex color value, For Example: #111D13

        Returns:
            str: Background color string from hex value.
        """
        color_string = self.hex_to_ANSI_color_string(hex)
        return f"\033[48;2;{color_string}m"

    def get_full_color_from_hex(self, fgHex: str, bgHex: str) -> str:
        """Return complete color with custom foreground and background color.

        Args:
            fgHex (str): Foreground color hex value.
            bgHex (str): Background color hex value.

        Returns:
            str: Complete color string with custom background and foreground color.
        """
        fg_string = self.hex_to_ANSI_color_string(fgHex)
        bg_string = self.hex_to_ANSI_color_string(bgHex)
        return f"\033[48;2;{bg_string};38;2;{fg_string}m"

    def get_fgColor_from_rgb(self, rgb: Tuple[int, int, int]) -> str:
        """Return foreground color from rgb color tuple.

        Args:
            rgb (Tuple[int, int, int]): rgb color tuple value.

        Returns:
            str: Foreground color string from rgb tuple.
        """
        color_string = self.rgb_to_ANSI_color_string(rgb)
        return f"\033[38;2;{color_string}m"

    def get_bgColor_from_rgb(self, rgb: Tuple[int, int, int]) -> str:
        """Return background color from rgb color tuple.

        Args:
            rgb (Tuple[int, int, int]): rgb color tuple.

        Returns:
            str: Background color string from rgb tuple.
        """
        color_string = self.rgb_to_ANSI_color_string(rgb)
        return f"\033[48;2;{color_string}m"

    def get_full_color_from_rgb(
        self, fgRgb: Tuple[int, int, int], bgRgb: Tuple[int, int, int]
    ) -> str:
        """Return complete color with custom background and foreground from rgb tuple.

        Args:
            fgRgb (Tuple[int, int, int]): Foreground rgb tuple value.
            bgRgb (Tuple[int, int, int]): Background rgb tuple value.

        Returns:
            str: Complete color string with custom background and foreground color.
        """
        fg_string = self.rgb_to_ANSI_color_string(fgRgb)
        bg_string = self.rgb_to_ANSI_color_string(bgRgb)
        return f"\033[48;2;{bg_string};38;2;{fg_string}m"

    # INFO start from here!
    def get_fgColor_base_on_type(
        self,
        color_type: Literal["xterm", "hex", "rgb"] = "xterm",
        color: Optional[Union[int, str, tuple]] = 25,
    ):
        if (
            not isinstance(color, int)
            and not isinstance(color, str)
            and not isinstance(color, tuple)
        ):
            raise TypeError(
                f"Color can either be int, str or a tuple not a {type(color)}"
            )
        if color_type == "xterm":
            if isinstance(color, int):
                out_color = self.get_fgColor_from_xterm256(xTerm=color)
        elif color_type == "hex":
            if isinstance(color, str):
                out_color = self.get_fgColor_from_hex(hex=color)
        elif color_type == "rgb":
            if isinstance(color, tuple):
                out_color = self.get_fgColor_from_rgb(rgb=color)
        else:
            raise ValueError("Color type and color value doesn't match.")
        return out_color

    def add_prefix(
        self,
        tag: str = "message",
        color: Optional[Union[int, str, tuple]] = 25,
        color_type: Literal["xterm", "hex", "rgb"] = "xterm",
    ):
        pass
