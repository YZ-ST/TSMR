from typing import Union
from fastapi import FastAPI, Depends
from modules import logger
from modules import verify_token
from modules import configs

from controller.booking_flow import BookingFlow

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/Booking_TSMR")
def Booking_TSMR(
    depart_station: str = "台北", 
    arrive_station: str = "台中", 
    book_ticket_date: str = "2023-12-25", 
    depart_time: str = "13:30", 
    ticket_amount: int = 1,
    end_time: str = "15:30",
    national_ID: str = "A123456789",
    phonenumber: str = "0983636056",
    email: str = "pp0975320034@gmail.com",
    to_go_account: str = None,
):
    try:
        logger.info(f"depart_station= {depart_station}")
        logger.info(f"arrive_station= {arrive_station}")
        logger.info(f"book_ticket_date= {book_ticket_date}")
        logger.info(f"depart_time= {depart_time}")
        logger.info(f"ticket_amount= {ticket_amount}")
        logger.info(f"end_time= {end_time}")
        logger.info(f"national_ID= {national_ID}")
        logger.info(f"phonenumber= {phonenumber}")
        logger.info(f"email= {email}")
        logger.info(f"to_go_account= {to_go_account}")
        booking = BookingFlow(depart_station, arrive_station, book_ticket_date, depart_time, ticket_amount, end_time, national_ID, phonenumber, email, to_go_account)
        return booking.Hello()
    except Exception as e:
        logger.error(e)
        


