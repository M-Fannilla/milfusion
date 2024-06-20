import os
import asyncio
from pathlib import Path

import aiohttp
from typing import TypeAlias
from duckduckgo_search import AsyncDDGS as DDGS
from aiohttp import ClientSession, ClientResponseError

import aiohttp

conn = aiohttp.TCPConnector(limit_per_host=50)

search_queries = {
    'anal sex': ['anal sex', 'ass fucking'],
    'asian': ['naked asian', 'asian woman', 'asian erotic'],
    'ass': ['ass', 'naked ass', 'ass erotic'],
    'ass licking': ['ass licking', 'ass licking erotic'],
    'asshole': ['ass hole', 'ass hole erotic'],
    'bath': ['bath erotic', 'bath sex'],
    'ball licking': ['ball licking', 'ball licking erotic'],
    'big beautiful woman': ['bbw', 'big beautiful woman', 'bbw erotic', 'bbw sex'],
    'bdsm': ['bdsm', 'bdsm erotic'],
    'beach': ['beach naked', 'beach erotic', 'beach sex'],
    'big tits': ['big tits', 'big tits clothing', 'big tits erotic'],
    'bikini': ['bikini', 'bikini erotic'],
    'blindfold': ['blindfold sex', 'blindfold erotic'],
    'blonde': ['blonde', 'blonde erotic', ],
    'blowbang': ['blowbang', 'blowbang erotic'],
    'blowjob': ['blowjob', 'blowjob erotic'],
    'bondage': ['bondage', 'bondage erotic'],
    'brunette': ['brunette', 'brunette full body', 'brunette erotic'],
    'chubby': ['chubby', 'chubby erotic'],
    'cosplay': ['cosplay', 'naked_cosplay', 'cosplay erotic'],
    'cowgirl': ['cowgirl sex', 'cowgirl erotic', 'cowgirl porn', 'cowgirl position', 'reverse cowgirl position'],
    'creampie': ['creampie pussy', 'creampie erotic'],
    'cum in mouth': ['cum in mouth', 'cum in mouth erotic'],
    'cum in pussy': ['cum in pussy', 'cum in pussy erotic'],
    'cum swapping': ['cum swapping', 'cum swapping erotic'],
    'cumshot': ['cumshot', 'cumshot erotic'],
    'curly': ['curly hair', 'curly hair sex', 'curly erotic'],
    'curvy': ['curvy naked', 'curvy erotic'],
    'deepthroat': ['deepthroat', 'deepthroat erotic'],
    'dildo': ['dildo pussy', 'dildo erotic', ],
    'doctor': ['doctor naked', 'doctor erotic', ],
    'doggy style': ['doggy style sex', 'doggy style erotic', 'doggy style porn', 'doggy style position'],
    'double penetration': ['double penetration', 'mmf sex'],
    'ebony': ['ebony sex', 'ebony naked', 'ebony erotic'],
    'facesitting': ['face sitting', 'face sitting erotic'],
    'facial': ['cum on face', 'cum on face erotic', 'facial erotic'],
    'fake tits': ['fake tits', 'fake tits erotic'],
    'feet': ['feet fetish', 'feet erotic'],
    'ffm': ['ffm sex', ],
    'fingering': ['fingering pussy', ],
    'fisting': ['fisting', ],
    'footjob': ['footjob erotic', ],
    'gangbang': ['gangbang', 'gangbang sex', 'gangbang group sex'],
    'gay': ['gay sex', 'gay erotic', ],
    'granny': ['granny erotic', ],
    'group sex': ['group sex', ],
    'gym': ['gym sex', 'gym erotic'],
    'hairy': ['hairy pussy', ],
    'handjob': ['handjob', 'handjob erotic'],
    'high heels': ['high heels erotic', ],
    'interracial': ['interracial sex', 'interracial erotic'],
    'jeans': ['jeans', 'jeans erotic'],
    'kissing': ['kissing', 'kissing erotic'],
    'ladyboy': ['ladyboy', 'ladyboy erotic'],
    'latex': ['latex', 'latex erotic'],
    'latina': ['latina', 'latina erotic'],
    'leather': ['leather', 'leather erotic'],
    'legs': ['female legs', 'legs erotic'],
    'lesbian': ['lesbian', 'lesbian erotic', 'lesbian sex', ],
    'lingerie': ['lingerie', 'lingerie sexy', 'lingerie erotic'],
    'maid': ['maid', 'maid erotic'],
    'massage': ['massage erotic', ],
    'masturbation': ['male masturbation', 'female masturbation'],
    'mature': ['mature sexy', 'mature erotic'],
    'milf': ['milf sexy', 'milf erotic'],
    'missionary': ['missionary sex', 'missionary position', 'missionary porn', 'missionary erotic'],
    'natural tits': ['natural tits', ],
    'nipples': ['nipples', 'nipples erotic'],
    'non nude': ['non nude', 'non nude erotic'],
    'nun': ['nun erotic', 'nun fetish'],
    'nurse': ['nurse erotic', 'nurse fetish'],
    'office': ['office erotic', 'office sex'],
    'oiled': ['oiled female', 'oiled erotic'],
    'old man': ['old man porn', ],
    'orgy': ['orgy porn', 'orgy erotic', 'orgy public'],
    'outdoor': ['outdoor fetish', 'outdoor porn', 'outdoor erotic'],
    'panties': ['panties fetish', 'panties erotic', 'panties porn'],
    'pantyhose': ['pantyhose fetish', 'pantyhose erotic', 'pantyhose porn'],
    'pawg': ['pawg', 'pawg erotic', ],
    'piercing': ['piercing erotic', ],
    'pigtails': ['pigtail fetish', ],
    'pissing': ['pissing fetish', 'pissing erotic'],
    'police': ['police porn', 'sexy police'],
    'pool': ['pool erotic', 'pool sex', ],
    'public': ['public erotic', 'public sex'],
    'pussy': ['pussy erotic', 'pussy close up'],
    'pussy licking': ['pussy licking', 'pussy licking erotic'],
    'redhead': ['redhead full body', 'redhead erotic'],
    'saggy tits': ['saggy tits', 'saggy tits erotic'],
    'schoolgirl': ['schoolgirl erotic', 'schoolgirl uniform'],
    'secretary': ['secretary', 'secretary erotic'],
    'selfie': ['selfie mirror', 'selfie erotic'],
    'shaved': ['shaved pussy erotic'],
    'shemale': ['shemale', 'shemale erotic'],
    'short hair': ['short hair full body', 'short hair erotic'],
    'shorts': ['shorts female body', 'short erotic'],
    'shower': ['shower erotic', 'shower sex'],
    'skinny': ['skinny erotic', 'skinny sex'],
    'skirt': ['skirt', 'skirt erotic'],
    'smoking': ['smoking erotic', 'smoking sex', 'smoking fetish'],
    'socks': ['socks erotic', 'socks porn'],
    'solo': ['solo porn', 'solo erotic'],
    'spreading': ['legs spreading', 'legs spreading erotic'],
    'squirting': ['squirt', 'squirting'],
    'ssbbw': ['ssbbw', 'ssbbw erotic', 'ssbbw fetish'],
    'stockings': ['stockings erotic', 'stockings fetish'],
    'strap on': ['strap on', 'strapon'],
    'swimsuit': ['swimsuit', 'swimsuit erotic'],
    'tattoo': ['tatoo erotic', 'tatoo sexy', 'female with tattoos'],
    'teen': ['teen erotic', 'teen sex'],
    'thick': ['thick', 'thick erotic'],
    'thong': ['thong erotic', ],
    'threesome': ['threesome', 'threesome erotic'],
    'tiny tits': ['tiny tits', 'flat chested'],
    'titjob': ['titjob', 'titjob erotic'],
    'tribbing': ['tribbing', 'tribbing porn'],
    'upskirt': ['upskirt porn', 'upskirt', 'upskirt erotic'],
    'yoga': ['yoga pants', 'yoga pants erotic'],
    'spooning': ['spooning sex position', 'spooning erotic'],
    '69': ['69 position', '69 erotic'],
    'transgender': ['transgender erotic', 'transgender porn']
}


