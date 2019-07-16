import praw
import shutil
import os
import logging
import change_background
from urllib.request import urlretrieve


def create_reddit_instance():
    reddit = praw.Reddit('image_pull', user_agent='ubuntu:subreddit_pull bot1')
    return reddit


def pull_from_subreddit(reddit, subreddit, num_of_posts):
        for submission in reddit.subreddit(subreddit).hot(limit=num_of_posts):
            # Checks for valid image file type
            try:
                if submission.url.endswith('jpg'):
                    urlretrieve(submission.url, 'images/'+submission.title+'.jpg')
                elif submission.url.endswith('png'):
                    urlretrieve(submission.url, 'images/'+submission.title+'.png')
                else:
                    continue
            except:
                logging.critical('Not able to obtain posts')
                continue
        logging.info('Downloaded ' + str(num_of_posts) + ' images from ' + subreddit + 'into /images')


def main():
    logging.basicConfig(filename='image_puller.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    # Remove all old images and recreate the folder for new ones
    if os.path.isdir('images'):
        shutil.rmtree('images')
    os.mkdir('images')
    logging.info('Created images directory')

    reddit = create_reddit_instance()
    subreddit = 'earthporn'
    num_of_posts = 15

    pull_from_subreddit(reddit, subreddit, num_of_posts)
    change_background.main()


if __name__ == '__main__':
    main()
