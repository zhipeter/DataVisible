'''Hacker New API'''
import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) +
           '.json')
    submission_r = requests.get(url)
    print("Submissions Status code:", submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Disussion link:', submission_dict['link'])
    print('Comments:', submission_dict['comments'])
