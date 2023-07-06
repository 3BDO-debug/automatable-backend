from google.cloud import speech
from google.cloud import language_v1
import io


def transcribe_audio_file(audio_file_path):
    client = speech.SpeechClient()

    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        language_code="ar-EG",
        enable_automatic_punctuation=True,
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    audio_file.close()

    return transcript


def analyze_sentiment_of_text(text):
    client = language_v1.LanguageServiceClient()

    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    response = client.analyze_sentiment(request={"document": document})

    sentiment = response.document_sentiment

    return sentiment.score, sentiment.magnitude
