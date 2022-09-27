from typing import Any, Dict, List, Union
from pydantic import BaseModel

class EMail(BaseModel):
    email: Union[List,Dict,Any]=None
