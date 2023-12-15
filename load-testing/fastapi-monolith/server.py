from fastapi import FastAPI
import asyncio


app = FastAPI()

# Function to simulate a delay
async def sleep(seconds):
    await asyncio.sleep(seconds)

# # Route 1
# @app.get('/route1')
# async def route1():
#     await sleep(1)
#     return {"message": "Response from Route 1"}

# Route 2
@app.get('/route2')
async def route2():
    await sleep(2)
    return {"message": "Response from Route 2"}

# # Route 3
# @app.get('/route3')
# async def route3():
#     await sleep(3)
#     return {"message": "Response from Route 3"}
