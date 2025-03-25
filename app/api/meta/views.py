from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse


router = APIRouter()


@router.get("/", tags=["Meta"])
async def root():
    return {
        "service": "Fraud scoring",
        "status": "Ready"
    }


@router.get("/version", tags=["Meta"])
async def version():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "version": 0.1,
        }
    )


@router.get("/health", tags=["Meta"])
async def health_check():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "ok"}
    )

