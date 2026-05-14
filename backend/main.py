from groq import Groq
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
import os

apikey = None

#Convertir luego a unm arreglo de modelos
model = 'llama-3.3-70b-versatile'

def load_env():
    global apikey
    load_dotenv()
    apikey = os.getenv("GROQ_API_KEY")

load_env()


Client = Groq(api_key=apikey)

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "api funciona!"}








