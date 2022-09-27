
from pydantic import BaseModel

class t4_data_model(BaseModel):
    meeting_id:str = None
    meeting_attendees:str = None
    meeting_start_datetime:str = None
    meeting_end_datetime:str = None
    is_online:bool = None
    organizer:str = None
    

