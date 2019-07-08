import praw
import shutil
import os
import change_background
from urllib.request import urlretrieve


def create_reddit_instance():
    reddit = praw.Reddit('image_pull', user_agent='ubuntu:subreddit_pull bot1')
    return reddit


def pull_from_subreddit(reddit, subreddit, num_of_posts):
    try:
        for submission in reddit.subreddit(subreddit).hot(limit=num_of_posts):
            # Checks for valid image file type
            if submission.url.endswith('jpg'):
                urlretrieve(submission.url, 'images/'+submission.title+'.jpg')
            elif submission.url.endswith('png'):
                urlretrieve(submission.url, 'images/'+submission.title+'.png')
            else:
                continue
    except Exception as e:
        print("Not able to obtain posts")
        print(e)


def main():
    # Remove all old images and recreate the folder for new ones
    if os.path.isdir('images'):
        shutil.rmtree('images')
    os.mkdir('images')

    reddit = create_reddit_instance()
    subreddit = 'earthporn'
    num_of_posts = 15

    pull_from_subreddit(reddit, subreddit, num_of_posts)
    change_background.main()


if __name__ == '__main__':
    main()
