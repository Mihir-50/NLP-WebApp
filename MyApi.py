import paralleldots

class API:
    def __init__(self):
        # Setting your API key
        paralleldots.set_api_key('7MCNTJGpAOg6MgIN3EiPvhHSgedpANmYG14sLEZqOgQ')

    def ner(self,text):
        response  = paralleldots.ner(text)
        return response

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response

    def emotion_prediction(self, text):
        response = paralleldots.emotion(text)
        return response

    def abuse_detection(self, text):
        response = paralleldots.abuse(text)
        return response