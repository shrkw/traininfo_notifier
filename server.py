import datetime
import http.server
import socket
import socketserver
import time
from multiprocessing import Process
from pathlib import Path

from caster import Caster
from speech_synthesizer import SpeechSynthesizer
from yahoo_train_info_scraper import YahooTrainInfoScraper


def serve(port):
    print("serving at port", port)
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        httpd.serve_forever()


class Server:
    def __init__(self):
        pass

    @classmethod
    def ip_addr(cls) -> str:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def start(self, friendly_name: str, file_path: Path):
        port = 8000
        p = Process(target=serve, args=(port,), daemon=True)
        p.start()

        # send to chromecast (as a promise, audio file is hosted by another http.server process)
        caster = Caster(friendly_name)
        server_host = Server.ip_addr()
        print(f"serve at {server_host}:{port}")
        caster.cast(f"http://{server_host}:{port}/{file_path}")
        time.sleep(20)
