from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
import uuid
import os

router = APIRouter()


@router.post("/mix", status_code=200)
async def upload_music(file: UploadFile):
    UPLOAD_DIR = "./music"
    content = await file.read()
    extension = file.filename.split(".")[1]
    origin = f"{str(uuid.uuid4())}.{extension}"
    with open(os.path.join(UPLOAD_DIR, origin), "wb") as fp:
        fp.write(content)

    after_mix = f"{str(uuid.uuid4())}.{extension}"
    with open(os.path.join(UPLOAD_DIR, after_mix), "wb") as fp:
        fp.write(content)
    return {"origin": origin, "after_mix": after_mix}


@router.get("/download/music/{filename}")
async def download_music(filename):
    UPLOAD_DIR = "./music"

    return FileResponse(os.path.join(UPLOAD_DIR, filename))
