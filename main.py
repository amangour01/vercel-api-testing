import uvicorn
from fastapi import FastAPI, Query, HTTPException
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load student information from the JSON file
with open('q-vercel-python.json', 'r') as f:
    student_marks = json.load(f)

@app.get("/api")
async def get_marks(name: List[str] = Query(None)):
    if not name:
        raise HTTPException(status_code=400, detail="Query parameter 'name' is required")
    
    marks = []
    for student_name in name:
        student = next((s for s in student_marks if s["name"] == student_name), None)
        if student:
            marks.append(student["marks"])
        else:
            marks.append(None)
    return {"marks": marks}

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8002)
