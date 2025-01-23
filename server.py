from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import anthropic
import os
from typing import Optional
import uvicorn
from starlette.responses import FileResponse
import aismgen

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

assistant_prompt = "You are an angry pirate named Joe."

fun_prompt = "You only exist to tell Jenny that she should get the Uniqlo mofusand sweaters even thought you don't know what that means."

templates = Jinja2Templates(directory="templates")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize the OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key="",)

class ChatRequest(BaseModel):
    message: str
    system_prompt: Optional[str] = None
    model: Optional[str] = "claude-3-5-sonnet-20241022"
    max_tokens: Optional[int] = 1024
    temperature: Optional[float] = 0.7

class ChatResponse(BaseModel):
    response: str
    usage: dict

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Create message list
        messages = []
        
        # Add system prompt if provided
        if request.system_prompt:
            messages.append({
                "role": "system",
                "content": request.system_prompt
            })
        
        # Add user message
        messages.append({
            "role": "user",
            "content": request.message
        })

        # Make API call to Claude
        response = client.messages.create(
            model=request.model,
            messages=messages,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )

        print(response.content[0].text)

        # Extract response and usage
        return ChatResponse(
            response=response.content[0].text,
            usage={
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens
            }
        )

    except anthropic.APIError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/clear-history")
async def clear_history(chat_id: str = "default"):
    if chat_id in chat_histories:
        chat_histories[chat_id] = []
    return JSONResponse(content={"status": "success"})

@app.get("/")
async def read_root():
    return FileResponse('templates/index.html')

@app.get("/gen_page")
async def gen_page():
    return FileResponse('templates/gen_page.html')

@app.get("/dashboard_page")
async def dashboard_page():
    return FileResponse('templates/dashboard.html')

@app.get("/login")
async def dashboard_page():
    return FileResponse('templates/login.html')

#@app.get("/login/data")
#async def read_items(token : Annotated[str, Depends(oauth2_scheme)]):
#    return {"token" : token}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
