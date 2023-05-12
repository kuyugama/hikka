from app.utils import pagination_dict, pagination
from .dependencies import validate_search_anime
from fastapi import APIRouter, Depends
from .schemas import AnimeSearchArgs
from app.models import Anime


router = APIRouter(prefix="/search")


@router.post("/anime")
async def search_anime(
    search: AnimeSearchArgs = Depends(validate_search_anime),
):
    query = Anime.filter().order_by("-score", "-scored_by")

    total = await query.count()
    limit, offset, size = pagination(search.page)

    anime_list = await query.limit(limit).offset(offset)

    result = [
        {
            "media_type": anime.media_type,
            "scored_by": anime.scored_by,
            "title_ua": anime.title_ua,
            "title_en": anime.title_en,
            "title_ja": anime.title_ja,
            "score": anime.score,
            "slug": anime.slug,
        }
        for anime in anime_list
    ]

    return {
        "pagination": pagination_dict(total, search.page, size),
        "list": result,
    }