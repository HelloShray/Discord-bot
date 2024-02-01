Welcome to my Discord Chatbot project. This project was created for my college.

A chatbot that responds to user's messages, providing conversations, and fulfills basic commands. The bot is linked to a discord bot account using Discord API.
Discord is an instant messaging and VoIP social platform which allows communication through voice calls, video calls, text messaging, and media and files. Communication can be private or take place in virtual communities called "servers".
This bot can respond to users within the channels in a server as well as private DMs.

Files:
1. main.py is responsible for starting up the bot itself.
2. responses.py handles the responses part. It parses the user's message and checks through the response json file to see if the user's message matches any of the possible conversations. It selects a response on the basis of this.
3. bot.py handles the bot functionality regarding connecting to discord, sending the messages to the correct channel with the correct user tagged, providing debugging information in the console, etc.
4. random_responses.py is used when the bot is talked to but it doesn't understand the user's messages (this is due to the bot.json file not containing a possible conversation candidate or the user typing an incorrect command)
5. bot.json contains various inputs and their responses that the bot is meant to give.


Further scope of expanding the bot exists, such as making it live permanently, adding more responses, making it AI-powered to further boost its conversational capabilities.
