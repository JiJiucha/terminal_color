from typing import Dict, Tuple

# Constants
RESET = '\033[0m'
STRING_STYLES: Dict[str, int] = {
    'normal': 0,
    'bright': 1,
    'underline': 4,
    'blink': 5,
    'inverse': 7,
    'invisible': 8  # 修正拼写错误
}

# Color functions with validation
def _validate_rgb(r: int, g: int, b: int) -> None:
    for value in (r, g, b):
        if not 0 <= value <= 255:
            raise ValueError(f"Invalid RGB value {value}, must be 0-255")

def text_color_rgb(r: int, g: int, b: int) -> str:
    """生成文字颜色ANSI转义码"""
    _validate_rgb(r, g, b)
    return f'\033[38;2;{r};{g};{b}m'

def back_color_rgb(r: int, g: int, b: int) -> str:
    """生成背景颜色ANSI转义码"""
    _validate_rgb(r, g, b)
    return f'\033[48;2;{r};{g};{b}m'

# Style function with validation
def string_style(*styles: str) -> str:
    """生成文字样式ANSI转义码"""
    codes = []
    for style in styles:
        if style not in STRING_STYLES:
            raise ValueError(f"无效样式: {style}")
        codes.append(str(STRING_STYLES[style]))
    return f'\033[{";".join(codes)}m'

# Reset function
def reset_all() -> str:
    """返回重置所有样式的转义码"""
    return RESET

# 测试代码
if __name__ == '__main__':
    # 注意：\033[2J 是清屏指令，原代码中的 2I 可能是笔误
    print('\033[2J' + 
          text_color_rgb(255, 0, 0) + 
          string_style('inverse') + 
          '123' + 
          RESET)
    print(1)
    print(reset_all(), end='')
   