
from fastapi import APIRouter


router = APIRouter()


@router.post("")
async def chat(conversation, request):
  print(conversation)
  print(request)

  return {"message": "Hello, World!"}


