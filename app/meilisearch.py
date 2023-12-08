from meilisearch_python_sdk.errors import MeilisearchError
from meilisearch_python_sdk import AsyncClient
from app.utils import pagination_dict
from app.utils import get_settings
from app.errors import Abort
from app import constants


async def search(
    content_index,
    query=None,
    sort=None,
    page=None,
    filter=None,
    size=constants.SEARCH_RESULT_SIZE,
):
    settings = get_settings()

    try:
        async with AsyncClient(**settings.meilisearch) as client:
            index = client.index(content_index)

            result = await index.search(
                hits_per_page=size,
                filter=filter,
                query=query,
                sort=sort,
                page=page,
            )

            return {
                "pagination": pagination_dict(
                    result.total_hits, result.page, result.hits_per_page
                ),
                "list": result.hits,
            }

    except MeilisearchError:
        raise Abort("search", "query-down")
