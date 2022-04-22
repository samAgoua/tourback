from fastapi import FastAPI
from pharmacie.models import Pharmacie


app = FastAPI()

@app.post("/pharmacie/", response_model=Pharmacie)
async def post_pharm(pharmacie: Pharmacie):
    res = await pharmacie.save()
    return res

@app.get("/pharmacie/", response_model=list[Pharmacie])
async def getAll_pharm():
    return await Pharmacie.objects.all()

@app.get("/pharmacie/{id}", response_model=Pharmacie)
async def getOne_pharm(id: int):
    return await Pharmacie.objects.get(id=id)




