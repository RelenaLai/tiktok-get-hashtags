from TikTokApi import TikTokApi
import pandas as pd

verifyFP = ''
api = TikTokApi.get_instance(custom_verify=verifyFP, use_test_endpoints=True)

def csv_dict(tiktok_dict):
  csv = {}
  csv['user_name'] = tiktok_dict['author']['uniqueId']
  csv['user_id'] = tiktok_dict['author']['id']
  csv['video_id'] = tiktok_dict['id']
  csv['video_desc'] = tiktok_dict['desc']
  csv['video_length'] = tiktok_dict['video']['duration']
  csv['video_link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(csv['user_name'], csv['video_id'])
  csv['likes'] = tiktok_dict['stats']['diggCount']
  csv['plays'] = tiktok_dict['stats']['playCount']
  return csv

count = 2000
username = 'tiktok'

likedVideos = api.userLikedbyUsername(username, count=count)
likedVideos = [csv_dict(video) for video in likedVideos]

likedVideosDF = pd.DataFrame(likedVideos)
likedVideosDF.to_csv('{}_liked_videos.csv'.format(username), index=False)
