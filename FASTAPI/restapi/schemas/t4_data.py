from sqlalchemy import JSON,Boolean,Table,Column,Date,String
from typing import List
from sqlalchemy import Boolean,Table,Column,Date,String,Integer
from database.database import conn,meta,db_engine

t4_data = Table(
    't4_data',meta,
    Column("id",Integer,primary_key=True),
    Column("meeting_id",String(255)),
    Column("meeting_attendees",JSON),
    Column("meeting_start_datetime",String(255)),
    Column("meeting_end_datetime",String(255)),
    Column("is_online",Boolean(32)),
    Column("organizer",String(32)),
)
meta.create_all(db_engine)

# t4_data = Table(
#     't4_data',meta,
#     Column("id",Integer,primary_key=True),
#     Column("meeting_id",String(255)),
#     Column("meeting_attendees",String(255)),
#     Column("meeting_start_datetime",String(255)),
#     Column("meeting_end_datetime",String(255)),
#     Column("is_online",Boolean(32)),
#     Column("organizer",String(32)),
# )


#val=(r.data.camera,r.data.device_ip,str(r.data.frame_uuid),"bugun",
#str(savePath),str(savePath),r2.events.coordinates,r2.events.payload)

#val=(r.data.camera,r.data.device_ip,str(r.data.frame_uuid),"bugun",
#str(savePath),str(savePath),r2.events.coordinates,r2.events.payload)