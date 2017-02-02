import urllib2, urllib, json

class news_API:
    def __init__(self):
        self.baseurl = "https://newsapi.org/v1/"
        self.api_key = "a8a3996ef8b84bc6b6373522f599a39c"

    def request_data(self, query):
        target_url = self.baseurl + query + "&apiKey=" + self.api_key
        response = urllib2.urlopen(target_url).read()

        return json.loads(response)

    def get_the_next_web_articles(self):
        query = "articles?source=the-next-web&sortBy=latest"

        return self.request_data(query)
