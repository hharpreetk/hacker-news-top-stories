# %%
import requests
import json

import plotly.express as px
from operator import itemgetter
# %%
# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
# print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()

submission_dicts = []

# Set a counter for the number of submissions
num_submissions = 0

for submission_id in submission_ids:
    # Check if the desired number of submissions has been reached
    if num_submissions >= 30:
        break
    # Make API call for each submssion
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    # print(f"status: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        "author": response_dict.get("by"),
        "title": response_dict.get("title"),
        "url": response_dict.get("url"),
        "comments": response_dict.get("descendants")
    }

    submission_dicts.append(submission_dict)

    # Increment the counter
    num_submissions += 1
# %%
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)

authors, titles, links, comments = [], [], [], []
for submission_dict in submission_dicts:
  authors.append(submission_dict['author'])
  titles. append(submission_dict['title'])
  links.append(submission_dict['url'])
  comments.append(submission_dict['comments'])