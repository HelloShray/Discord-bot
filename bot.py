import discord
import responses


# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if response is not None:    #Sends response to user in DM or channel depending on received message 
            await message.author.send(response) if is_private else await message.channel.send(response)  

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA1MDcyNjIzNzU1Mjc4NzQ5Nw.GCYMXg.ONEIa1RVc14GCPn5SBMlPhFSVWIkvdUxsAftUs'  #This token links the discord bot to this code.
    
    intents = discord.Intents.default()
    intents.messages = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop by talking to itself
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message. Response will be sent in a DM.
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?' and reads the command as normal
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)
