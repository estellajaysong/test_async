from time import sleep
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def background_job():
    print('start background job')
    sleep(300)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/job")
async def start_job(background_tasks: BackgroundTasks):
    background_tasks.add_task(background_job)
    return {"Background job": "Started"}
