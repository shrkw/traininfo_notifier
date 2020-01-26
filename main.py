import http.server
import os
import socket
import socketserver
from multiprocessing import Process

from caster import Caster
from speech_synthesizer import SpeechSynthesizer
from yahoo_train_info_scraper import YahooTrainInfoScraper

friendly_name = os.getenv("FRIENDLY_NAME")
server_host = os.getenv("SERVER_HOST")
train_info_url = os.getenv("TRAIN_INFO_URL")


def serve(port):
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("serving at port", port)
        httpd.serve_forever()


def main():
    # fetch info
    scraper = YahooTrainInfoScraper()
    title, status = scraper.fetch_train_info(train_info_url)
    # synthesize text
    synth = SpeechSynthesizer()
    file_name = synth.synthesize(f"{title}の運行情報です。 {status}")

    p = Process(target=serve, args=(8000,), daemon=True)
    p.start()

    # send to chromecast (as a promise, audio file is hosted by another http.server process)
    caster = Caster(friendly_name)
    caster.cast(f"http://{server_host}/{file_name}")


if __name__ == "__main__":
    main()
