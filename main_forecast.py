import datetime
import logging
import os
from pathlib import Path

from caster import Caster
from server import Server
from speech_synthesizer import SpeechSynthesizer
from yahoo_forecast_api import YahooForecastApi
from yahoo_train_info_scraper import YahooTrainInfoScraper

friendly_name = os.getenv("FRIENDLY_NAME")
train_info_url = os.getenv("TRAIN_INFO_URL")
location = os.getenv("LOCATION")
yahoo_app_id = os.getenv("YAHOO_APP_ID")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def main():
    logger.info("Start")
    # fetch info
    api = YahooForecastApi(location, yahoo_app_id)
    status = api.run()
    if status is None:
        return

    # synthesize text
    dest_path = Path("tmp/forecast.mp3")

    if not dest_path.exists():
        synth = SpeechSynthesizer()
        synth.synthesize(status, dest_path)

    server = Server()
    server.start(friendly_name, dest_path)

    logger.info("Finish")


if __name__ == "__main__":
    main()
