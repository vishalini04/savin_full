from transformers import pipeline

# Load a pre-trained intent classification model
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict_intent(text):
    result = classifier(text)[0]  # Get the classification result
    intent = result["label"]  # Label is either 'POSITIVE' or 'NEGATIVE' (basic sentiment model)
    
    # Map sentiment labels to intents (customize this)
    if intent == "POSITIVE":
        return "general_query"
    elif intent == "NEGATIVE":
        return "complaint"
    else:
        return "unknown"
