#!/usr/bin/env python
import praw
import pickle
import re
import time
from config import *
from credentials import *

subreddits = submissions = done = None

def extractWords(s):
    cleanedString = re.sub(r'[^a-zA-Z ]', '', s).lower()
    titleAsList = cleanedString.split(' ')
    return titleAsList

def Word(Title, inGroup):
    titleAsList = extractWords(Title)
    inGroup = list(inGroup)

    names = []
    for i in titleAsList:
        if i.lower() in inGroup:
            names.append(i)
        if len(names) == 2:
            if names[0] != names[1]:
                return True

def main():

    submissions =  list(subreddits.get_new(limit=50))

    for submission in submissions:

        try:

            if submission.id not in done:

                done.append(submission.id)
                with open('done', 'w') as f:
                    pickle.dump(done, f)

                if not submission.is_self:

                    for i,j in enumerate(celebs):
                        if Word(submission.title, j.keys()[0]):
                            submission.add_comment(j.values()[0])

        except Exception as e:

            log = "Sub Error: "+str(e)+" on "+submission.title+" "+submission.id+" @ "+str(time.time())+"\n"
            with open("errorlog.txt", "a") as f:
                f.writelines(log)


if __name__ == "__main__":

    r = praw.Reddit(user_agent=REDDIT_USERAGENT)
    r.login(REDDIT_USERNAME, REDDIT_PASSWORD)


    try:

        with open("done", "r") as f:
            done = pickle.load(f)

        subreddits = r.get_subreddit(subreddits_string)
        submissions =  list(subreddits.get_new(limit=50))

    except:

        subreddits = r.get_subreddit(subreddits_string)
        submissions =  list(subreddits.get_new(limit=50))

        done = []
        for submission in submissions:
            done.append(submission.id)

        with open('done', 'w') as f:
            pickle.dump(done, f)


    while True:

        try:

            main()

        except Exception as e:

            log = "General Error: "+str(e)+" @ "+str(time.time())+"\n"
            with open('errorlog.txt', 'a') as f:
                f.writelines(log)

        print "Sleeping for 5 minutes."
        time.sleep(300)
