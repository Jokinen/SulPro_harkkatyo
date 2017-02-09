import urllib2, urllib, json

class weather_API:
    def __init__(self):
        self.baseurl = "http://apidev.accuweather.com/"
        self.city_id = "134768" # turku
        self.api_key = "hoArfRosT1215" #"ABDoIV5jKaExyKDYxVcPcOpfodxgAASN"

    def request_data(self, query):
        target_url = self.baseurl + query + "?apiKey=" + self.api_key
        response = urllib2.urlopen(target_url).read()

        return json.loads(response)

    def get_current_conditions(self):
        query = "currentconditions/v1/" + self.city_id + ".json"

        return self.request_data(query)
        # return self.mock_data()

    def mock_data(self):
        # no unnecessary API request while devving
        return json.loads("""[{"LocalObservationDateTime":"2017-02-02T10:05:00+02:00","EpochTime":1486022700,"WeatherText":"Cloudy","WeatherIcon":7,"IsDayTime":true,"Temperature":{"Metric":{"Value":0.0,"Unit":"C","UnitType":17},"Imperial":{"Value":32.0,"Unit":"F","UnitType":18}},"MobileLink":"http://m.accuweather.com/en/fi/turku/134768/current-weather/134768","Link":"http://www.accuweather.com/en/fi/turku/134768/current-weather/134768"}]""")
