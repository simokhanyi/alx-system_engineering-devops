#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Custom User-Agent header
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        if children:
            for post in children:
                title = post['data']['title'].lower()
                for word in word_list:
                    word_lower = word.lower()
                    if word_lower in title:
                        counts[word_lower] = (
                            counts.get(word_lower, 0) + title.count(word_lower)
                            )
            return count_words(subreddit, word_list,
                               children[-1]['data']['name'],
                               counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print(None)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)
