import concurrent
import os
import re
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

import aiohttp
import aiofiles
from tqdm import tqdm
from pathlib import Path
from selenium import webdriver
from aiohttp import ClientTimeout
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

gcp = [
    # 'amateur', 'asian', 'ass', 'babe', 'bath', 'beautiful', 'big-tits', 'bikini', 'blonde', 'bondage', 'boots',
    # 'brazilian', 'brunette', 'centerfold', 'christmas',
    'chubby', 'clothed', 'college', 'cosplay', 'cougar', 'curvy',
    'doggystyle', 'ebony', 'european', 'face', 'fake-tits', 'feet', 'girlfriend', 'glamour', 'glasses', 'granny',
    'hairy', 'high-heels', 'homemade', 'hot-naked-women', 'housewife', 'japanese', 'jeans', 'latex', 'latina',
    'legs', 'lingerie', 'maid', 'masturbation', 'mature', 'milf', 'model', 'mom', 'natural-tits', 'nipples',
    'non-nude', 'nude', 'nurse', 'office', 'oiled', 'panties', 'pantyhose', 'pool', 'pornstar', 'redhead',
    'saggy-tits', 'secretary', 'selfie', 'sexy', 'shaved', 'short-hair', 'shorts', 'skinny', 'skirt', 'smoking',
    'socks', 'solo', 'sports', 'spreading', 'stockings', 'tattoo', 'teen', 'thai', 'thick', 'thong', 'undressing',
    'uniform', 'upskirt', 'white', 'yoga-pants'
]

SRC_DIR = Path('/Volumes/external_drive')


class ImageScraper:

    def __init__(self, main_url: str, category: str):
        self.main_url = main_url
        self._category = category

    def pure_category(self):
        return self.category

    @property
    def category(self):
        if "/" in self._category:
            return "-".join(self._category.split("/"))
        else:
            return self._category

    @classmethod
    def setup_driver(cls):
        """Set up Selenium WebDriver."""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    @staticmethod
    def get_text_from_div(html):
        pattern = r'<div class="hidden suggest-2_source-list__cat">\s*(.*?)\s*</div>'
        match = re.search(pattern, html, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None

    def extract_gallery_info(self, gallery_url: str):
        driver = self.setup_driver()
        driver.get(gallery_url)

        gallery_path = SRC_DIR / self.category / gallery_url.split('/')[-2] / url.split('/')[-1]
        gallery_path.parent.mkdir(parents=True, exist_ok=True)

        links = []
        try:
            tiles_ul = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'gallery-info'))
            )

            list_items = tiles_ul.find_elements(By.CLASS_NAME, 'gallery-info__item')
            info_file_path = gallery_path.parent / 'gallery_info.txt'
            if info_file_path.exists():
                os.remove(info_file_path)

            with open(info_file_path, 'w') as f:
                for item in list_items:
                    try:
                        title = item.find_element(By.CLASS_NAME, 'gallery-info__title')
                    except Exception:
                        title = "<no gallery-info__title>"

                    if "channel" in title.text.lower():
                        try:
                            tags = item.find_elements(By.TAG_NAME, 'a')
                            content = "".join([a.get_attribute('title') for a in tags])
                        except Exception:
                            content = "<no a tag>"

                        f.write(
                            f"Channel: {content if isinstance(content, str) else content}\n"
                        )

                    elif "models" in title.text.lower():
                        content = item.find_element(By.CLASS_NAME, 'gallery-info__content')
                        a_hrefs = content.find_elements(By.TAG_NAME, 'a')

                        models = []
                        for a in a_hrefs:
                            model = a.get_attribute('title')
                            if model:
                                models.append(model)

                        f.write(
                            f"Models: {models}\n"
                        )

                    elif "categories" in title.text.lower():
                        cats = []
                        content = item.find_element(By.CLASS_NAME, 'gallery-info__content')
                        a_hrefs = content.find_elements(By.TAG_NAME, 'a')
                        for a in a_hrefs:
                            title = a.get_attribute('title')
                            if title:
                                cats.append(title)

                        extra_cats = self.get_text_from_div(item.get_attribute('outerHTML')).split(",")

                        f.write(
                            f"Categories: {cats}\n"
                            f"Categories_suggestions: {extra_cats}\n"
                        )

                    elif "tags" in title.text.lower():
                        content = item.find_element(By.CLASS_NAME, 'gallery-info__content')
                        a_hrefs = content.find_elements(By.TAG_NAME, 'a')

                        titles = []
                        for a in a_hrefs:
                            title = a.get_attribute('title')
                            if title:
                                titles.append(title)

                        f.write(
                            f"Tags: {titles}\n"
                        )

        except TimeoutException:
            print("TimeoutException: Could not find gallery-info.")

        finally:
            driver.quit()

        return links

    def run(self):
        category_path = SRC_DIR / self.category
        txt_file_path = category_path / "gallery_links.txt"

        with open(txt_file_path, 'r') as file:
            gallery_links = file.read().splitlines()

        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.extract_gallery_info, gallery_url)
                for gallery_url in gallery_links
            ]
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
                future.result()


if __name__ == "__main__":
    url = 'https://www.pornpics.com'

    for cat in gcp:
        print(f"Scraping `{cat}` category...")
        image_scraper = ImageScraper(url, cat)
        image_scraper.run()
        del image_scraper
