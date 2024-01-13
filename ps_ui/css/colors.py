from enum import Enum
from collections import namedtuple

Color = namedtuple('Color', ['foreground_color', 'background_color'])


class Colors(Enum):
    '''  buttons color themes '''
    BLUE = Color('rgb(46, 134, 193)', 'rgb(230, 230, 230)')
    RED = Color('rgb(160, 20, 20)', 'rgb(250, 250, 250)')
    ORANGE = Color('rgb(236, 183, 41)', 'rgb(30, 30, 30)')
    GREEN = Color('rgb(40, 205, 50)', 'rgb(30, 30, 30)')
    YELLOW = Color('rgb(240, 240, 0)', 'rgb(30, 30, 30)')
    GRAY = Color('rgb(80, 80, 80)', 'rgb(230, 230, 230)')
    DISABLED = Color('rgb(80, 80, 80)', 'rgb(180, 180, 180)')


if __name__ == '__main__':
    print(f'Value for {Colors.BLUE} is '
          f'foreground_color {Colors.BLUE.value.foreground_color} and '
          f'background_color {Colors.BLUE.value.background_color}'
          )
