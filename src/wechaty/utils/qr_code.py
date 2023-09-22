# -*- coding: utf-8 -*-
"""
qr_code helper utils
"""
from typing import Any
import qrcode


def qr_terminal(data: str, version: Any = None) -> None:
    """print the qrcode to the terminal using the python-qrcode tools

    https://github.com/lincolnloop/python-qrcode

    Args:
        data (str): the data of the qrcode
        version (Any, optional): the qrcode version. Defaults to None.
    """
    qr = qrcode.QRCode(version=2, border=2)
    qr.add_data(data)
    if version:
        img = qr.make()
    else:
        img = qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    with open('/opt/qrcode.jpg', 'wb') as f:
        img.save(f)
    qr.print_ascii(invert=True)
