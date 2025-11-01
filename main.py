from fastapi import FastAPI

app = FastAPI()

storage = {
    'statement': ''
}


@app.get("/api/v1/addition")
async def addition(a: float | int, b: float | int):
    return {"a": a, "b": b, "result": a + b}


@app.get("/api/v1/subtraction")
async def subtraction(a: float | int, b: float | int):
    return {"a": a, "b": b, "result": a - b}


@app.get("/api/v1/multiplication")
async def multiplication(a: float | int, b: float | int):
    return {"a": a, "b": b, "result": a * b}


@app.get("/api/v1/division")
async def division(a: float | int, b: float | int):
    if b == 0.0:
        return {"err": "cannot divide by 0"}
    return {"a": a, "b": b, "result": a / b}


@app.get("/api/v1/statement/get")
async def statement_get():
    return {"statement": storage["statement"]}


@app.get("/api/v1/statement/del")
async def statement_del():
    storage["statement"] = ''
    return {"statement": storage["statement"]}


@app.get("/api/v1/statement/set")
async def statement_set(a: str, op: str, b: str):
    storage["statement"] = f"{a} {op} {b}"
    return {"statement": storage["statement"], "success": "ok"}


@app.get("/api/v1/statement/calc")
async def statement_set(a: str, op: str, b: str):
    storage["statement"] = f"{a} {op} {b}"
    return statement_raw(storage["statement"])


@app.get("/api/v1/statement/raw")
async def statement_raw(statement: str):
    storage["statement"] = ''
    try:
        result = eval(statement)
        return {"statement": statement, "result": result}
    except Exception as err:
        return {"err": err}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

