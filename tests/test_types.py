from lyra.llm.types import Message, TextDelta, ToolCallEvent, ToolCall, Done
from pydantic import ValidationError
import pytest

def test_instances():
    cases = [
        (Message(name="test", role="tool"), Message),
        (ToolCall(name="app", arguments={}), ToolCall),
        (ToolCallEvent(call=ToolCall(name="test", arguments={})), ToolCallEvent),
        (TextDelta(text="test"), TextDelta),
        (Done(), Done),
    ]
    for instance, expected in cases:
        assert isinstance(instance, expected)

def test_invalid():
    with pytest.raises(ValidationError):
        Message(role="banana", content="x")

def test_optional():
    msg = Message(role="assistant")
    assert isinstance(msg, Message)
    assert msg.content == ""
    assert msg.tool_calls == []

def test_tool_name_too_long():
    with pytest.raises(ValidationError):
        ToolCall(name="x" * 65, arguments={})

def test_event_holds_call():
    event = ToolCallEvent(call=ToolCall(name="open_app", arguments={"app": "notepad"}))
    assert event.call.name == "open_app"
    assert event.call.arguments["app"] == "notepad"