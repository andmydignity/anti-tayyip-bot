import praw
from random import sample
from datetime import datetime
from time import sleep
ata=open("atatürk.txt","r")
rte=open("rte.txt","r")
wait=15#Interval of requesting a call
atal=[]#Atatürk picture links
rtel=[]#RTE qoutes
titlel=[]
for x in ata:
    atal.append(x)
for x in rte:
    rtel.append(x)
wordl=["tayyip","erdoğan","teyyip","tahsin","rte","r.t.e","r.t.e.","uzun adam"]#Words that should be in title to bot to reply
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username="",
    password="",
)

subl=["Turkey","TurkeyJerkey","ShitpostTC"]#Subs that bot will reply on
d=0
d1=0
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
                break
                #If D1 comes true,post includes one of the holy words.
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
                qou=sample(rtel, 1)[0]
                print(pic)
                rep_temp="Başlıkta RTE ile ilgili şeyler geçtiği için bir Atatürk [fotoğrafı]({}) paylaşmaya geldim"+"\n\n"+"^(------------------------------------------------------------------------------------------------------------------------------------------------------------------)"+"\n\n"+"[Kaynak Kodu|Source Code](https://github.com/andmydignity/anti-tayyip-bot)"+"\n\n"+"^('{}' -R.T.E)"
                rep=rep_temp.format(pic,qou)
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


