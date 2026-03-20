def emotion_detector(text_to_analyze):
    """
    This function simulates emotion detection from text.
    """

    emotions = {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.1,
        "joy": 0.7,
        "sadness": 0.05
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return (
        f"Anger: {emotions['anger']}, "
        f"Disgust: {emotions['disgust']}, "
        f"Fear: {emotions['fear']}, "
        f"Joy: {emotions['joy']}, "
        f"Sadness: {emotions['sadness']}. "
        f"Dominant emotion: {dominant_emotion}"
    )


print(emotion_detector("I am happy"))