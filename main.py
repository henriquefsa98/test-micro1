from fastapi import FastAPI

app = FastAPI()


database: dict[str, int] = {}


@app.get("/")
async def vulnerable_function(name, age):

    try: 
        agevalidated = int(age)

        database[name] = agevalidated
        return {"message": f"User {name} inserted into database!"}

    except:
        return {"message": f"Error!!! The age input is not a valid integer!"}
