import uvicorn
from fastapi import FastAPI

from app.routes import processing_routes, search_routes

# Create the FastAPI application
app = FastAPI(
    title='SILVA Medical :: Tesseract',
    version='0.1.0'
)

# Add the routes
app.include_router(processing_routes.router)
app.include_router(search_routes.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