async def fetch_image(session, image_url, file_path, sem, max_retries=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Check if file already exists
    if os.path.exists(file_path):
        print(f">>>>>>>>>>>>>>>>>> File {file_path} already exists. Skipping download.")
        return

    async with sem:
        for attempt in range(max_retries):
            try:
                async with session.get(image_url, headers=headers, timeout=30, ssl=True) as response:
                    if response.status == 403:
                        raise ClientResponseError(
                            request_info=response.request_info,
                            history=response.history,
                            status=response.status,
                            message='Forbidden'
                        )
                    response.raise_for_status()
                    with open(file_path, 'wb') as file:
                        file.write(await response.read())
                    print(f"Downloaded {file_path}")
                    break

            except ClientResponseError as e:
                if e.status == 403:
                    print(f"Attempt {attempt + 1}: Forbidden error for {file_path} - {e.message}")
                    if attempt < max_retries - 1:
                        await asyncio.sleep(2)  # Wait before retrying
                    else:
                        print(f"Failed to download {file_path} after {max_retries} attempts: {e.message}")
                else:
                    print(f"Failed to download {file_path}: {e}")
                    break

            except asyncio.TimeoutError:
                print(f"Attempt {attempt + 1}: Timeout error for {file_path}. Retrying...")
                if attempt < max_retries - 1:
                    await asyncio.sleep(2)  # Wait before retrying
                else:
                    print(f"Failed to download {file_path} after {max_retries} attempts due to timeout.")

            except aiohttp.ClientError as e:
                print(f"Failed to download {file_path}: {e}")
                break


async def download_images(key_folder, query, num_images=1000, output_dir='ddg_images'):
    query_dir = os.path.join(output_dir, key_folder.replace(' ', '_'))
    os.makedirs(query_dir, exist_ok=True)

    results = await DDGS().aimages(
        keywords=query,
        safesearch="off",
        max_results=num_images * 20,
    )

    sem = asyncio.Semaphore(100)  # Adjust this based on your system's capacity
    async with ClientSession(trust_env=True) as session:
        tasks = []
        for i, result in enumerate(results):
            image_url = result['image']

            PIU = Path(image_url.split('?')[0])

            if len(PIU.stem) > 50:
                PIU = PIU.with_name(PIU.stem[:50])

            file_path = Path(query_dir) / f"{PIU.stem}{PIU.suffix}"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            tasks.append(fetch_image(session, image_url, file_path.as_posix(), sem))
            if i >= num_images:
                break
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    # Example usage
    for i in range(10):
        for key_folder, query in search_queries.items():
            for Q in query:
                asyncio.run(download_images(key_folder, Q))
