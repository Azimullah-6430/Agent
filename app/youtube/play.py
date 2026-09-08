import re
import urllib.
import urllib.request

def get_vid(query):
  try:
    encoded = urllib.parse.quote(query)
    url = (
          "https://www.youtube.com/results"
          "?search_query =" + encoded
    )

  request = urllib.request.urlopen(
      url,
      headers = {
            "User-Agent
          
