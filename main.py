import datetime
import os
from pathlib import Path

from caster import Caster
from server import Server
from speech_synthesizer import SpeechSynthesizer
from yahoo_train_info_scraper import YahooTrainInfoScraper

friendly_name = os.getenv("FRIENDLY_NAME")
train_info_url = os.getenv("TRAIN_INFO_URL")


def main():
    print("Start")
    # fetch info
    scraper = YahooTrainInfoScraper()
    title, status = scraper.fetch_train_info(train_info_url)
    # synthesize text
    dest_path = Path("tmp").joinpath(
        "on_time.mp3"
        if "平常運転" in status
        else f'{datetime.datetime.now().strftime("%Y-%m-%dT%H%M%S")}.mp3'
    )
    if not dest_path.exists():
        synth = SpeechSynthesizer()
        synth.synthesize(f"{title}の運行情報です。 {status}", dest_path)

    server = Server()
    server.start(friendly_name, dest_path)

    print("Finish")


if __name__ == "__main__":
    main()
