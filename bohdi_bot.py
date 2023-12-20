import discord
from discord.ext import commands
import random

# Your list of random phrases
random_phrases = [
    "I am the king, bohdi, bohdishaman or Jaheiraa, but for a less syllable-intensive workout, you may refer to me as Sir.",
    "I didn't know they had internet in the gulag.",
    "It's arrabbiata sauce... not tomato sauce, educate yourself you gulag food-eating simpleton!",
    "I got kicked from Rigged because Hickory couldn't deal with me high rolling comets trail on my druid alt and being a bitch with it. #Standwithbohdi",
    "#itwasafairroll",
    "HELP IVE TURNED INTO HICKORI!!!! 🪱",
    "i wont raid with prickori again",
    "name is Bohdi, King Bohdi",
    "Is 'hickoriisacunt' still available",
    "Harry hickori is taking me back, replacing you",
    "Imagine kiting anub over the ice patch where boss needs to be tanked",
    "I am surrounded by idiots",
    "This inadvertent punishment banish is killing me, Hickori has cursed me with the pug life",
    "Mate i was like 1 second after the roll, dont be fucking scammers",
    "u guys are a disgrace - looking after ur own instead of respecting the high roll",
    "fucking hard man behind ur screen",
    "looking for a raiding guild clearing all HM content",
    "whilst i feel u guys enjoy ripping hickori cannot help feel this is burning already utterly destroyed bridges. Only the stumps of the bridge remain,bloodied and splintered beyond all repair",
    "strike me down Hickler and I will return more powerful than even you can imagine #standwithbohdi",
    "has there been any indication Hickorii got my letter",
    "My Liege, Know that I am truly sorry. I am sorry that I highrolled an item in your glorious pug raid and people didn't appreciate it. I am sorry I am a bad winner, it is in my nature, as King. I am sorry I send you some delicious 5 day old fish. And I am most certainly sorry for daring to accuse you of being a dictator for taking what on the face of it was clearly the only reasonable and level headed approach to my many mistakes. by removing me from discord and the guild./The King, Bohdi 👑",
    "man Hickorii needs to get over himself. Egotistical and cant take a joke. Guy needs to get to the gym and burn off some energy instead of nerd raging over a joke smh. Thinks WOW is the hickori show, well it isnt. more to the game than one mans ego",
    "my dog plays hpala, she only has 3 legs",
    "The sooner you accept the truth, the sooner you will improve",
    "Just take 1 x bohdishaman and all your healing issues will disappear",
    "unfortunately the 🤴 is busy otherwhise I would of come for them achives 👑",
    "low signs ups what can a man do 🤷‍♂️",
    "Yeah they did good. Would of been a kill weeks ago with the shaman King",
    "You eat gulag good. My dog eats better than u",
    "My dog eats your logs I.e shite",
    "I cannot be accountable for lack of progress due to absences. We will get it done. Regardless, are you playing like 1 handed or letting your dog do the buttons? Serious question...",
    "What is season of mastery I'm literally clueless",
    "Lil bro? ill bench press u for reps lil ruskie forgotten land lad",
    "Yeah that made sense Manx but before that someone literally wrote 'you are going round to the right' and then another said I am going anti clockwise. Well Anti clockwise is going to the left, that's where the confusion arose. Hey either way me and Undying/Deathshade smashed it we got those healing buffs like a couple of olympic level synchronised swimmers",
    "Now to find a group for mag/gruul, wow that was fast within 30 seconds I get a raid. Then I am asked for the humiliation of having to attend to have my gear inspected. Do they not know who I am, oh great king in my naxx shoulders? Dogs. But I did what I was asked",
    "You literally eat prison food, I wouldn't expected you to appreciate a nice cote de rhone and some fine cheese n meat",
    "Your portions can only be described as 'a grape with a foreskin' or a 'budgie's tongue'",
    "Mate you eat like you live in a prison and your logs look like u using prison WiFi. If I were you I'd just admit to getting sucked off by your own father to save yourself from any further embarrassment",
    "No Bohdi No Party",
    "Establishment in Northerend of a national home for the Pala King",
    "Kicked from discord because hick can't take a joke",
    "Got COMET - The tears of hickori and alter are flowing 🤣🤣🤣🤣",
    "Nah when I was reading into the whole flower weaving and bear weaving I was like fuck that , that isn't how its meant to be",
    "I've literally been doing feral druid play since classic first came out but got ridiculed as it wasn't great dps in classic",
    "I'm being punished because I won the comet in his pug fair and square. I high rolled it. I won. It upset some of the more regular puggers. Not my fault I played by the rules that were there",
]

# Function to select a random phrase
def select_random_phrase():
    return random.choice(random_phrases)

# Discord bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} new message test')

@bot.command(name='bohdi')
async def bohdi_command(ctx):
    # Send a random phrase as a reply
    await ctx.send(select_random_phrase())

@bot.command(name='Bohdi')
async def bohdi_uppercase_command(ctx):
    # Send a random phrase as a reply
    await ctx.send(select_random_phrase())

# Run the bot with the token
bot.run('MTE4Njc1Mjg5NTgxMTU5NjQyOQ.GqFGx-.zxB0bOG2DLvh_a_KNFIhXKNOjvBFDby0KUOobw')