from fastapi import APIRouter,FastAPI
import requests
from database.database import conn
from fastapi.responses import JSONResponse
from schemas.t4_data import t4_data
import json
from typing import Any, Dict, List, Union
from datetime import datetime


app = FastAPI()
t = APIRouter()



@t.post('/v1/t4/upload/')
async def user_save(items:Union[List,Dict,Any]=None):

    db_get_data=conn.execute(t4_data.select()).fetchall()
    # print(len(db_get_data))
    if (len(db_get_data))>0:
        conn.execute(t4_data.delete().where(t4_data.c.id > 0))
    for i in items['data']:
        conn.execute(t4_data.insert().values(
            meeting_id= i['meeting_id'],
            meeting_attendees= i['meeting_attendees'],
            meeting_start_datetime = i['meeting_start_datetime'],
            meeting_end_datetime= i['meeting_end_datetime'],
            is_online = i['is_online'],
            organizer= i['organizer'], 
        ))
    return JSONResponse({'status':'ok'}),200



@t.post('/v1/t4/email')
async def root(data: Union[List,Dict,Any]=None):
    dicts=[]
    new=[]
    totalSecs = 0
    totalSecs2=0
    req=conn.execute(t4_data.select().where(t4_data.c.organizer == str(data['email']))).fetchall()
    for i in range(len(req)):
        start_datetime_object = datetime.strptime(req[i][3], '%Y-%m-%d %H:%M')
        finish_datetime_object =datetime.strptime(req[i][4], '%Y-%m-%d %H:%M')
        fark=finish_datetime_object-start_datetime_object
        res={
            'date':str(start_datetime_object)[:10],
            'time':str(fark)
            }
        dicts.append(res)
        # print('')
    print(dicts)
    for i in range(len(dicts)):
        for j in range(len(dicts)):
            if i != j:
                if dicts[i]['date']==dicts[j]['date']:
                    timeParts = [int(s) for s in (dicts[i]['time']).split(':')]
                    timeParts2 = [int(s) for s in (dicts[j]['time']).split(':')]
                    totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
                    totalSecs2 += (timeParts2[0] * 60 + timeParts2[1]) * 60 + timeParts2[2]
                    total=(totalSecs+totalSecs2)
                    total, sec = divmod(total, 60)
                    hr, min = divmod(total, 60)
                    new_dict={
                        'date':dicts[i]['date'],
                        'time':(hr, min, sec)
                    }
                    # print(new_dict)
                    new.append(new_dict)
                    totalSecs=0
                    totalSecs2=0
    return JSONResponse({'status':json.dumps(new)}),200


@t.post('/v1/t4/meet')
async def get_meet(data: Union[List,Dict,Any]=None):
    sayac=0
    db_get_data=conn.execute(t4_data.select()).fetchall()
    # print(db_get_data)
    for i in range(len(db_get_data)):
        # print(str(db_get_data[i][3]), data['date'])
        if str(db_get_data[i][3]) == str(data['date']) or str(db_get_data[i][4]) == str(data['date']):
            print(len(db_get_data[i][2]))
            for j in range(len(db_get_data[i][2])):
                if (db_get_data[i][2][j]) == data['email']:
                    sayac+=1
        print(i)
    
    return "{'status':çakışma mevcut}" if sayac > 1 else "{'status':çakışma mevcut değildir.}"




@t.post('/v1/t4/update/')
async def get_month(data:Union[List,Dict,Any]=None):
    
    db_get_data=conn.execute(t4_data.select()).fetchall()
    print(type(db_get_data))
    # results_as_dict = db_get_data.mappings().all()
    # print(results_as_dict)
    for i in range(len(data['data'])):
        for j in range(len(db_get_data)):
            print(data['data'][i]['meeting_id'])
            print(db_get_data[j][1])
            if data['data'][i]['meeting_id'] == db_get_data[j][1]:
                print('a')
                conn.execute(t4_data.update().where(t4_data.c.meeting_id == data['data'][i]['meeting_id']).set(
                        meeting_attendees= db_get_data[j][2],
                        meeting_start_datetime = db_get_data[j][3],
                        meeting_end_datetime= db_get_data[j][4],
                        is_online = db_get_data[j][5],
                        organizer= db_get_data[j][6], 
                ))

          

    return JSONResponse({'status':'ok'}),200





