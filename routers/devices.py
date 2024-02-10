from fastapi import APIRouter

router = APIRouter(
    prefix="/devices"
)


@router.get("/")
async def list_devices():
    pass


@router.get("/{device_id")
async def get_device(device_id: int):
    pass
