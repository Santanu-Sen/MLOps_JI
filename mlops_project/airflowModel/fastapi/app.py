from fastapi import FastAPI, HTTPException
from main import main  # Import the main function from main.py

app = FastAPI()

@app.get("/anuvad")
async def read_root():
    # Call the main function from main.py
    result = main()
    return result
