import asyncio
import logging

from aiohttp import web

from shortener.routes import setup_routes
from shortener.views import UrlHandler
from config import config
from db.schema import create_tables


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def on_startup(app):
    await create_tables()

def init():
    logger.info('Init application')

    app = web.Application()
    handler = UrlHandler()

    setup_routes(app, handler)
    app.on_startup.append(on_startup)

    return app, config.APP_HOST, config.APP_PORT


if __name__ == '__main__':
    app, host, port = init()

    logger.info('Run application')

    web.run_app(app, host=host, port=port, access_log=None)
