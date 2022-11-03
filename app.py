from fastapi import FastAPI
import uvicorn
from routes.tree_api import tree

app = FastAPI(
    title="CIMA Api",
    description="Services for CIMA Api",
    version="0.0.1",
    openapi_tags=[{
        "name": "Trees",
        "description": "Services for to get trees"
    }]
)

app.include_router(tree)

#For debugging with breakpoints
if __name__ == '__app__':
    uvicorn.run(app,host='0.0.0.0', port=8000)