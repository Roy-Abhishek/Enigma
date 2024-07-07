import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from get_response import get_response, encode, decode

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

async def send_message(message, user_message):
    if not user_message:
        print("(Message was empty because intents were not enabled properly)")
        return
    
    user_message_words = user_message.split()

    if user_message_words[1] == "encode":
        index_of_message = user_message_words.index("message:")
        index_of_settings = user_message_words.index("settings:")
        main_message = " ".join(user_message_words[index_of_message + 1 : index_of_settings])

        encoded_code = encode(main_message,
                              user_message_words[index_of_settings + 1],
                              user_message_words[index_of_settings + 2], 
                              user_message_words[index_of_settings + 3], 
                              user_message_words[index_of_settings + 4], 
                              user_message_words[index_of_settings + 5],
                              user_message_words[index_of_settings + 6],
                              user_message_words[index_of_settings + 7],
                              user_message_words[index_of_settings + 8])
        
        await message.channel.send(encoded_code)

    elif user_message_words[1] == "decode":
        index_of_message = user_message_words.index("message:")
        index_of_settings = user_message_words.index("settings:")
        main_message = " ".join(user_message_words[index_of_message + 1 : index_of_settings])

        decoded_code = decode(main_message,
                              user_message_words[index_of_settings + 1],
                              user_message_words[index_of_settings + 2], 
                              user_message_words[index_of_settings + 3], 
                              user_message_words[index_of_settings + 4], 
                              user_message_words[index_of_settings + 5],
                              user_message_words[index_of_settings + 6],
                              user_message_words[index_of_settings + 7],
                              user_message_words[index_of_settings + 8])
        
        await message.channel.send(decoded_code)


@client.event
async def on_ready():
    print(f"We have loggen in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f"[{channel}] {username}: \"{user_message}\"")

    try:
        if user_message.split()[0] == "\enigma":
            await send_message(message, user_message)
        elif user_message.split()[0] == "\quit":
            quit()
        else:
            return
    except Exception as e:
        print(e)


def main():
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()


