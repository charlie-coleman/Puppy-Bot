import random
import warnings
import time
import math

# praw causes some weird warnings that don't matter if you don't do this. Clears up the console
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    import praw

# Change to false to stop the bot. Used in !disconnect
run = True

# Set the number of times one message can post
max_post = 3

# The text to trigger a command
open_commands = ['!puppy', '!hotguys', '!bellathorne', '!food', '!cheese', '!help', '!uptime']
admin_commands = ['!disconnect', '!setmax']

# The purpose of each command, used in !help. Must be the same length as the corresponding command array
open_purpose = ['pups', 'people say their hot, idk', 'bella thorne', 'and food', 'cheese', 'this', 'how long the bot has been running']
admin_purpose = ['disconnect the bot', 'sets the max number of posts per message']

# List of admin account ids
admins = ['7246623']

# Setup the arrays of reddit posts to pull from
consequences = False
r = praw.Reddit(client_id='K_Vq8AygtCs4VQ', client_secret='r5OCC3nCwP-n1dMP75LLucoW6JQ', user_agent='Luscious-Bot')

start_time = time.time()
puppy_posts = []
davefranco_posts = []
bellathorne_posts = []
food_posts = []
cheese_posts = []
puppy_subs = ['puppies']
davefranco_subs = ['ladyboners']
bellathorne_subs = ['bellathorne']
food_subs = ['food']
cheese_subs = ['cheese']
puppy_subs_amount = [200]
davefranco_subs_amount = [200]
bellathorne_subs_amount = [200]
food_subs_amount = [200]
cheese_subs_amount = [200]

# ~~~~~~~~OPEN COMMANDS~~~~~~~~


# update pool of images
def update():
    global puppy_posts
    global davefranco_posts
    global bellathorne_posts
    global food_posts
    global cheese_posts
    puppy_posts = []
    davefranco_posts = []
    bellathorne_posts = []
    food_posts = []
    cheese_posts = []
    for i in range(len(puppy_subs)):
        if puppy_subs[i]:
            for post in r.subreddit(puppy_subs[i]).hot(limit=puppy_subs_amount[i]):
                if 'imgur' in post.url:
                    puppy_posts.append(post)
    for i in range(len(davefranco_subs)):
        if davefranco_subs[i]:
            for post in r.subreddit(davefranco_subs[i]).hot(limit=davefranco_subs_amount[i]):
                if 'imgur' in post.url:
                    davefranco_posts.append(post)
    for i in range(len(bellathorne_subs)):
        if bellathorne_subs[i]:
            for post in r.subreddit(bellathorne_subs[i]).hot(limit=bellathorne_subs_amount[i]):
                if 'imgur' in post.url:
                    bellathorne_posts.append(post)
    for i in range(len(food_subs)):
        if food_subs[i]:
            for post in r.subreddit(food_subs[i]).hot(limit=food_subs_amount[i]):
                if 'imgur' in post.url:
                    food_posts.append(post)
    for i in range(len(cheese_subs)):
        if cheese_subs[i]:
            for post in r.subreddit(cheese_subs[i]).hot(limit=cheese_subs_amount[i]):
                if 'imgur' in post.url:
                    cheese_posts.append(post)


# generate and post the output for !boobs
def puppy_output(*args):
    global puppy_posts
    if len(puppy_posts) < 1:
        update()
    output_string = random.choice(puppy_posts).url
    try:
        args[1].post(output_string)
    except AttributeError:
        print('Second argument must be the bot')


# generates and posts the output for !ass
def davefranco_output(*args):
    global davefranco_posts
    if len(davefranco_posts) < 1:
        update()
    output_string = random.choice(davefranco_posts).url
    try:
        args[1].post(output_string)
    except AttributeError:
        print('Second argument must be the bot')


def bellathorne_output(*args):
    global bellathorne_posts
    if len(bellathorne_posts) < 1:
        update()
    output_string = random.choice(bellathorne_posts).url
    try:
        args[1].post(output_string)
    except AttributeError:
        print('Second argument must be the bot')


def food_output(*args):
    global food_posts
    if len(food_posts) < 1:
        update()
    output_string = random.choice(food_posts).url
    try:
        args[1].post(output_string)
    except AttributeError:
        print('Second argument must be the bot')


def cheese_output(*args):
    global cheese_posts
    if len(cheese_posts) < 1:
        update()
    output_string = random.choice(cheese_posts).url
    try:
        args[1].post(output_string)
    except AttributeError:
        print('Second argument must be the bot')


# generates and posts the output for !help
def help_output(*args):
    output_string = 'Open Commands:\n'
    for i in open_commands:
        output_string += i + ': ' + open_purpose[open_commands.index(i)] + '\n'
    output_string += '\nAdmin Commands:\n'
    for i in admin_commands:
        output_string += i + ': ' + admin_purpose[admin_commands.index(i)] + '\n'
    try:
        args[1].post(output_string)
    except AttributeError:
        print('Second argument must be the bot')


# return time running
def uptime(*args):
    global start_time
    seconds = int(time.time() - start_time)
    hours = math.floor(seconds/3600)
    minutes = math.floor((seconds-hours*3600)/60)
    seconds = seconds - hours*3600 - minutes*60
    time_string = str(hours) + ' hours ' + str(minutes) + ' minutes and ' + str(seconds) + ' seconds'
    output_string = 'The last time the bot was reset was ' + time_string + ' ago.'
    try:
        args[1].post(output_string)
    except AttributeError:
        print('Second argument must be the bot')


# ~~~~~~~~ADMIN COMMANDS~~~~~~~~

# disconnect the bot
def disconnect(*args):
    try:
        output_string = args[1].name + ' is never truly gone.'
        args[1].post(output_string)
    except AttributeError:
        print('Second argument must be the bot')
    print('Disconnected by an admin')
    global run
    run = False


def set_max(*args):
    message_parts = args[0].text.split()
    global max_post
    try:
        if len(message_parts) > 0:
            max_post = int(message_parts[1])
        else:
            max_post = 3
        output_string = 'Max post number set to ' + str(max_post)
    except TypeError:
        output_string = 'Improper argument for max post number'
    try:
        args[1].post(output_string)
    except AttributeError:
        print('Second argument must be the bot')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Get the reddit posts
update()

# Assigns a function to a command. Must be the same length as the corresponding '_commands' array
open_functions = [puppy_output, davefranco_output, bellathorne_output, food_output, cheese_output, help_output, uptime]
admin_functions = [disconnect, set_max]