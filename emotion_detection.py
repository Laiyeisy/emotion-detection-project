import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    return response.json()
    

# Prueba
print(emotion_detector("I am happy"))
