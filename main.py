import praw
import os
import time
from upcoming import upcoming
from roster import roster
from standings import standings

client_id = os.environ['client_id']
client_secret = os.environ['client_secret']
username = os.environ['username']
password = os.environ['password']

reddit = praw.Reddit(client_id=client_id,
                   client_secret=client_secret,
                     username = username,
                     password = password,
                     user_agent="<GLeagueBot1.0>")

subreddit = reddit.subreddit('insert subreddit')

while True:
  # Roster and Upcoming Schedule 
  table = roster()
  text = upcoming()
  
  widgets = reddit.subreddit("insert subreddit").widgets
  widgets.progressive_images = True
  
  # Update Schedule 
  widget = reddit.subreddit("insert subreddit").widgets.sidebar[0]
  widget.mod.update(shortName="Schedule", text=text)
  
  # Update Roster
  widget = reddit.subreddit("insert subreddit").widgets.sidebar[1]
  widget.mod.update(shortName="Roster", text=table + "\n(*) = 2-Way")
  
  # Update Roster
  widget = reddit.subreddit("insert subreddit").widgets.sidebar[2]
  widget.mod.update(shortName="Standings", text=standings())
  time.sleep(86400)
  
  