from fastapi import FastAPI, APIRouter
import uvicorn
from run import Run
import logging

logging.basicConfig(level = logging.INFO)

app = FastAPI(
    title = "Generate Image",
    description = "Use Stable Diffusion LoRA to generate and image that looks like pixel art.",
    summary="Practice project by Abdias Baldiviezo.",
    version="0.0.1",
    contact={
        "name": "Abdias Baldiviezo",
        "url": "https://abadias618.github.io",
        "email": "abadias618@gmail.com",
    },
)
router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/test")
async def home():
    return {"message": "This service generates pixel art from a prompt"}

@router.post("/generate-pixel-img")
async def data(data: dict):
    try:
        run = Run()
        input_text = data["text"]
        res = run.run(input_text)
        return res
    except Exception as e:
        logging.log.error("Something messed up")
        
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=6000, host="0.0.0.0")