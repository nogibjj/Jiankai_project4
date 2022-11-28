from fastapi import FastAPI
import uvicorn
from lib.getrand import result_generator

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Functions From Zero 2"}

@app.get("/fruits/{fruit}")
async def myfruit(fruit: str):
    """Adds a fruit to random fruit"""

    chosen_random_fruit = result_generator(fruit)
    return {"random_fruit": chosen_random_fruit}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')