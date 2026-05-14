from groq import Groq
from fastapi import FastAPI
from dotenv import load_dotenv
import os

apikey = None

def load_env():
    global apikey
    load_dotenv()
    apikey = os.getenv("GROQ_API_KEY")

load_env()

Client = Groq(api_key=apikey)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "api funciona!"}
