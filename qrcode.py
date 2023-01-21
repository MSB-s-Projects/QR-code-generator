import pyqrcode
import png
from pyqrcode import QRCode

toBeencoded = "String to be encoded"

url = pyqrcode.create(toBeencoded)

url.svg("myqr.svg", scale=8)

url.png('myqr.png', scale=6)
