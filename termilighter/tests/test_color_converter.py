import pytest
from src.color_converter import ColorConverter

converter = ColorConverter()


def test_rgb_to_hex():
    assert converter.rgb_to_hex(rgb=(95, 0, 215)) == "#5F00D7"
    assert converter.rgb_to_hex(rgb=(95, 175, 215)) == "#5FAFD7"


def test_hex_to_rgb():
    assert converter.hex_to_rgb(hex="#5F00D7") == (95, 0, 215)
    assert converter.hex_to_rgb(hex="5FAFD7") == (95, 175, 215)


def test_rgb_to_xterm256():
    assert converter.rgb_to_xterm256(rgb=(95, 0, 215)) == 56
    assert converter.rgb_to_xterm256(rgb=(95, 175, 215)) == 74


def test_hex_to_xterm256():
    assert converter.hex_to_xterm256(hex="#5F00D7") == 56
    assert converter.hex_to_xterm256(hex="5FAFD7") == 74


def test_rgb_to_ANSI_color_string():
    assert converter.rgb_to_ANSI_color_string(rgb=(95, 0, 215)) == "95;0;215"
    assert converter.rgb_to_ANSI_color_string(rgb=(95, 175, 215)) == "95;175;215"


def test_hex_to_ANSI_color_string():
    assert converter.hex_to_ANSI_color_string(hex="#5F00D7") == "95;0;215"
    assert converter.hex_to_ANSI_color_string(hex="5FAFD7") == "95;175;215"


def test_validate_xtermType():
    with pytest.raises(TypeError) as excinfo:
        converter.validate_xtermType(xTerm="s")
    assert str(excinfo.value) == "Need an int value not <class 'str'>."

    with pytest.raises(ValueError) as excinfo:
        converter.validate_xtermType(xTerm=455)
    assert str(excinfo.value) == "xTerm value should be in range between 0 and 255."


def test_get_fgColor_from_xterm256():
    assert converter.get_fgColor_from_xterm256(xTerm=25) == "\033[38;2;25m"
    assert converter.get_fgColor_from_xterm256(xTerm=45) == "\033[38;2;45m"


def test_get_bgColor_from_xterm256():
    assert converter.get_bgColor_from_xterm256(xTerm=25) == "\033[48;2;25m"
    assert converter.get_bgColor_from_xterm256(xTerm=45) == "\033[48;2;45m"


def test_get_full_color_from_xterm256():
    assert (
        converter.get_full_color_from_xterm256(fg_xterm=25, bg_xterm=75)
        == "\033[48;2;75;38;2;25m"
    )
    assert (
        converter.get_full_color_from_xterm256(fg_xterm=12, bg_xterm=142)
        == "\033[48;2;142;38;2;12m"
    )


def test_get_fgColor_from_hex():
    assert converter.get_fgColor_from_hex(hex="#5F00D7") == "\033[38;2;95;0;215m"
    assert converter.get_fgColor_from_hex(hex="5FAFD7") == "\033[38;2;95;175;215m"


def test_get_fgColor_from_rgb():
    assert converter.get_fgColor_from_rgb(rgb=(95, 0, 215)) == "\033[38;2;95;0;215m"
    assert converter.get_fgColor_from_rgb(rgb=(95, 175, 215)) == "\033[38;2;95;175;215m"


def test_get_bgColor_from_hex():
    assert converter.get_bgColor_from_hex(hex="#5F00D7") == "\033[48;2;95;0;215m"
    assert converter.get_bgColor_from_hex(hex="5FAFD7") == "\033[48;2;95;175;215m"


def test_get_bgColor_from_rgb():
    assert converter.get_bgColor_from_rgb(rgb=(95, 0, 215)) == "\033[48;2;95;0;215m"
    assert converter.get_bgColor_from_rgb(rgb=(95, 175, 215)) == "\033[48;2;95;175;215m"


def test_get_full_color_from_hex():
    assert (
        converter.get_full_color_from_hex(fgHex="111D13", bgHex="AFFC41")
        == "\033[48;2;175;252;65;38;2;17;29;19m"
    )
    assert (
        converter.get_full_color_from_hex(fgHex="bc4749", bgHex="ea9010")
        == "\033[48;2;234;144;16;38;2;188;71;73m"
    )


def test_get_full_color_from_rgb():
    assert (
        converter.get_full_color_from_rgb(fgRgb=(17, 29, 19), bgRgb=(175, 252, 65))
        == "\033[48;2;175;252;65;38;2;17;29;19m"
    )
    assert (
        converter.get_full_color_from_rgb(fgRgb=(188, 71, 73), bgRgb=(234, 144, 16))
        == "\033[48;2;234;144;16;38;2;188;71;73m"
    )


#  write assert statement to catch exception!
def test_get_fgColor_base_on_type():
    assert (
        converter.get_fgColor_base_on_type(color=45, color_type="xterm")
        == "\033[38;2;45m"
    )
    assert (
        converter.get_fgColor_base_on_type(color="#111D13", color_type="hex")
        == "\033[38;2;17;29;19m"
    )
    assert (
        converter.get_fgColor_base_on_type(color=(95, 0, 215), color_type="rgb")
        == "\033[38;2;95;0;215m"
    )
