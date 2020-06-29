from pathlib import Path

from google.cloud import texttospeech


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
        synthesis_input = texttospeech.types.SynthesisInput(text=text)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code="ja-JP", name="ja-JP-Wavenet-B"
        )
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3,
            effects_profile_id=[effects_profile_id],
        )

        response = client.synthesize_speech(synthesis_input, voice, audio_config)
        with open(output, "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "%s"' % output)


if __name__ == "__main__":
    synth = SpeechSynthesizer()
    synth.synthesize("おはようございます", Path("tmp").joinpath("foo.mp3"))
