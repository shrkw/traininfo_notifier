import os

from caster import Caster
from speech_synthesizer import SpeechSynthesizer
from yahoo_train_info_scraper import YahooTrainInfoScraper

friendly_name = os.getenv("FRIENDLY_NAME")
server_host = os.getenv("SERVER_HOST")
train_info_url = os.getenv("TRAIN_INFO_URL")


def main():
    # fetch info
    scraper = YahooTrainInfoScraper()
    title, status = scraper.fetch_train_info(train_info_url)
    # synthesize text
    synth = SpeechSynthesizer()
    file_name = synth.synthesize(f"{title}の運行情報です。 {status}")
    # send to chromecast (as a promise, audio file is hosted by another http.server process)
    caster = Caster(friendly_name)
    caster.cast(f"http://{server_host}/{file_name}")


if __name__ == "__main__":
    main()
