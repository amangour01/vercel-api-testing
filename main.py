# import uvicorn
# from fastapi import FastAPI, Query, HTTPException
# from typing import Optional, List
# from fastapi.middleware.cors import CORSMiddleware
# import json,request
# import jsonify

# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

# # Load student information from the JSON file
# with open('q-vercel-python.json', 'r') as f:
#     student_marks = json.load(f)

# # @app.get("/api")
# # async def get_marks(name: List[str] = Query(...)):
#     # if not name:
#     #     raise HTTPException(status_code=400, detail="Query parameter 'name' is required")
    
#     # marks = []
#     # for student_name in name:
#     #     student = next((s for s in student_marks if s["name"] == student_name), None)
#     #     if student:
#     #         marks.append(student["marks"])
#     # return {"marks": marks}

# @app.get("/api")
# def get_marks():
#     names = request.args.getlist('name')    
#     marks = []
#     for name in names:
#         # Iterate over students list and check if the student's name matches
#         student_found = False
#         for student in students:
#             if student.get('name') == name:
#                 marks.append(student.get('marks', "Marks not found"))
#                 student_found = True
#                 break
        
#         if not student_found:
#             marks.append("Student not found")
    
#     return jsonify({"marks": marks})

# @app.get("/")
# def read_root():
#     return {"message": "Hello from FastAPI!"}

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

# os.environ.get('54367')

app = Flask(__name__)
CORS(app)  # Enable CORS to allow GET requests from any origin

# Load student data from the JSON file
with open("q-vercel-python.json") as f:
    students = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get names from query parameters
    names = request.args.getlist('name')
    
    # Retrieve the marks for the provided names
    marks = []
    for name in names:
        # Iterate over students list and check if the student's name matches
        student_found = False
        for student in students:
            if student.get('name') == name:
                marks.append(student.get('marks', "Marks not found"))
                student_found = True
                break
        
        if not student_found:
            marks.append("Student not found")
    
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
