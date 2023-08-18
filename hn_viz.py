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
        "score": int(response_dict.get("score", 0)),
        "url": response_dict.get("url"),
        "comments": int(response_dict.get("descendants", 0)),
    }

    submission_dicts.append(submission_dict)

    # Increment the counter
    num_submissions += 1

# %%
submission_dicts = sorted(submission_dicts, key=itemgetter("score"), reverse=True)

story_urls, scores, hover_texts = [], [], []
for submission_dict in submission_dicts:
    author = submission_dict["author"]
    title = submission_dict["title"]
    url = submission_dict["url"]
    story_urls.append(f"<a href='{url}'>{title}</a>")
    scores.append(submission_dict["score"])
    comments = submission_dict["comments"]
    # Build hover texts
    hover_texts.append(f"<b>Author: {author}</b><br />Comments: {comments}")

# Vizualize top stories
title = "Top Stories at Hacker News"
labels ={'x': 'Story Titles', 'y': 'Scores'}
fig = px.bar(x=story_urls, y=scores, title=title, labels=labels)
fig.update_traces(
    marker_color="skyblue",
    hovertemplate=(
        "<b>Title: %{x}</b><br />" "<b>%{customdata}</b><br />" "<b>Score: %{y}</b>"
    ),
    customdata=hover_texts,
)

fig.show()