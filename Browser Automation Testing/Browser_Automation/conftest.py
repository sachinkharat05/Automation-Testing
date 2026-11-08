
import pytest
import threading
from werkzeug.serving import make_server
from app import app, users


@pytest.fixture
def base_url():

    users.clear()
    server = make_server("127.0.0.1", 0, app)

    thread = threading.Thread(
        target=server.serve_forever,daemon=True)

    thread.start()

    yield f"http://127.0.0.1:{server.server_port}"

    server.shutdown()
    thread.join()
    server.server_close()

    users.clear()
