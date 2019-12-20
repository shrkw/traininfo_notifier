import datetime

import google.cloud.texttospeech
from google.cloud import texttospeech_v1 as texttospeech


class SpeechSynthesizer:
    def synthesize(self, text):
        d = datetime.datetime.now()

        self.synthesize_text_with_audio_profile(
            text,
            f'${d.strftime("%Y-%m-%dT%H%M%S")}.mp3',
            "small-bluetooth-speaker-class-device",
        )

    # pylint: disable=no-member
    def synthesize_text_with_audio_profile(self, text, output, effects_profile_id):
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(text=text)
        voice = texttospeech.types.VoiceSelectionParams(language_code="ja-JP")
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3,
            effects_profile_id=[effects_profile_id],
        )

        response = client.synthesize_speech(input_text, voice, audio_config)
        with open(output, "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "%s"' % output)
