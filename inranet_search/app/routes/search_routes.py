from fastapi import APIRouter

from app.services.store_service import store_service

router = APIRouter(
    prefix='/search'
)


@router.get('')
async def search(q: str) -> list[int]:
    results = store_service.search(q)
    return list(set([r['file_external_id'] for r in results]))
