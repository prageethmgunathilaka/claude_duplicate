
# Tests for Claude Duplicate
import pytest
from claude_duplicate import Assistant

def test_assistant_init():
    assistant = Assistant()
    assert assistant.model_name == 'gpt-3.5-turbo'
    assert assistant.conversation_history == []

def test_query_processing():
    assistant = Assistant()
    response = assistant.process('Hello')
    assert isinstance(response, str)
    assert 'Hello' in response
