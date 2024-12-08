import asyncio
from app import create_app
from asgiref.wsgi import WsgiToAsgi
import uvicorn

async def main():
    app = await create_app()  # Your Flask app
    asgi_app = WsgiToAsgi(app)  # Wrap Flask app to make it ASGI compatible
    config = uvicorn.Config(asgi_app, host="127.0.0.1", port=5000, loop="asyncio")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:  # Handle 'already running event loop'
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
