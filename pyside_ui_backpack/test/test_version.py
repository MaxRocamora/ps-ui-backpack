from pyside_ui_backpack.version import (
    VERSION_MAJOR,
    VERSION_MINOR,
    VERSION_PATCH,
    __version__,
)


def test_version_string_matches_parts():
    """Test that the __version__ string is correctly formatted and matches the major, minor, and patch parts."""
    assert __version__ == f'{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}'


def test_version_is_current_release():
    """Test that the __version__ string matches the current release version."""
    assert __version__ == '1.0.7'
