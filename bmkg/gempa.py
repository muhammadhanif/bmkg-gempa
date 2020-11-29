#
# @author       : Muhammad Hanif
# @email        : moehammadhanif@gmail.com
# @home page    : https://hanifmu.com
# @create date  : 2020-11-29 09:26:19
# @modify date  : 2020-11-29 11:24:56
#

import requests
import json
import xmltodict


class Gempa:
    def m_5_terkini(self):
        """
        Data gempa bumi magnitudo 5.0+ terkini.
        """

        url = "https://data.bmkg.go.id/autogempa.xml"

        return self.__getData(url)

    def tsunami_terkini(self):
        """
        Data tsunami terkini.
        """

        url = "https://data.bmkg.go.id/lasttsunami.xml"

        return self.__getData(url)

    def m_5(self):
        """
        Data gempa bumi magnitudo 5.0+.
        """

        url = "https://data.bmkg.go.id/gempaterkini.xml"

        return self.__getData(url)

    def dirasakan(self):
        """
        Data gempa bumi dirasakan+.
        """

        url = "https://data.bmkg.go.id/gempadirasakan.xml"

        return self.__getData(url)

    def __getData(self, url):
        try:
            response = requests.get(url)
            data = xmltodict.parse(response.content)

            return json.dumps(data)
        except requests.exceptions.HTTPError as errh:
            return repr(errh)
        except requests.exceptions.ConnectionError as errc:
            return repr(errc)
        except requests.exceptions.Timeout as errt:
            return repr(errt)
        except requests.exceptions.RequestException as err:
            return repr(err)
