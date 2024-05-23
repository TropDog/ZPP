from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import logic, uuid, pika, json



app = FastAPI()

@app.get("/from_disc/{file_name}")
def count_people_on_img(file_name: str):
    return logic.count_people_on_img(file_name)

@app.get("/no_rabbit/{url_path:path}")
def count_people_on_img_url(url_path: str):
    img_id = str(uuid.uuid4())
    return logic.count_people_on_img_from_url(url_path, img_id)

@app.get("/with_rabbit/{url_path:path}")
def count_people_on_img_url(url_path: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
    channel = connection.channel()
    channel.queue_declare(queue='img_processing')
    img_id = str(uuid.uuid4())
    api_result = json.dumps({img_id: url_path})

    channel.basic_publish(exchange='',
                routing_key='img_processing',
                body=api_result)
    
    connection.close()
    return {'request id' : img_id}

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