"""
Useful constant variables.
"""

from pathlib import Path
import pathlib

ASSETS_PATH = pathlib.Path("путь/к/папке/с/данными")
CRAWLER_CONFIG_PATH = pathlib.Path("config.json")  # или полный путь
NUM_ARTICLES_UPPER_LIMIT = 150
TIMEOUT_LOWER_LIMIT = 0
TIMEOUT_UPPER_LIMIT = 60
PROJECT_ROOT = Path(__file__).parent.parent
PROJECT_CONFIG_PATH = PROJECT_ROOT / "project_config.json"
CONFIG_PACKAGE_PATH = PROJECT_ROOT / "config"
CORE_UTILS_PACKAGE_PATH = PROJECT_ROOT / "core_utils"

