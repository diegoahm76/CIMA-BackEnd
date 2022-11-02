from pydoc import describe
from unicodedata import name
from fastapi import FastAPI
import uvicorn
from routes.rios import rio

app = FastAPI(
    title="CIMA Api",
    description="Services for CIMA Api",
    version="0.0.1",
    openapi_tags=[{
        "name": "Rios",
        "description": "Services for to get rivers"
    }]
)

app.include_router(rio)

#For debugging with breakpoints
if __name__ == '__app__':
    uvicorn.run(app,host='0.0.0.0', port=8000)