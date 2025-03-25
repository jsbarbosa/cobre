from fastapi import APIRouter
from .serializers import GetScorePost
from app.core.handler import calculate_score


router = APIRouter()


@router.post("/evaluate", tags=["Score"])
async def get_score(request: GetScorePost):
    score = calculate_score(
        request.identity.dict(),
        request.transaction.dict()
    )

    return score
    

@router.post("/notify/slack", tags=["Notification"])
async def notify_slack(document: str):
    pass

