class BookingFlow:
    def __init__(self, depart_station, arrive_station, book_ticket_date, depart_time, ticket_amount, end_time, national_ID, phonenumber, email, to_go_account):
        self.depart_station = depart_station
        self.arrive_station = arrive_station
        self.book_ticket_date = book_ticket_date
        self.depart_time = depart_time
        self.ticket_amount = ticket_amount
        self.end_time = end_time
        self.national_ID = national_ID
        self.phonenumber = phonenumber
        self.email = email
        self.to_go_account = to_go_account
        self.ticket = None  # 定票代碼
    
    def run(self):
        return {"Hello": "World"}
    
