from google.cloud import texttospeech
import json


def tts(voice, dialog):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=dialog)

    voice_config = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name=voice["type"],
        ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        pitch=voice["pitch"],
        speaking_rate=voice["speakingRate"]
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice_config,
                 "audio_config": audio_config}
    )

    return response


with open("config.json", "r") as file:
    config = json.loads(file.read())

with open(config["input"], "r", encoding="utf8") as file:
    conversation = file.read()

with open(config["output"], "wb") as file:
    lines = conversation.split(config["delimiters"]["dialog"])

    for line in lines:
        speaker, dialog = line.split(config["delimiters"]["speaker"])
        response = tts(config["voices"][speaker], dialog)
        file.write(response.audio_content)
