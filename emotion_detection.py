def emotion_detector(text_to_analyze):
    """
    This function simulates emotion detection from text.
    """

    # Simulated response (como si viniera de Watson)
    emotions = {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.1,
        "joy": 0.7,
        "sadness": 0.05
    }

    # Detectar emoción dominante
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }