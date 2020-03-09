from pathlib import Path

import google.cloud.texttospeech
from google.cloud import texttospeech_v1 as texttospeech


class SpeechSynthesizer:
    def synthesize(self, text: str, dest_path: Path) -> Path:
        dest_path.parent.mkdir(exist_ok=True)
        self.synthesize_text_with_audio_profile(
            text, dest_path, "small-bluetooth-speaker-class-device",
        )
        return dest_path

    # pylint: disable=no-member
    def synthesize_text_with_audio_profile(
        self, text: str, output: Path, effects_profile_id: str
    ):
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(text=text)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code="ja-JP", name="ja-JP-Wavenet-B"
        )
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3,
            effects_profile_id=[effects_profile_id],
        )

        response = client.synthesize_speech(input_text, voice, audio_config)
        with open(output, "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "%s"' % output)
