from starlette import status
from fastapi import APIRouter
from .serializers import GetScorePost
from starlette.responses import JSONResponse
from app.config.settings import NOTIFY_THRESHOLD
from app.core.handler import ScoreHandler, send_slack_alert


router = APIRouter()


@router.post("/evaluate", tags=["Score"])
async def get_score(notify: bool, request: GetScorePost):
    try:
        score = ScoreHandler.run(
            transaction_id=request.transaction_id,
            identity=request.identity.dict(),
            transaction=request.transaction.dict()
        )
        
        if notify and score['score'] > NOTIFY_THRESHOLD:
            send_slack_alert(
                f'Potential fraudulent transaction. Please check transaction {request.transaction_id}'
            )
        
        return score
        
    except Exception as e:
        return JSONResponse(
            status_code=status. HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                'exception': str(e)
            }
        )
        

@router.post("/notify/slack", tags=["Notification"])
async def notify_slack(message: str):
    try:
        response = send_slack_alert(message)
        
        return JSONResponse(
            status_code=response['status'],
            content=response
        )
        
    except Exception as e:
        return JSONResponse(
            status_code=status. HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                'exception': str(e)
            }
        )
