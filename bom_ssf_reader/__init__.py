import requests
import bom_data_parser as bdp

try:
    from urlib2 import urlopen
except:
    from urllib.request import urlopen

class SSFReader(object):

    def __init__(self, server_url = 'http://www.bom.gov.au/water/ssf'):
        self.server_url = server_url
        config_url = '{0}/images/site_config.json'.format(self.server_url)
        self.metadata = requests.get(config_url).json()

        self.station_list = []
        self.station_meta = {}
        for station in self.metadata['stations']['features']:
            station_id = station['properties']['ID']

            self.station_list.append(station_id)

            self.station_meta[station_id] = {
                'drainage': station['properties']['drainage'],
                'basin': station['properties']['basin'],
                'properties': station,
            }

    def get_site_info(self, awrc):
        return self.station_meta[awrc]['properties']

    def get_forecast(self, awrc, forecast_date):
        forecast_url = '{site}/{drainage}/{basin}/fc/{year}/{month:02d}/{awrc}_FC_10_{year}_{month:02d}_table.csv'.format(**{
            'site': self.server_url,
            'drainage': self.station_meta[awrc]['drainage'],
            'basin': self.station_meta[awrc]['basin'],
            'year': forecast_date.year,
            'month': forecast_date.month,
            'awrc': awrc
        })

        return bdp.read_ssf_csv(urlopen(forecast_url))
