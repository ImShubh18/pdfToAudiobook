import asyncio
from backend.app.utils.file_utils import save_upload

class DummyFile:
    def __init__(self, content, name="test.pdf"):
        self.filename = name
        self.content = content
    async def read(self):
        return self.content

def test_save_upload():
    dummy = DummyFile(b"Hello World")
    path = asyncio.run(save_upload(dummy, "backend/temp"))
    assert path.endswith("test.pdf")
