# pke/run.py

from app.gear_up import setup_environment, init_web_driver
from app.trap import crawl_and_capture
import asyncio

async def main():
    # Setting up the environment (config, web driver, etc.)
    config = setup_environment()

    # Initialize Web Driver
    browser, page = await init_web_driver()

    await crawl_and_capture(config)


    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
