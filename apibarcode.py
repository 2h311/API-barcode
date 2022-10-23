import base64
from io import BytesIO
from typing import Dict

import requests
from PIL import Image
from fake_useragent import UserAgent


class GenerateBarcode:
    """generate gs1_128 barcode from an external API"""

    ua = UserAgent(
        fallback="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    )
    url = "https://api.products.aspose.app/barcode/generate/generatebarcode?culture=en"

    @staticmethod
    def get_payload(code: str) -> Dict:
        return {
            "barcodetype": "Code128",
            "content": code,
            "filetype": "PNG",
            "filesize": 3,
        }

    def get_header(self) -> Dict:
        return {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-length": "86",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://products.aspose.app",
            "referer": "https://products.aspose.app/",
            "user-agent": self.ua.random,
        }

    def get_barcode(self, code: str = "(420)14150(94)05511298370625316403") -> None:
        res = requests.post(
            self.url, headers=self.get_header(), data=self.get_payload(code)
        )
        if res.ok:
            print("Request Successful")
            imgbase = base64.urlsafe_b64decode(res.json()["imgBase64"])
            im = Image.open(BytesIO(imgbase))
            im.show()
        else:
            print(res.status)


if __name__ == "__main__":
    GenerateBarcode().get_barcode()
