from fastapi import FastAPI
import logic

app = FastAPI()

@app.get("/serialized_data/{file_name}")
def return_movies_data(file_name: str):
    json = logic.serialized_data(file_name)
    return json
