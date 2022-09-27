import praw
from random import sample
from time import sleep
ata=open("atatürk.txt","r")
wait=15#Interval of requesting a call
atal=[]#Atatürk picture links
postid=[]
for x in ata:
    atal.append(x)
wordl=["tayyip","erdoğan","teyyip","tahsin","rte","r.t.e","r.t.e.","uzun adam"]#Words that should be in title to bot to reply
reddit = praw.Reddit(
client_id="",
client_secret="",
user_agent="<console:LOL:1.0>",
username="anti-rte-bot",
password="",
ratelimit_seconds=1200,
)

subl=["Turkey","TurkeyJerky","ShitpostTC"]#Subs that bot will reply on
d=0
while True:
    try:
        sub=reddit.subreddit(subl[d])
        print("Searching in:"+subl[d])
        for post in sub.new(limit=10):
            if post.id in postid:
                continue
            for x in wordl:
                k=post.title.lower()
                i=k.find(x)
                if i != -1:
                    t1=k[i-1]
                    u2=len(x)
                    t2=k[i+u2]
                    if t1 == " " or ":" or "'" :
                        if t2 == " " or ":" or "'" :
                            postid.append(post.id)
                            pic=sample(atal, 1)[0]
                            rep_temp="Başlıkta RTE ile ilgili şeyler geçtiği için gerçek bir liderin [fotoğrafını]({}) paylaşmaya geldim"+"\n\n"+"\n\n"+"^(I am a bot and this action was performed automatically.)"+"\n\n"+"[Kaynak Kodu|Source Code](https://github.com/andmydignity/anti-tayyip-bot)"
                            rep=rep_temp.format(pic)
                            post.reply(rep)
                            print("Replied to a post.({}|{})".format(subl[d],post.title))
                            break

        if d==len(subl)-1:
                d=0
        else:
            d+=1
        if len(postid)>30:
            for l in range(4):
                postid.pop(x)
        #Switch to an another sub
        sleep(wait)
    except:
        continue
        sleep(wait)
