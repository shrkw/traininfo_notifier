import pychromecast


class Caster:
    def __init__(self, friendly_name):
        chromecasts = pychromecast.get_chromecasts()
        self.living = next(
            cc for cc in chromecasts if cc.device.friendly_name == friendly_name
        )

    def cast(self, mp3_url: str):
        self.living.wait()
        mc = self.living.media_controller
        mc.play_media(mp3_url, "audio/mp3")
        mc.block_until_active()
