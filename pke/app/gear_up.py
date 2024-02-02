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
    async def init_web_driver():
    print("🖥️ Initializing WebDriver...")
    try:
        browser = await launch(headless=True, args=['--disable-gpu', '--no-sandbox', '--disable-setuid-sandbox'])
        page = await browser.newPage()
        print("🚀 WebDriver Initialized.")
    except Exception as e:
        print(f"❌ WebDriver Initialization Failed: {e}")
    return browser, page
