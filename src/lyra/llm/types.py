from pydantic import BaseModel, Field, TypeAdapter
from typing import Literal

class ToolCall(BaseModel):
    name: str = Field(max_length=64)
    arguments: dict

class Message(BaseModel):
    name: str | None = None
    role: Literal["system", "user", "assistant", "tool"]
    images: list[bytes] = []
    content: str = ""
    tool_calls: list[ToolCall]  = []

class TextDelta(BaseModel):
    text: str

class ToolCallEvent(BaseModel):
    call: ToolCall

class Done(BaseModel):
    pass 

Event = TextDelta | ToolCallEvent | Done
