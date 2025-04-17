from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from markitdown import convert

app = FastAPI()

class URLInput(BaseModel):
    url: str

@app.post("/v1/markitdown")
async def markitdown_endpoint(url_input: URLInput):
    try:
        markdown_content = convert(url_input.url)
        return Response(markdown_content, media_type="text/markdown")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
