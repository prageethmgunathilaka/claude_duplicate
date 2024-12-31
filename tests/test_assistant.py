import pytest
from claude_duplicate import Assistant
from claude_duplicate.web_search import search
from claude_duplicate.code_generator import generate_code

def test_assistant_init():
    assistant = Assistant()
    assert assistant.model_name == 'gpt-3.5-turbo'
    assert assistant.conversation_history == []

def test_query_processing():
    assistant = Assistant()
    response = assistant.process('Hello')
    assert isinstance(response, str)
    assert 'Hello' in response

def test_web_search():
    results = search('python programming')
    assert isinstance(results, dict)

def test_code_generation():
    code = generate_code('create a function to add numbers')
    assert isinstance(code, str)
    assert 'def' in code

def test_conversation_history():
    assistant = Assistant()
    assistant.process('First query')
    assert len(assistant.conversation_history) == 1