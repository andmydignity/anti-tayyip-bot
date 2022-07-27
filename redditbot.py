import praw
from random import sample
from datetime import datetime
from time import sleep
ata=open("atatürk.txt","r")
wait=15#Interval of requesting a call
atal=[]
titlel=[]
for x in ata:
    atal.append(x)
wordl=["tayyip","erdoğan","teyyip","rte","r.t.e","r.t.e.","uzun adam"]
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username="",
    password="",
)

subl=["Turkey","TurkeyJerkey","ShitpostTC"]
d=0
d1=0
chosen=str()
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time=="02:00:00":
        titlel=[]
        #Flush the title list at 4 AM İstanbul Time
    sub=reddit.subreddit(subl[d])
    print(subl[d])
    for post in sub.new(limit=25):
        for x in wordl:
            print(post.title.lower())
            if x in post.title.lower():
                d1=True
                x=chosen
                break
                #If D1 comes true,post includes one of the holy words.
                #Also 'chosen' is the one of the holy words
            else:
                d1=False
                continue
        if d1:
            if post.title in titlel:
                pass
                #Do not reply to same post.(Might do it twice after the flush at 4 AM)
            else:
                titlel.append(post.title)
                pic=sample(atal, 1)[0]
                print(pic)
                rep_temp="Başlıkta RTE ile ilgili şeyler geçtiği için bir Atatürk [fotoğrafı]({}) paylaşmaya geldim                                                                     [Source Code](https://github.com/andmydignity/anti-tayyip-bot)"
                rep=rep_temp.format(pic)
                post.reply(rep)
                print("Replied to a post.("+subl[d]+")")

        else:
            pass
    if d==len(subl)-1:
            d=0
    else:
        d+=1
    #Switch to an another sub
    sleep(wait)

