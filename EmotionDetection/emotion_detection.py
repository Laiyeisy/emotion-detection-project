import requests

def emotion_detector(text_to_analyze):
    """
    This function sends text to the Watson NLP Emotion Prediction API
    and returns the detected emotions with the dominant emotion.
    """
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    
    emotions = response_json["emotionPredictions"][0]["emotion"]
    
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }


# prueba (puedes dejarla o quitarla según te pidan)
if __name__ == "__main__":
    print(emotion_detector("I am happy"))
