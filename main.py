from fastapi import FastAPI

app = FastAPI()


database: dict[str, int] = {}


@app.get("/")
async def vulnerable_function(name, age):

    database[name] = age
    return {"message": f"User {name} inserted into database!"}
