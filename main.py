from fastapi import FastAPI
import uvicorn
from lib.getrand import result_generator

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Which country will win the world cup?"}


@app.get("/country/{country}")
async def myfruit(country: str):
    """Adds a fruit to random fruit"""

    chosen_random_fruit = result_generator(country)
    return {"The champion: ": chosen_random_fruit}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
