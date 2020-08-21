import asyncio
import logging

from aiohttp import web

from routes import setup_routes


def main():
    try:
        app = web.Application()
        setup_routes(app)
        web.run_app(app, host='localhost', port=8888)

    except KeyboardInterrupt:
        logging.info("SIGINT received")


if __name__ == '__main__':
    logging.basicConfig(format='<%(levelname)s>: %(message)s |%(filename)s:%(lineno)d|%(threadName)s',
                        level=logging.DEBUG)
    import sys
    logging.info(f"Python version: {sys.version}")
    assert sys.version_info.major == 3 and sys.version_info.minor >= 7

    try:
        main()
    except (asyncio.CancelledError, KeyboardInterrupt):
        logging.info("Client tasks cancelled")
