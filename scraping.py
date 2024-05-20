import os
import time
import asyncio
import aiohttp
import aiofiles
from tqdm import tqdm
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

"""
Possible sites:
- https://idealmature.com/
"""

categories = [
    # "mature","amateur", "milf",
    # "tags/mature-amateur",
    # "lingerie",
    # "sexy",
    "cougar",
    "stockings", "housewife", "saggy-tits", "chubby", "redhead", "undressing", "curvy",
    "non-nude", "teen", "selfie", "ebony", "ass", "natural-tits", "hairy", "beautiful",
    "secretary", "spreading", "masturbation", "thick", "upskirt", "tattoo", "skinny",
    "short-hair", "bikini", "panties", "babe", "feet", "latina", "solo", "shaved",
    "skirt", "glasses", "latex", "girlfriend", "clothed", "brunette", "pantyhose",
    "shorts", "brazilian", "face", "bath", "jeans", "boots", "hot-naked-women"
]


class ImageScraper:

    def __init__(self, main_url: str, category: str):
        self.driver = self.setup_driver()
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

    def scroll_to_bottom(self):
        """Scrolls to the bottom of the page using Selenium."""
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        scrolls = 0
        while True:
            print(f"{scrolls}: Scrolling...")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Adjust this depending on the site's loading time
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("Reached the bottom of the page.")
                break
            last_height = new_height
            scrolls += 1

    def fetch_current_links(self):
        """Fetches currently available gallery links on the page using explicit waits."""
        links = []
        try:
            tiles_ul = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.ID, 'tiles'))
            )
            list_items = tiles_ul.find_elements(By.CLASS_NAME, 'rel-link')

            for li in list_items:
                try:
                    link = li.get_attribute('href')
                    if link and (link.startswith(self.main_url) or link.startswith("https://cdni.pornpics.com")):
                        links.append(link)
                except Exception:
                    print(f"Failed to find 'rel-link' in one of the items. Skipping...")
        except TimeoutException:
            print("Timeout waiting for 'tiles' element to be present.")
        except NoSuchElementException:
            print("No such element: 'tiles'")

        return links

    def extract_gallery_links(self):
        """Uses Selenium to handle infinite scroll and extract gallery links."""
        self.driver.get(f"{self.main_url}/{self.pure_category()}")
        self.scroll_to_bottom()
        return self.fetch_current_links()

    def extract_image_links_from_gallery(self, gallery_url: str):
        """Uses Selenium to handle infinite scroll and extract gallery links."""
        self.driver.get(gallery_url)
        return self.fetch_current_links()

    async def download_file(self, session, url, directory, gallery_name):
        path = Path(directory) / gallery_name / url.split('/')[-1]
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            async with session.get(url) as response:
                if response.status == 200:
                    async with aiofiles.open(path, mode='wb') as f:
                        while True:
                            chunk = await response.content.read(1024)  # read in chunks
                            if not chunk:
                                break
                            await f.write(chunk)
                else:
                    print(f"Failed to download {url} with status {response.status}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    async def download_all(self, urls, directory_path, gallery_name):
        os.makedirs(directory_path, exist_ok=True)
        async with aiohttp.ClientSession() as session:
            tasks = [self.download_file(session, url, directory_path, gallery_name=gallery_name) for url in urls]
            await asyncio.gather(*tasks)

    async def fetch_and_download(self):
        category_path = Path(f"./scraped_images/{self.category}")
        txt_file_path = category_path / "gallery_links.txt"

        if os.path.exists(txt_file_path):
            with open(txt_file_path, 'r') as file:
                gallery_links = file.read().splitlines()
        else:
            gallery_links = self.extract_gallery_links()
            txt_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(txt_file_path, 'w') as file:
                for link in gallery_links:
                    file.write(f"{link}\n")

        print(f"Found {len(gallery_links)} gallery links.")

        all_image_links = []
        for gallery_url in tqdm(gallery_links):
            gallery_path = Path(f"./scraped_images/{self.category}/{gallery_url.split('/')[-2]}")

            if os.path.exists(gallery_path):
                if len(os.listdir(gallery_path)) != 0:
                    continue

            image_links = self.extract_image_links_from_gallery(gallery_url)
            all_image_links.extend(image_links)

            await asyncio.create_task(
                self.download_all(image_links, category_path, gallery_name=gallery_url.split('/')[-2])
            )

    def run(self):
        """Runs the scraper."""
        asyncio.run(self.fetch_and_download())

    def stop(self):
        """Stops the driver."""
        self.driver.quit()


if __name__ == "__main__":
    url = 'https://www.pornpics.com'

    for cat in categories:
        image_scraper = ImageScraper(url, cat)
        image_scraper.run()
        image_scraper.stop()
