# pke/app/gear_up.py
import yaml
import asyncio
from pyppeteer import launch

def setup_environment():
    print("🔧 Setting up the application environment.")
    config = load_config('config.yml')
    print("✅ Environment setup completed.")
    return config

def load_config(file_path):
    """
    Loads configuration from a YAML file.
    """
    print(f"📖 Loading configuration from {file_path}...")
    with open(file_path, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    print(f"🎉 Configuration loaded successfully from {file_path}.")
    return cfg

async def init_web_driver():
    """
    Initializes Pyppeteer web driver for asynchronous web scraping.
    """
    print("🖥️ Initializing WebDriver...")
    browser = await launch(headless=True)
    page = await browser.newPage()
    print("🚀 WebDriver Initialized.")
    return browser, page
