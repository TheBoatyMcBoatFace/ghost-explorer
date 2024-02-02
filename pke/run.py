# pke/run.py

from app.gear_up import setup_environment, init_web_driver
from app.trap import crawl_and_capture
import asyncio

async def main():
    print("🚀 Launching setup...")
    config = setup_environment()

    print("🌍 Initializing Web Driver...")
    browser, page = await init_web_driver()

    print("🕸 Starting crawl process...")
    await crawl_and_capture(config)

    print("🏁 Closing browser...")
    await browser.close()
    print("🔚 Process completed successfully!")

if __name__ == '__main__':
    asyncio.run(main())
