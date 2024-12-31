class Assistant:
    def __init__(self, model_name='gpt-3.5-turbo'):
        self.model_name = model_name
        self.conversation_history = []

    def process(self, query):
        """Process user query and return response"""
        # Add processing logic here
        return 'Response to: ' + query