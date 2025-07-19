def analyze_sentiment(text):
    text = text.lower()
    if "good" in text or "happy" in text or "love" in text:
        sentiment = "positive"
        score = 0.9
    elif "bad" in text or "hate" in text or "sad" in text:
        sentiment = "negative"
        score = 0.1
    else:
        sentiment = "neutral"
        score = 0.5
    return {"label": sentiment, "score": score}
