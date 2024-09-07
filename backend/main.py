from fastapi import FastAPI,Response
from starlette.middleware.cors import CORSMiddleware
import classification_model as classificator
import uvicorn

app = FastAPI()
PORT=5555
origins=[
    "http://localhost",
    "http://localhost:4200"
]

app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
@app.get("/health_check",status_code=200)
def read_hc():
    return {"status":"OK"}

@app.post("/prediction",status_code=200)
def read_review(query: classificator.HealthData, response: Response):
    if (query is None):
        response.status_code=500
        return {"status":"Error"}
    else:
        try:
            p= classificator.predictResult(query)
            return p
        except Exception as e:
            response.status_code = 500
            return {"status":"Error"}


if __name__=="__main__":
    uvicorn.run("main:app",port=PORT)
