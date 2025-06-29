import datetime
import asyncio
import httpx
from fastapi import APIRouter, Body
from src.database import scheduler_collection
from src.schemas.notice import NoticeSchema

router = APIRouter(tags=["Scheduler"])

scheduler_status = False


@router.on_event("startup")
async def start_scheduler():
    global scheduler_status
    if not scheduler_status:
        print('started')
        asyncio.create_task(check_time())
        scheduler_status = True


@router.post('/get_schedule/', summary="Get notice.")
async def get_schedule(notice: NoticeSchema):
    notice_data = {
        "body": notice.body,
        "type": notice.type,
        "callback": notice.callback,
        "status": notice.status
    }

    async with httpx.AsyncClient() as client:
        await client.post("http://127.0.0.1:8001/schedule/", json=notice_data)


@router.post('/schedule/', summary="Schedule notice.")
async def schedule(notice_data: dict = Body(...)):
    await scheduler_collection.insert_one(notice_data)

    return {"message": "Scheduled."}


async def check_time():
    while True:
        now = datetime.datetime.utcnow()
        try:
            notices = scheduler_collection.find({
                "status": False,
                "body.scheduled_at": {"$lte": now.isoformat()}
            })

            async for notice in notices:
                try:
                    async with httpx.AsyncClient() as client:
                        if notice["type"] == "post":
                            await client.post(notice["callback"],
                                              json=notice["body"])

                            await scheduler_collection.update_one({
                                "_id": notice["_id"]},
                                {"$set": {"status": True}}
                            )

                except Exception as exc:
                    print(f"Error: Unable to send a request. {exc}")

        except Exception as globalExc:
            print(f"Global error: Unable to send a request. {globalExc}")

        await asyncio.sleep(30)
