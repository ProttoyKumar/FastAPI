from fastapi import FastAPI

app=FastAPI()

foods={'Indian':['Bhatura','Chaat'],
       'Bengali':['Mutton Curry','Macher Jhol'],
       'Chinese':['Dumplings','Tofu']}

@app.get('/get_items/{cuisine}') 
async def get_items(cuisine):
    return foods.get(cuisine)

discount={1:'10%', 2:'15%', 3:'20%'}

@app.get('/cupon/{code}')
async def cupon_code(code: int):
    return discount.get(code)