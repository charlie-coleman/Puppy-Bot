import groupy
import time
import commands

max_posts = 5

# define the start times and the group ids for common groups
time_last_updated = time.time()
time_last_sent = time.time()
hold_message = None
future_neighbors = '26789966'
testing_ground = '19123252'
amy_chat = '26981106'

# find the correct group
groups = groupy.Group.list()
main_group = None
for group in groups:
    if group.group_id == amy_chat:
        main_group = group

# choose the correct bot depending on which chat we are in
in_neighbors = False
if main_group.group_id == future_neighbors:
    groupme_bot = groupy.Bot.list()[5]
elif main_group.group_id == amy_chat:
    groupme_bot = groupy.Bot.list()[4]
else:
    groupme_bot = groupy.Bot.list()[1]

# confirm that the bot connected successfully
print('Connection successful')

while commands.run:
    # get the latest message and split it into single words
    message = main_group.messages()[0]
    message_parts = []
    if message.text is not None:
        message_parts = message.text.split()

    # update the reddit posts every 10 minutes
    if time.time()-time_last_updated > 600:
        commands.update()
        time_last_updated = time.time()

    # check if the message is meant to trigger an admin command and that the person sending the message is an admin
    # if both are true, send its function
    if message.user_id in commands.admins and message_parts[0] in commands.admin_commands:
        commands.admin_functions[commands.admin_commands.index(message_parts[0])](message, groupme_bot)

    # check if the message is meant to trigger an open command, if so, send its function
    post_number = 0
    message_sent = False
    for i in range(len(message_parts)):
        part = message_parts[i]
        if part in commands.open_commands and post_number < commands.max_post:
            num = 0
            if i < len(message_parts)-1:
                if message_parts[i+1].isdigit():
                    num = int(message_parts[i+1])
            else:
                num = 1
            num = num if num <= max_posts else max_posts
            for j in range(num):
                commands.open_functions[commands.open_commands.index(part)](message, groupme_bot)
            post_number += 1
        elif part in commands.open_commands and post_number == commands.max_post:
            output = 'Limit ' + str(commands.max_post) + ' post(s) per message.'
            groupme_bot.post(output)
            post_number += 1

    # prevent timeout
    if hold_message != main_group.messages()[0].created_at:
        hold_message = main_group.messages()[0].created_at
        time_last_sent = time.time()

    # reduce cpu usage
    time.sleep(2)