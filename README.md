# gleague_autosidebar

Automatically retrieve current roster, standings, and upcoming games and update sidebar widgets on a G-League subreddit.

## Prerequisites
* Python
* BeautifulSoup
* PRAW

## Usage
*main.py*:
1. Must set all Reddit credentials through: https://www.reddit.com/prefs/apps
2. Update all "*insert subreddit*" with target subreddit   

*roster.py* & *upcoming.py*:
1. Update URLs from RealGM

## Notes
The data is retrieved from RealGM and ESPN, so it will be up to date as long as the website is up to date.

