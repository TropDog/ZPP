from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import logic

app = FastAPI()

@app.get("/from_disc/{file_name}")
def count_people_on_img(file_name: str):
    return logic.count_people_on_img(file_name)

@app.get("/files/{url_path:path}")
def count_people_on_img_url(url_path: str):
    return logic.count_people_on_img_from_url(url_path)


@app.post("/upload_jpg/")
async def create_upload_files(files: list[UploadFile] = File(...)):
    result = logic.save_images_and_count(files)
    return result

@app.get("/")
async def main():
    content = """
<body>
<form action="/upload_jpg/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</body>
    """
    return HTMLResponse(content=content)