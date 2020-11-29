#
# @author       : Muhammad Hanif
# @email        : moehammadhanif@gmail.com
# @home page    : https://hanifmu.com
# @create date  : 2020-11-29 09:26:19
# @modify date  : 2020-11-29 09:26:19
#

import requests
import json
import xmltodict


class Gempa:
    def m_5_terkini(self):
        """
        Data gempa bumi magnitudo 5.0+ terkini.
        """
        data = requests.get("https://data.bmkg.go.id/autogempa.xml")
        xml = xmltodict.parse(data.content)

        return json.dumps(xml)

    def tsunami_terkini(self):
        """
        Data tsunami terkini.
        """
        data = requests.get("https://data.bmkg.go.id/lasttsunami.xml")
        xml = xmltodict.parse(data.content)

        return json.dumps(xml)

    def m_5(self):
        """
        Data gempa bumi magnitudo 5.0+.
        """
        data = requests.get("https://data.bmkg.go.id/gempaterkini.xml")
        xml = xmltodict.parse(data.content)

        return json.dumps(xml)

    def dirasakan(self):
        """
        Data gempa bumi dirasakan+.
        """
        data = requests.get("https://data.bmkg.go.id/gempaterkini.xml")
        xml = xmltodict.parse(data.content)

        return json.dumps(xml)
