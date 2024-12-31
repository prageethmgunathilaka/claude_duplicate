from claude_duplicate import Assistant

def test_basic_response():
    assistant = Assistant()
    response = assistant.process('test')
    assert isinstance(response, str)