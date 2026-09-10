import os
import json
import re
import time
import random
import urllib.request
import urllib.error
API_KEY = os.getenv("GEMINI_API_KEY","")
MODEL = os.getenv("GEMINI_MODEL","gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing")

  prompt = f""" 
  you are professional gmail email writing assistant 
  convert the user's voice command into a professioanl email
  rules:
  - do not copy the command literally
  - do not explain anything
  - do not invert names,dates,prices,companies,attachments,or facts
  - keep the email naturaland coincise
  - include an appropriate greeting and closing

  output exactly:

  SUBJECT: <subject>
  BODY:
  <email body>

  User command:
  {command}
  """
  url = (
    f"https://generativelanguage.googlepis.com/"
    f"v1beta/models/{MODEL}:generativecontent"
  )
  payload = {
    "content": [{"parts": [{"text":prompts}]}],
    "generateConfig": {
      "temperature":0.7,
      "maxOutputTokens":800
    }
  }
  req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode(),
    headers={
      "Content-Type":"application/json",
      "x-goog-api=key": API-KEY
    },
    method="POST"
  )
