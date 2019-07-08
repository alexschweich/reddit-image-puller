# `Reddit Image Puller`

#### Reddit image puller is a small script to pull a set of images from a selected subreddit, and change your desktop background to randomly select one of those images.

The subreddit, number of results, and sorting method can be changed easily

    For subreddit: change the 'subreddit' variable in __main__
    For number of results: change the 'num_of_posts' variable in __main__
    For sorting method: change hot in 'pull_from_subreddit'

Setting a CRON/Windows scheduler will do the following for each file:
    
    image_pull.py will refresh the images/ directory with the latest hot posts.
    change_background.py will randomly change the background to a file from the images directory. 

By default the program deletes existing images and downloads new ones when image_pull.py is run. To disable this, comment/delete the rmtree and mkdir lines in the main method.

Ensure to configure a praw.ini file and put it in the directory before running the script, instructions here:
https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html#praw-ini

change_background.py has not yet been tested on Windows and may not function properly.