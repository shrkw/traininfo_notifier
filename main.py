import http.server
import os
import socket
import socketserver
from multiprocessing import Process

from caster import Caster
from speech_synthesizer import SpeechSynthesizer
from yahoo_train_info_scraper import YahooTrainInfoScraper

friendly_name = os.getenv("FRIENDLY_NAME")
train_info_url = os.getenv("TRAIN_INFO_URL")


def serve(port):
    print("serving at port", port)
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        httpd.serve_forever()


def ip_addr():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip


def main():
    print("Start")
    # fetch info
    scraper = YahooTrainInfoScraper()
    title, status = scraper.fetch_train_info(train_info_url)
    # synthesize text
    synth = SpeechSynthesizer()
    file_name = synth.synthesize(f"{title}の運行情報です。 {status}")

    port = 8000
    p = Process(target=serve, args=(port,), daemon=True)
    p.start()

    # send to chromecast (as a promise, audio file is hosted by another http.server process)
    caster = Caster(friendly_name)
    server_host = ip_addr()
    print(f"serve at {server_host}:{port}")
    caster.cast(f"http://{server_host}:{port}/{file_name}")
    print("Finish")


if __name__ == "__main__":
    main()
