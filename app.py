


from download import download
from movies import movieLinks
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
import uvicorn

def downloader():
    links = movieLinks()
    
    for link in links:
        download(link)


scheduler = BackgroundScheduler()
scheduler.add_job(
    downloader,
    "interval",
    days=1,
)

app = FastAPI()

@app.on_event("startup")
def start():
    scheduler.start()
    print("**** startup ****")


@app.on_event("shutdown")
def shutdown():
    scheduler.shutdown()
    print("**** shutdown ****")



if __name__ == "__main__":
    uvicorn.run(app="app:app", host="127.0.0.1", port=8000)
    