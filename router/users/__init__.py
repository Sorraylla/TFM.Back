from fastapi import APIRouter

router = APIRouter(tags=["users"], prefix="/users")


@router.get("/")
def read_root():
    return {"Hello": "World"}