from fastapi import APIRouter
import routes.music as music

router = APIRouter()

# router config
router.include_router(music.router)
