import praw
from random import sample
from time import sleep
import json

from dotenv import dotenv_values

env_config = dotenv_values(".env")

bot_config = None
with open('bot-config.json') as f:
    bot_config = json.load(f)

title_words = bot_config["active_subs"]
active_subs = bot_config["title_words"]

reddit = praw.Reddit(
    client_id=env_config["CLIENT_ID"],
    client_secret=env_config["CLIENT_SECRET"],
    user_agent=env_config["USER_AGENT"],
    username=env_config["USERNAME"],
    password=env_config["PASSWORD"],
    ratelimit_seconds=1200,
)


def comment_generator():
    post_text = "Başlıkta RTE ile ilgili şeyler geçtiği için gerçek bir liderin [fotoğrafını]({}) paylaşmaya geldim" + \
        "\n\n"+"\n\n" + \
        "^(I am a bot and this action was performed automatically.)"+"\n\n" + \
        "[Kaynak Kodu|Source Code](https://github.com/andmydignity/anti-tayyip-bot)"
    return post_text.format(sample(bot_config["pics"], 1)[0])


post_ids = []
sub_iterator = 0
while True:  # this loop is for switching between subs
    try:
        sub = reddit.subreddit(active_subs[sub_iterator])
        print("Searching in:" + active_subs[sub_iterator])
        for post in sub.new(limit=10):
            if post.id in post_ids:
                continue
            for word in title_words:

                lowercase_title = post.title.lower()  # split the title into words
                title_words = lowercase_title.split()

                # if there is an overlap between title_words and word
                if set(title_words).intersection(word):
                    print("Found match in post: " + post.title)
                    post.reply(comment_generator())
                    post_ids.append(post.id)
                    print("Replied to post: " + post.title)
                    break

        if sub_iterator == len(active_subs) - 1:
            sub_iterator = 0  # reset the sub iterator
        else:
            sub_iterator += 1

        if len(post_ids) > 30:
            del post_ids[0:4]
    except:
        continue
