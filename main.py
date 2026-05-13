from fastapi import FastAPI, Path, HTTPException, status, Query
import json

app=FastAPI()

def load_data():
    with open('patients_info.json','r') as f:
        data = json.load(f)
    return data
        
@app.get('/')
def hello():
    return {'message':'Patient Management System API.'}

@app.get('/view')
def view():
    data=load_data()
    return data

@app.get('/view_patient/{ID}')
def view_patient(ID: str = Path(..., description='Patient Id', example='PAT001')):
    data = load_data()
    
    # Check if the patient ID actually exists
    if ID not in data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Patient with ID {ID} not found"
        )
    return data[ID]

@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description='sort data by height, weight or BMI.'), order: str = Query('asc',descrition='Sort order: asc or desc.')):

    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key= lambda x:x[sort_by], reverse=sort_order)
    return sorted_data
    