from fastapi import FastAPI
import uvicorn
from routes.tree_api import tree
from routes.typeValues_api import typeValues
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CIMA Api",
    description="Services for CIMA Api",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "Trees",
            "description": "Services for to get trees"
        },
        {
            "name": "TypeValues",
            "description": "Services for to get typeValues"
        }
    ]
)

origins = [
    "http://localhost:4201",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tree)
app.include_router(typeValues)

#For debugging with breakpoints
if __name__ == '__app__':
    uvicorn.run(app,host='0.0.0.0', port=8000)