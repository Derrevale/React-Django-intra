from fastapi import APIRouter

from app.services.store_service import store_service

# Create the router for search
router = APIRouter(
    prefix='/search'
)


@router.get('')
async def search(q: str) -> list[int]:
    """
    Searches for a given query in the database.
    :param q: the query to search for.
    :return: the list of external ids that match the query.
    """

    # Search for the query within the data store
    results = store_service.search(q)
    # Return the list of external ids
    return list(set([r['file_external_id'] for r in results]))
