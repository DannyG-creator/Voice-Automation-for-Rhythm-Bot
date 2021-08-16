# INFO

import os
from discord.ext import commands
from dotenv import load_dotenv
import speech_recognition as sr
r = sr.Recognizer()

load_dotenv()
token = os.getenv('DISCORD_TOKEN') # put your bots discord token in the .env file

VOICE_CHAT = os.getenv('VOICE_CHAT') # put the voice chat ID in the .env file

CHANNEL = os.getenv('CHANNEL') # put the text channel ID in the .env file

VOICE_COMMANDS = ["hey rhythm"]
#RHYTHM_ONE = ["hey rhythm"]
#RHYTHM_TWO = ["hey rhythm 2", "hey rhythm two", "hey 2", "hey two"]
#MEE_SIX = ["hey me", "hey me 6", "hey me six"]

bot = commands.Bot(command_prefix="<", description="RHTHM_AUTOMATION", self_bot=True)

#listens for command
def listener():
    with sr.Microphone() as source:
        print("Say: 'hey rhythm'")
        global audio
        audio = r.listen(source)
        prompt()

#discord connection
@bot.event
async def on_ready():
    voice_channel = bot.get_channel(VOICE_CHAT)
    message_channel = bot.get_channel(CHANNEL)

    if r.recognize_google(play_audio) == "what's playing":
        await voice_channel.connect()
        await message_channel.send("+np")
        await bot.close()

    if r.recognize_google(play_audio) == "skip":
        await voice_channel.connect()
        await message_channel.send("+skip")

    if r.recognize_google(play_audio) == "loop":
        await voice_channel.connect()
        await message_channel.send("+loop")
     
    if r.recognize_google(play_audio) == "lyrics":
        await voice_channel.connect()
        await message_channel.send("+lyrics")

    else:
        await voice_channel.connect()
        await message_channel.send(DiscordPlay)

    listener()

#listens for play command
def player():
    print("Hi Danny, what do you want?")
    print("Commands: 'play ...' / 'what's playing' / 'skip' / 'lyrics' / 'loop'")
    with sr.Microphone() as source:
        global play_audio
        play_audio = r.listen(source)
        print("You said: " + r.recognize_google(play_audio))

        global DiscordPlay # variable used to ask rhythm_automation to play a song
        DiscordPlay = "+" + r.recognize_google(play_audio)

        bot.run(token, bot=False)
        listener()

#exception handling if incorrect command heard
def error():
    print("The bot couldn't understand what you said")
    print("You said: " + r.recognize_google(audio))
    listener()

#listens for "hey lamp" / "hey lampy" / "hey streetlamp"
def prompt():
    while True:
        if r.recognize_google(audio) in VOICE_COMMANDS:
            print("You said: " + r.recognize_google(audio))
            player()
        else:
            error()

try:
    listener()

#exception handling
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition")
