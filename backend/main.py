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


test_message = input("Write anything")
response = Client.chat.completions.create(model = model,
                                           messages = [{"role": "user", "content": test_message}],
                                          temperature=0.1,
                                          max_tokens = 800)

print(response.choices[0].message.content)


@app.route("/chat", methods = ["POST"])
def chat():
    pass








