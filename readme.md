# Tweepy Tornado

## Demonstration

The running application can be viewed at: http://mlh.mercenarytech.com

## Prerequisites

1) Python3
2) Pip
3) Virtualenv (optional, see documentation elsewhere)

## Install

In the source code directory, from the command line execute ```pip3 install -r requirements.txt```
    
Primary requirements are:

   - Tornado [http://www.tornadoweb.org]
   - Tweepy [http://www.tweepy.org]
    
## Run

In the source code directory, from the command line execute ```python3 tweepy_tornado.py```

## Use

Using you favorite browser, navigate to:

Example: http://localhost:8888/

or 

Example: http://localhost:8888?term=mlhacks    

## Background

This is an intentionally trivial project. It could have very quickly involved streams, websockets, CORS, OAUTH, a distributed front end and back end, or even a database. It could have been unwieldy and confusing for the target audience. The intention then became:
- Build the most basic functionality needed to scrape data from Twitter.
- Build the most basic functionality needed to present that data in a visual form that didn't involve raw text output.
- Build in a way that involved the fewest number of dependencies.
- Build in a way that involved the smallest amount of technical knowledge.

Even in this simplified form, it involves:

- Python and its supporting tools
- HTTP
- A third-party library that includes OAUTH-based authentication to Twitter and abstracts its REST-based API.
- Bootstrap [https://getbootstrap.com], for CSS-based styling
- HTML
- Source control
- Server administration
- DNS

