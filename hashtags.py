import csv
import re
import itertools  

username = 'tiktok'

# generate dict of hashtags (key) and their number of occurences (value) from a user's log
def getHashtags(username):
    hashtagDict = {}
    with open('{}_liked_videos.csv'.format(username)) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',',)
        for row in csvReader:
            hashtags = re.findall('\B#\w\w+', row[3])
            for h in hashtags:
                if h in hashtagDict and notGeneric(h):
                    hashtagDict[h] += 1
                else:
                    hashtagDict[h] = 1
    return hashtagDict

# returns true if the hashtag is not considered "generic"
def notGeneric(hashtag):
    genericTags = ['#fyp', '#foryoupage', '#foryou', '#fypシ', '#fy', '#foryourpage', '#tiktok', '#trending', '#stitch', '#greenscreen', '#duet', '#xyzbca', '#viral', '#Asosfashunweek', '#Videosnapchallenge']
    return hashtag not in genericTags

# returns new dict containing top one hundred occuring hashtags
def getTopHundred(hashtagDict):
    sortedDict = dict(sorted(hashtagDict.items(), key=lambda item: item[1], reverse=True))
    return dict(itertools.islice(sortedDict.items(), 100)) 

topHashtags = getTopHundred(getHashtags(username))

for hashtag, count in topHashtags.items():
    print(hashtag, ' , ', count)


        






