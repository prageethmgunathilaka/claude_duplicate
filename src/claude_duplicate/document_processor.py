class DocumentProcessor:
    def process(self, text):
        '''Process document text'''
        return {'tokens': len(text.split())}