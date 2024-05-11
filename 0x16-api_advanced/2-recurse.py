import requests

def recurse(subreddit, hot_list=[], after=None):
    '''
    Returns a list containing the titles of all hot articles for a given subreddit.
    '''
    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=100'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=100&after={after}'
    
    headers = {'User-Agent': 'Lizzie'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            if 'error' in data:
                return None
            else:
                children = data.get('data', {}).get('children', [])
                if len(children) == 0:
                    return hot_list
                else:
                    for post in children:
                        hot_list.append(post.get('data').get('title'))
                    after = data.get('data').get('after')
                    return recurse(subreddit, hot_list, after)
        except Exception as e:
            print(e)
            return None
    else:
        return None

