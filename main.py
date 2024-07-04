from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from router.users import router as router_users
from router.readMolecules import router as router_molecules
from router.convertMolecules import router as router_convert_molecules
from router.searchSubstructures import router as router_search_substructures
from router.chemistryTransformations import router as router_chemistry_transformations
app = FastAPI()

origins = [
    "http://localhost:8080",  # Ajusta esto al puerto y host de tu frontend Vue.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Métodos HTTP permitidos
    allow_headers=["*"],  # Cabeceras HTTP permitidas
)
app.include_router(router_users)
app.include_router(router_molecules)
app.include_router(router_convert_molecules)
app.include_router(router_search_substructures)
app.include_router(router_chemistry_transformations)
