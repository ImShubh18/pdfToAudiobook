import os

async def save_upload(file, folder: str) -> str:
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return file_path
