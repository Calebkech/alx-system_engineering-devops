import requests

def top_ten(subreddit):
    '''
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    '''
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    headers = {'User-Agent': 'Lizzie'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'error' in data:
                print(None)
                return
            for post in data.get('data').get('children'):
                print(post.get('data').get('title'))
        except Exception as e:
            print(e)
    else:
        print(None)

