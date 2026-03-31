from pyside_ui_backpack.css.colors import Colors


def test_colors_include_expected_themes():
    expected = {'BLUE', 'RED', 'GREEN', 'GREY', 'DARK_BLUE', 'BG_BLACK'}
    assert expected.issubset(set(Colors.__members__.keys()))


def test_color_values_have_foreground_and_background():
    for color in Colors:
        assert isinstance(color.value.foreground_color, str)
        assert isinstance(color.value.background_color, str)
        assert color.value.foreground_color.startswith('rgb(')
        assert color.value.background_color.startswith('rgb(')
