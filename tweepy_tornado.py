__author__ = 'jeffstrickler - jeff@mercenarytech.com'
__copyright__ = "Copyright (C) 2018 Mercenary Technologies LLC"


import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from tornado.options import define, options
import tweepy

# Authentication params
CONSUMER_KEY = '2IppHcvm74T7xikyZDsuYoU29'
CONSUMER_SECRET = 'tzzotNFn00uQBH7y1AoViYYM4fZy71N5ekePaBY70i15CrtaQI'
ACCESS_TOKEN = '15638014-WQBUVpeeiDUjHqQWwPhzpXG98LMB8okxiNKnoqrRy'
ACCESS_TOKEN_SECRET = 'GKzBHy5tS6shYc8TvxTWXjdubQEsijpu12PmMkAPFUjDS'

DEFAULT_SEARCH_TERM = '#MLHLocalhost'

define("port", default=8888, help="run on the given port", type=int)


class FetchTweetsHandler(tornado.web.RequestHandler):

    def get(self):

        # Connect to the Twitter API using Tweepy
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        # Check for received query string parameters
        term_parameters = self.get_arguments("term")

        # If we receive query string parameters, use them as our search terms for Twitter.
        # Otherwise use our default term
        if term_parameters:
            terms = term_parameters
        else:
            terms = [DEFAULT_SEARCH_TERM]
        results = api.search(q=[terms])

        tweets = []

        for r in results:
            # This is so that we have convenient access to the data in the html template
            current = r.parse(api, r._json)
            tweets.append(current)

        self.render("tweets.html", tweets=tweets)

    def post(self):
        # HTTP POST NOT IMPLEMENTED
        self.set_status(501)
        self.finish()

    def put(self):
        # HTTP PUT NOT IMPLEMENTED
        self.set_status(501)
        self.finish()

    def delete(self):
        # HTTP DELETE NOT IMPLEMENTED
        self.set_status(501)
        self.finish()


class Application(tornado.web.Application):

    def __init__(self):
        settings = {
            'template_path': 'templates',
            'static_path': 'static'
        }

        handlers = [
            (r'/', FetchTweetsHandler)
        ]
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    io_loop = tornado.ioloop.IOLoop.instance()
    application = Application()

    application.listen(options.port)
    io_loop.start()


if __name__ == "__main__":
    main()