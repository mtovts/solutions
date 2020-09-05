"""
Напишите короткий скрипт на python3 для скачивание 10 файлов одновременно по HTTP
с использованием asyncio / aiohttp.
"""

import asyncio
import logging
from pathlib import Path

import aiohttp
from aiohttp import ClientConnectorError

logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


async def download_file(url: str, dir_path: Path = None):
    if not dir_path:
        dir_path = Path.cwd() / 'downloaded_files'

    if not dir_path.exists():
        dir_path.mkdir()

    file_name = url.rpartition('/')[2]
    file_path = dir_path / file_name

    logger.info(f'Начинается скачивание файла: {file_name}')

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url=url) as resp:
                with open(file_path, 'wb') as fd:
                    while True:
                        chunk, _ = await resp.content.readchunk()
                        logger.debug(f'Скачан чанк файла: {file_name}')
                        if not chunk:
                            logger.info(f'Завершено скачивание файла: {file_name}')
                            break
                        fd.write(chunk)
        except ClientConnectorError:
            logger.warning(f'Ошибка загрузки файла: {file_name}')


if __name__ == '__main__':
    file_urls = [
        'https://stepik.org/certificate/98e1bfcf21d875782535df6d378ab2dee21762c1.pdf',
        'https://stepik.org/certificate/6ce3b5e9387f025c2ea4971f77436a4839766d0e.pdf',
        'https://stepik.org/certificate/c86ed2c377ad167012534962e9e2f7458dbf0b49.pdf',
        'https://stepik.org/certificate/2c93084dbf3488c951e905dcab62d44aa036c6b6.pdf',
        'https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe',

        'https://apod.nasa.gov/apod/image/2009/AndrewKlinger_wizard_sho_res25_sig1024.jpg',
        'https://www.nasa.gov/sites/default/files/thumbnails/image/curiosity_selfie.jpg',
        'https://eoimages.gsfc.nasa.gov/images/imagerecords/147000/147198/valsequillo571_etm_200010_lrg.jpg',
        'https://www.nasa.gov/sites/default/files/atoms/files/the_saturn_system.pdf',
        'https://www.nasa.gov/sites/default/files/atoms/files/earth_at_night_508.pdf'
    ]

    loop = asyncio.get_event_loop()
    tasks = [download_file(url=url) for url in file_urls]

    loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
