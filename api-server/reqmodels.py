from pydantic import BaseModel, Field, constr
from typing import List, Type
import inspect
from fastapi import Form

# def as_form(cls: Type[BaseModel]):
#     """
#     Adds an as_form class method to decorated models. The as_form class method
#     can be used with FastAPI endpoints
#     """
#     new_params = [
#         inspect.Parameter(
#             field.alias,
#             inspect.Parameter.POSITIONAL_ONLY,
#             default=(Form(field.default) if not field.required else Form(...)),
#             annotation=field.outer_type_,
#         )
#         for field in cls.__fields__.values()
#     ]

#     async def _as_form(**data):
#         return cls(**data)

#     sig = inspect.signature(_as_form)
#     sig = sig.replace(parameters=new_params)
#     _as_form.__signature__ = sig
#     setattr(cls, "as_form", _as_form)
#     return cls

# @as_form
class QlOptionsReq(BaseModel):
    database: str
    option: int = Field(..., ge=1, le=2)
    category: int = Field(None, ge=1, le=5)
    custom_query: int = Field(None, ge=1, le=4)
    source: str = None
    source_index: str = None
    sink: str = None
    sink_index: str = None
    taint: str = None