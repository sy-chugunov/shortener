from logging import getLogger
from aiohttp import web

from shortener.utils import generate_short_id, get_url
from config import config
from db.queries import Queries

logger = getLogger(__name__)


class UrlHandler:
    def __init__(self):
        self._queries = Queries()

    async def shortify(self, request):
        data = await request.json()
        long_url = get_url(data)

        logger.info(f"Request to shortify url `{long_url}`")

        short_id = await self._queries.get_short_id(long_url)

        if not short_id:
            logger.info(
                f"`{long_url}` was not shortified before, generating new short id"
            )

            next_id = await self._queries.get_next_id()
            short_id = generate_short_id(next_id)

            await self._queries.add_url(short_id, long_url)

        short_url = f"http://{config.APP_HOST}:{config.APP_PORT}/{short_id}"

        logger.info(f"`{long_url}` short url `{short_url}`")

        return web.json_response({"short_url": short_url})

    async def redirect(self, request):
        short_id = request.match_info["short_id"]

        logger.info(f"Searching for long url by short id `{short_id}`")

        long_url = await self._queries.get_long_url(short_id)

        if not long_url:
            logger.warning(f"Long url not found by short id `{short_id}`")
            raise web.HTTPNotFound()

        logger.info(f"Redirecting to `{long_url}` by short id `{short_id}`")

        return web.HTTPFound(long_url)

    async def remove(self, request):
        short_id = request.match_info["short_id"]

        logger.info(f"Removing short id `{short_id}`")

        removed = await self._queries.remove_url(short_id)

        if not removed:
            logger.warning(f"Remove url: short id `{short_id}` not found")
            raise web.HTTPNotFound()

        logger.info(f"Url removed by short id `{short_id}`")

        return web.Response()
