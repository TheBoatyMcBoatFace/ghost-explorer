# pke/app/trap.py

import os
import asyncio
import aiohttp
from .ecu_transfer import write_to_csv

async def fetch_page(session, page_number, category):
    url = os.getenv('WHERE_GHOSTS_COME_FROM', 'default_url_if_not_set')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0',
        'content-type': 'application/x-www-form-urlencoded',
    }
    payload = {
        "requests": [
            {
                "indexName": "EXPLORE",
                "params": f"facets=%5B%22lang%22%5D&filters=categories%3A%22{category}%22&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=21&maxValuesPerFacet=50&page={page_number}&tagFilters="
            }
        ]
    }

    async with session.post(url, headers=headers, json=payload) as response:
        return await response.json()

def match_data_to_schema(data_item, schema):
    """
    Restructure the data item to match the provided schema.
    """
    structured_item = {key: data_item.get(key, '') for key in schema}
    return structured_item

async def crawl_and_capture(config):
    async with aiohttp.ClientSession() as session:
        for category in config.get('categories', []):
            if not category.get('enable', True):
                continue
            page_number = 0
            category_items = []
            while True:
                print(f"Fetching page {page_number} for category {category['name']}...")
                response = await fetch_page(session, page_number, category['slug'])
                data = response.get('results', [])[0].get('hits', [])
                if not data:
                    break
                category_items.extend(data)
                page_number += 1

            # Move data matching process inside crawl_and_capture
            if category_items:
                processed_items = [match_data_to_schema(item, config['schema']) for item in category_items]
                await write_to_csv(processed_items, config.get('schema', []), category['slug'])
