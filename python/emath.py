#!/usr/bin/env python3
"""
Replace String in Filename
"""
import sys
import urllib.parse


def main(argv):
    length = len(argv)
    if length < 1:
        print("usage: emath [math equation]")
        sys.exit()
    parsed = urllib.parse.quote_plus(argv[0])
    res = "![equation](http://www.sciweavers.org/tex2img.php?eq="
    res += "{}&bc=White&fc=Black&im=png&fs=12&ff=fourier&edit=)".format(parsed)
    print(res)


if __name__ == "__main__":
    main(sys.argv[1:])
