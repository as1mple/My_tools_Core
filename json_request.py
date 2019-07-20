import aiohttp as aiohttp
from requests import Session
import response.json as res


def fetch(url: str, session: Session) -> res:
    with session.get(url, params={
        # "checkin": CHECKIN,
        # "los": LOS, "hotel_id": ID,
        # 'adults': 2},
    },
                     timeout=10) as response:
        try:
            response = response.json()
        except aiohttp.client_exceptions.ContentTypeError as io:
            print(io)
            return 0
        return response
