import random, discord, asyncio, os, time, json
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands import Bot
from AntiSpam import AntiSpamHandler
from pretty_help import PrettyHelp
from datetime import datetime
from PIL import Image
from io import BytesIO

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents().all()
intents.members = True
bot = commands.Bot(command_prefix=["bob ", "BOB ", "Bob ", "bOb "], case_insensitive=True, intents=intents, help_command=PrettyHelp(active_time=60, color=0xff2676, ending_note="To see more information about a specific command, just do 'bob help' and type the command name after!\nTo see all the commands, click the right-arrow reaction. Yup, that easy!", no_category="More Lies Ahead..."))
mainshop = [{"name": "Bobinator", "price":400, "description": "Turns your friends into a big fat Bob"},
            {"name": "Goo-Goo Gas", "price":450, "description": "Makes everyone laugh for no reason"},
            {"name": "Test-Product", "price":1, "description": "Just a test product for Bob's devs to use"}]
global spamstops
spamstops = False
welcomepersonalmsg = None
if spamstops == False:
  bot.handler = AntiSpamHandler(bot)
else:
  pass

pollNames = ["A New Poll!", "Dun Dun Dunnnn...", "OMG NEW POLL", "It's free poll estate", "You want a poll, you *got* a poll!", "It's a *Poll-io* (badum crash)", "I've polling foreverrrr", "Guess what? Polls!", "pOlLs", "t h i c c  p o l l", "Potato Pollato", "Shoutout to Phil the *Poll*ato! ('booo')"]
aintsupposedtobeheresunnyboy = ["https://media.makeameme.org/created/403-you-know.jpg", "https://memegenerator.net/img/instances/24124974/ill-send-you-guys-a-link-that-doesnt-work.jpg", "https://th.bing.com/th/id/Rc0a8166275967865cb1e63d7bbe3794d?rik=qNfrA5ErTTcWuw&riu=http%3a%2f%2fwww.quickmeme.com%2fimg%2fac%2facd3579adc1c3a114d879c9b95ab02d9d8b0026687c1ccb5ae08fce5ec94bb6c.jpg&ehk=k0gYVNy4uzN8m90oUVEgu1kPINyNRpd1QVxM8k5SGkY%3d&risl=&pid=ImgRaw", "https://pics.me.me/403-this-is-a-forbidden-area-i-like-this-one-43196017.png", "https://th.bing.com/th/id/Re9549e514dd51435b747c3d5beca095e?rik=VfupznfsW1%2fExg&riu=http%3a%2f%2fcatplanet.org%2fwp-content%2fuploads%2f2014%2f09%2fCats-as-error-message-403.jpg&ehk=M6vlv0lDHd%2b9R1teH%2b6vIG5XzkZAptDRugQ4NR362D8%3d&risl=&pid=ImgRaw", "https://i.kym-cdn.com/entries/icons/facebook/000/000/091/TrollFace.jpg"]
greetings = ["Hey man", "Whassap boi", "Hola", "Bonjour!", "Yello", "Heyyyy", "Greetings, my king!", "h i  t h e r e", "Whats poppin my man"]
finishHim = ["hit by", "struck by", "destroyed by", "shattered by", "vamooshed by", "intricately-wrapped-up-into-a-ball-and-kicked-away by", "sliced like a watermalone by", "nommed up by", "whooped by", "run over by", "yeeted by", "checkered by", "hippied by", "roasted by", "*s i m m e r e d* by", "yoinked by", "heplapoded by", "narwhaled by", "spiked by"]
weaponsForDend = ["lightsaber", "thor's hammer", "raccoon", "cat", "gauntlet ('s n a p')", "bayonet", "nerf shooter", "bob", "snake", "elephant"]
nomrc = ["oh you playin minecraft\n\ni like ya cut g", "no u", "nahh i'll pass", "i'm in my mums car                          vroom vroom", "yeet boi", "KICK HIM HE TRIED TO BLABORATE MR.C", "hehe boi\n\nnope", "try again, that ain't gonna work with me"]
eightballlist = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful", "Probably not", "I do not believe so", "Skeptical about that", "Seems unsure", "Absolutely not"]
allowbd = False

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.CheckFailure):
    await ctx.send("Sorry my good user but you don't have the correct role to do that. I'm sorry to disappoint you. If you want to do something like make a new channel, kick a user, or something else, you gotta have the role 'Admin' (case sensitive too, it should be at the top of the roles list, and you don't actually need to give the administrator permission; just make a new role called Admin itself!)")
  elif isinstance(error, commands.errors.CommandNotFound):
    await ctx.send("Aw man, sorry but I don't know what that command is! Maybe try using another command? Or type 'bob help' for more information? I dunno ¯\_(ツ)_/¯")
  elif isinstance(error, commands.errors.BadArgument):
    await ctx.send("Sorry, I couldn't find that member!")
  elif isinstance(error, commands.CommandOnCooldown):
    msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
    return await ctx.send(msg)
  elif isinstance(error, commands.MissingRequiredArgument):
    arg = error.param.name
    await ctx.send(f"```Oops!\nHey there, {ctx.author.display_name}! I just want to inform you that when you tried messaging me, you forgot to include this part of the command in your message:\n\n{arg}\n\nIf you want to see more about a command, just type 'bob help' to see a list of all of them!```")

@bot.event
async def on_message(message):
  if message.author.id == 814958813298819092:
    pass
  else:
    if spamstops == False:
      """
      await bot.handler.propagate(message)
      await bot.process_commands(message)
      """
    else:
      pass
    await bot.process_commands(message)
    

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="'bob help' || ver 2.2.0"))
  print("Bob Bot is ready boi")

@bot.event
async def on_member_join(member: discord.Member):
  if welcomepersonalmsg == None:
    memberjoin = discord.Embed(title=f"Hey *{member}*, welcome to *{member.guild}*!", description=f"Hi there! I'm Bob Bot, a bot used in the server {member.guild}. I just wanted to drop by to tell you to have a great time in this server!", color=0xff9054)
  else:
    memberjoin = discord.Embed(title=f"Hey *{member}*, welcome to *{member.guild}*!", description=f"Hi there! I'm Bob Bot, a bot used in the server {member.guild}. I just wanted to drop by to tell you to have a great time in this server!\n{welcomepersonalmsg}", color=0xff9054)
  await member.send(embed=memberjoin)

@bot.command(name="hello", aliases = ["hi", "sup", "hey", "hola", "bonjour", "greetings", "yo", "hallo", "ello", "ello mate", "whats up", "what up", "whassap", "how ya doin", "hows it going", "how it going", "how is it going"], help="Simply responds with a greeting to a user.")
async def hello(ctx):
  response = random.choice(greetings)
  await ctx.send(response)

@bot.command(name="roll", aliases=["rolldice"], help="Rolls a dice for you. The first number is the number of dice, and the second is the number of sides.")
async def rollit(ctx, number_of_dice:int=1, number_of_sides:int=6):
  dice = [
    str(random.choice(range(1, number_of_sides + 1)))
    for _ in range(number_of_dice)
  ]
  
  diceem = discord.Embed(title="Result(s): " + ', '.join(dice), description="The amount of numbers is the number of dice you wanted.", color=0x854dff)
  diceem.set_thumbnail(url="http://www.clker.com/cliparts/f/9/a/f/1216179531563743945ytknick_A_die.svg.hi.png")
  diceem.set_footer(text=f"Rolled by {ctx.author.name}", icon_url = ctx.author.avatar_url)
  await ctx.send(embed=diceem)

@bot.command(name="flipacoin", aliases=["coinflip", "coinf"], help="Flips a coin for you.")
@commands.cooldown(1, 15, commands.BucketType.user)
async def flipacoin(ctx, side: str, bet: int):
    users = await get_bank_data()
    user = ctx.author
    if side == "heads" or side == "tails":
        sides = ["heads", "tails"]
        sidepick = random.choice(sides)
        result = ""
        if sidepick == side:
            result = "won!"
            money = bet * 2
        else:
            result = "lost."
            money = -1 * bet
        coinem = discord.Embed(title=f"{sidepick} - You {result}", description=f"Your pick: **{side}** • Result: **{sidepick}**", color=0xDC7F64)
        coinem.add_field(name="Omegas earned", value=f"Whoop whoop, `Ω{money}`")
        coinem.set_thumbnail(url="https://www.freepngimg.com/thumb/bitcoin/59787-cash-bitcoin-scalable-vector-graphics-logo.png")
        coinem.set_footer(text=f"Flipped by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=coinem)
        users[str(user.id)]["pocket"] += money
        with open("mainbank.json", "w") as f:
          json.dump(users, f)
    else:
        await ctx.send(f"**{ctx.author.name}**, that is not a valid side name!")

@bot.command(name='newChannel', help="Makes a new channel in the Discord server. To use this command, you must have the role 'Admin' (case sensitive!).")
@commands.has_role('Admin')
async def makethatchannelboi(ctx, channel_name, category_name):
  guild = ctx.guild
  existing_channel = discord.utils.get(guild.channels, name=channel_name)
  existing_category = discord.utils.get(ctx.guild.categories, name=category_name)
  if not existing_channel:
    if not existing_category:
      reactforcats = discord.Embed(title="You need to confirm first", description="To make sure you want to make a new channel, you must confirm with Bob.", color=0x9224ed)
      reactforcats.set_author(name="Really wanted by " + ctx.author.display_name, url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
      reactforcats.add_field(name="Inconvenience? Never heard of him.", value="I'm just doing my job, man! You can't hate on me if this is inconvenient for you. It's just a simple reaction, anyway.", inline=False)
      reactforcats.add_field(name="What to do", value="Respond to this message with this specific reaction: 👍. This will confirm you want to create a new category for this channel.")
      reactforcats.set_footer(text="This was an automated message sent to you by Bob Bot 2.0.0. This bot is not responsible for any vulgar slurs, inappropriate content, or insults. If a user has been doing any of these to you, consider reporting them to Discord.")
      await ctx.send(embed=reactforcats)

      def check(reaction, user):
          return user == ctx.message.author and str(reaction.emoji) == '👍'
      try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
      except asyncio.TimeoutError:
        await ctx.send("Some kind of error occured. Sowwy.")

      new_category = await ctx.guild.create_category(category_name)
      await guild.create_text_channel(channel_name, category=new_category)
      await ctx.send(f"Alright, {channel_name} has been created by Bob in the category {category_name}")
      print(f"{ctx.author.display_name} made channel on '{ctx.guild.name}': {channel_name}")
    else:
      await guild.create_text_channel(channel_name, category=existing_category)
      await ctx.send(f"Alright, {channel_name} has been created by Bob in the category {category_name}")
      print(f"{ctx.author.display_name} made channel on '{ctx.guild.name}': {channel_name}")
  else:
    await ctx.send(f"Whoa whoa whoa yo yo yo, {channel_name} already exists")
    print(f"{ctx.author.display_name} tried to make channel on '{ctx.guild.name}' but was already there")

@bot.command(name='sendDM', aliases = ["DM", "direct message", "dir msg", "direct msg"], help="Sends a private direct message to a specified user.")
async def dm(ctx, user: discord.User, *, value):
  if user == ctx.author:
      await ctx.send(f"Uhhhh {ctx.author.display_name}, I can't send a message to yourself...")
  else:
      embeda=discord.Embed(title=value, description=f"Sent on server: **{ctx.guild.name}**\nSent by: **{ctx.author.display_name}**", color=0x3366ff)
      embeda.set_author(name=ctx.author.display_name, url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
      embeda.set_footer(text="This bot is not responsible for any vulgar slurs, inappropriate content, or insults.")
      await user.send(embed=embeda)

      embed2=discord.Embed(title=f"Good day {ctx.author.display_name}, your message to {user} was successfully sent!", description=f"The message you sent to {user} on the server **{ctx.guild.name}** was sent! You can review your message below.", color=0x3366ff)
      embed2.set_author(name=user.display_name, url=random.choice(aintsupposedtobeheresunnyboy), icon_url=user.avatar_url)
      embed2.add_field(name="Review your message:", value=f"*{value}*", inline=False)
      embed2.set_footer(text="This was an automated message sent to you by Bob Bot 2.0.0. This bot is not responsible for any vulgar slurs, inappropriate content, or insults. If a user has been doing any of these to you, consider reporting them to Discord.")
      await ctx.author.send(embed=embed2)
    
      print(f"{ctx.author.display_name} to {user} on '{ctx.guild.name}': {value}")

@bot.command(name='makePoll', help="Makes a new poll that other users can vote for. Bob Bot may be erroring out because it does not have the highest permissions in the server, so you will need to give it roles to kick users.")
async def makeapoll(ctx,*, message : str):
    embed=discord.Embed(title=random.choice(pollNames), description=message, color=0xfcd602)
    embed.set_author(name=ctx.author.display_name + " (you can end this poll by reacting with this: 🔴)", url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
    mymsg = await ctx.send(embed=embed)
    embed.set_footer(text="This was an automated message sent to you by Bob Bot 2.0.0. This bot is not responsible for any vulgar slurs, inappropriate content, or insults. If a user has been doing any of these to you, consider reporting them to Discord.")
    await mymsg.add_reaction('✅')
    await mymsg.add_reaction('❌')

    def check(reaction, user):
      return user == ctx.message.author and str(reaction.emoji) == '🔴'
    try:
      reaction, user = await bot.wait_for('reaction_add', check=check)
    except asyncio.TimeoutError:
      await ctx.send("Some kind of error occured. Sowwy.")

    #thanks to user @thegamecracks for the reaction DMing part- view their profile here: https://stackoverflow.com/users/14312437/thegamecracks
    mymsg = await mymsg.channel.fetch_message(mymsg.id)

    choices = ['✅', '❌']
    counts = {}
    for emoji in choices:
      reaction = discord.utils.get(mymsg.reactions, emoji=emoji)
      counts[emoji] = reaction.count - 1
    results = counts
    pollEmbed = discord.Embed(title=f"Poll results for *{ctx.author.display_name}*!", description=f"You just declared that the poll you made had ended. Welp, here are the results!", color=0xfcd602)
    pollEmbed.set_author(name="Poll's Creator: " + ctx.author.display_name, url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
    pollEmbed.add_field(name="The final results:", value=f"The answer count: {results} (does not include Bob Bot's reaction)\n\nYour poll question: {message}\n\nThanks for using Bob Bot as a poll creator!", inline=False)
    await ctx.author.send(embed=pollEmbed)

    deletionEmbed = discord.Embed(title="This ends now!", description="It's over, Anakin... I have the high ground", color=0xfcd602)
    deletionEmbed.add_field(name="The poll ended!", value=f"The poll's author {ctx.author.display_name} just declared that the poll ended. RIP poll :(\n\nFor those of you who missed the question, here it is: *{message}*\n\n{ctx.author.display_name}, the results of the poll should have been DMed to you right about now. Happy statistical advancement!", inline=False)

    await mymsg.edit(embed=deletionEmbed)

@bot.command(name="fight", help="Fights with another user (your choice).")
async def fight(ctx, user: discord.Member):
  if ctx.author == user:
    await ctx.send("Fight yourself???")
  else:
    fight = Image.open("C:\\Users\\admin\\Downloads\\bob-bot-fight-command.jpg")

    asset_author = ctx.author.avatar_url_as(size=64)
    asset_member = user.avatar_url_as(size=64)
    data_author = BytesIO(await asset_author.read())
    data_member = BytesIO(await asset_member.read())
    pfp_author = Image.open(data_author)
    pfp_member = Image.open(data_member)

    pfp_author = pfp_author.resize((73, 73))
    pfp_member = pfp_member.resize((205, 205))
    fight.paste(pfp_author, (226, 61))
    fight.paste(pfp_member, (381, 61))
    fight.save("fight-profile.jpg")

    await ctx.send(file = discord.File("fight-profile.jpg"))

@bot.command(name="monkey", help="Turns someone into a monkey... maybe...")
async def monkey(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.author
  monkey = Image.open("C:\\Users\\admin\Downloads\\bob-bot-monkey-command.jpg")

  asset = user.avatar_url_as(size=64)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)

  pfp = pfp.resize((73, 76))
  monkey.paste(pfp, (258, 78))
  monkey.save("monkey-profile.jpg")

  await ctx.send(file = discord.File("monkey-profile.jpg"))

@bot.command(name="trash", help="Don't mind me just taking out the trash.")
async def trash(ctx, user: discord.Member):
  if ctx.author == user:
    await ctx.send("Fight yourself???")
  else:
    trash = Image.open("C:\\Users\\admin\Downloads\\bob-bot-trash-command.jpg")

    asset_author = ctx.author.avatar_url_as(size=64)
    asset_member = user.avatar_url_as(size=64)
    data_author = BytesIO(await asset_author.read())
    data_member = BytesIO(await asset_member.read())
    pfp_author = Image.open(data_author)
    pfp_member = Image.open(data_member)

    pfp_author = pfp_author.resize((86, 83))
    pfp_member = pfp_member.resize((122, 123))
    trash.paste(pfp_author, (200, 129))
    trash.paste(pfp_member, (329, 189))
    trash.save("trash-profile.jpg")

    await ctx.send(file = discord.File("trash-profile.jpg"))

@bot.command(name='kickUser', help="Kicks a member out of the server. If no reason is specified, then the reason is passed in as None. To use this command, you must have kick members permissions.")
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *, reason = None):
  if user.id == 814958813298819092:
    await ctx.send("Not today sunny boy, you can't kick me")
  elif user.id == 804777320123990108:
    await ctx.send("Not today sunny boy, you can't kick one of my creators")
  elif user.id == 804780050318622730:
    await ctx.send("Not today sunny boy, you can't kick one of my creators")
  else:
    if not reason:
        embed3=discord.Embed(title=f"{user}, you were kicked from {ctx.guild.name} by {ctx.author.display_name}!", description=f"I'm sorry, but no reason was actually specified. :( To join the server again, contact the person who kicked you, {ctx.author.display_name}.", color=0xf41004)
        embed3.set_author(name=ctx.author.display_name, url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
        embed3.set_footer(text="This was an automated message sent to you by Bob Bot 2.0.0. This bot is not responsible for any vulgar slurs, inappropriate content, or insults. If a user has been doing any of these to you, consider reporting them to Discord.")
        await user.send(embed=embed3)
    else:
      embed3=discord.Embed(title=f"{user}, you were kicked from {ctx.guild.name} by {ctx.author.display_name}!", description=f"**Reason why**:\n{reason}\n\nTo join the server again, contact the person who kicked you, {ctx.author.display_name}.", color=0xf41004)
      embed3.set_author(name=ctx.author.display_name, url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
      embed3.set_footer(text="This was an automated message sent to you by Bob Bot 2.0.0. This bot is not responsible for any vulgar slurs, inappropriate content, or insults. If a user has been doing any of these to you, consider reporting them to Discord.")
      await user.send(embed=embed3)

    if not reason:
      await ctx.guild.kick(user)
      await ctx.send(f"Aw man, **{user}** has been kicked for really no specified reason. Rest In Peace, fellow user")
    else:
      await ctx.guild.kick(user)
      await ctx.send(f"Aw man, **{user}** has been kicked for this following reason: **{reason}**. Rest In Peace, fellow user.")

@bot.command(name='inviteToGuild', help="Gives the invitation link for Bob Bot so you can connect him to other servers.")
async def inviteBob(ctx):
  await ctx.send(f"{ctx.author.display_name}, here is my invite link! https://discord.com/api/oauth2/authorize?client_id=814958813298819092&permissions=8&scope=bot")

@bot.command(name='allMembers', help="Retrieves all members from a server.")
async def fetchAllUsers(ctx):
    for member in ctx.guild.name.members:
        await ctx.send(member)

@bot.command(name='userInfo', help="Gives general information about a user.")
async def info(ctx, *, member: discord.Member):
  memberInfo=discord.Embed(title=f"Alright, let's take a look at *{member}*", description="We're just getting some general basic information about this user...", color=0xfcd602)
  memberInfo.set_author(name="Requested by " + ctx.author.display_name, url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
  memberInfo.add_field(name="User ID:", value=str(member.id))
  memberInfo.add_field(name="Joined Server:", value=f"{ctx.guild.name}.", inline=True)
  memberInfo.add_field(name="When Joined (most recently):", value=f"Joined the server on {member.joined_at}")
  memberInfo.add_field(name="Total Roles:", value=f"They have {(len(member.roles))-1} role(s).")
  if member.status == "dnd":
    memberInfo.add_field(name="Current Status:", value="Currently on Do Not Disturb.")
  else:
    memberInfo.add_field(name="Current Status:", value=f"Currently {member.status}.")
  memberInfo.add_field(name="Account Creation:", value=f"Created account on {member.created_at}.")
  memberInfo.set_thumbnail(url=f"{member.avatar_url}")
  memberInfo.set_footer(text="This was an automated message sent to you by Bob Bot 2.0.0. This bot is not responsible for any vulgar slurs, inappropriate content, or insults. If a user has been doing any of these to you, consider reporting them to Discord.")
  memberInfo = await ctx.send(embed=memberInfo)

@bot.command(name='avatar', help="Retrieves the profile picture of a specified user.", aliases=["getpfp", "av", "getProfilePic"])
async def pfp(ctx, *, member: discord.Member):
  serverProfilePic = discord.Embed(title=f"**{member}'s** avatar", color=0xfcd602)
  serverProfilePic.set_author(name=ctx.author, icon_url=ctx.author.avatar_url())
  serverProfilePic.set_image(url=f"{member.avatar_url}")
  serverProfilePic.set_footer(text="nitro nitro nitro nitro")
  await ctx.send(embed=serverProfilePic)

#GOTTA WORK ON THIS MUTING STUFF
@bot.command(name='muteUser', help="Mutes a user throughout the Discord server so they cannot send messages in channels.")
@commands.has_permissions(manage_messages=True)
async def mutedem(ctx, member: discord.Member, *, reason=None):
  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")
  if not mutedRole:
    mutedRole = await guild.create_role(name="Muted") 
    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
  await member.add_roles(mutedRole)
  mutede = discord.Embed(title="Ooh, mute!", description="This isn't a Zoom, but... eh, it's a *mute*", color=0xe0dada)
  mutede.set_author(name=f"Done by {ctx.author.display_name}", url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
  if reason:
    mutede.add_field(name=f"{member} was muted!", value=f"This is why: {reason}")
  else:
    mutede.add_field(name=f"{member} was muted!", value=f"There wasn't any reason... darn!")
  await ctx.send(embed=mutede)
  
  muteduser=discord.Embed(title=f"{member}, you were muted in {ctx.guild.name} by {ctx.author.display_name}!", description=f"**Reason why**:\n{reason}\n\nTo be unmuted, you can ask anyone with the permissions *manage messages* or unmute yourself if you can do that.", color=0xf41004)
  muteduser.set_author(name=ctx.author.display_name, url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
  muteduser.set_footer(text="This was an automated message sent to you by Bob Bot 2.0.0. This bot is not responsible for any vulgar slurs, inappropriate content, or insults. If a user has been doing any of these to you, consider reporting them to Discord.")
  await member.send(embed=muteduser)

@bot.command(name='unmuteUser', help="Unmutes a user throughout the Discord server so they can once again send messages in channels.")
@commands.has_permissions(manage_messages=True)
async def unmutedem(ctx, member: discord.Member, *, reason=None):
  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")
  if not mutedRole:
    mutedRole = await guild.create_role(name="Muted")
    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
  await member.remove_roles(mutedRole)
  await ctx.send(f"{member} has been unmuted!")


"""
@bot.command(name='startCount', help="Starts a basic countdown to 1. Can be useful in some cases, but most likely will not be used in general.")
async def count(ctx, message : in
t):
  count = message
  if count < 100000:
    msg = await ctx.send(message)
    while message > 0:
      await asyncio.sleep(1)
      await msg.edit(content=count)
      count -= 1
      if count < 0:
        break
      if count == 0:
        await ctx.send(f"HEY **{ctx.author.display_name}**, COUNTDOWN IS OVER!!!")
  else:
    await ctx.send(f"Whoa whoa whoa, sorry {ctx.author.display_name.upper()} but I can only start a countdown under 100000!")
"""

@bot.command(name='spamGoff', help="Disables the built-in spam warnings for Bob Bot, which is used if you want people to intentionally spam in your server.")
@commands.has_role('Admin')
async def spamisoff(ctx, spamstops = False):
  if spamstops == True:
    await ctx.send("Spam protection has already been disabled! ❌")
  else:
    spamstops = True
    guild_owner = await bot.fetch_user(ctx.guild.owner.id)
    await ctx.send(f"OK {ctx.author.display_name}, spam protection has been turned off! Just to make sure this decision was confirmed, the owner of this server {guild_owner} will be informed of this change.")

    await guild_owner.send(f"**Alert, alert!**\n{guild_owner.mention}, Bob Bot's built-in (and basic) spam protection has been turned off in your server {ctx.guild.name}. This action was performed by {ctx.author.display_name}. To enable spam protection, type 'bob spamGon' in the server where it was turned off.")

"""
@bot.command(name='spamGon', help="Enables the built-in spam warnings for Bob Bot, which is used if you want to prevent spam in your server.")
@commands.has_role('Admin')
async def spamison(ctx):
  if spamstops == False:
    await ctx.send("Spam protection has already been enabled! ✔")
  else:
    spamstops = False
    guild_owner = await bot.fetch_user(ctx.guild.owner.id)
    await ctx.send(f"OK {ctx.author.display_name}, spam protection has been turned on! Just to make sure this decision was confirmed, the owner of this server {guild_owner} will be pinged. <{guild_owner.mention}>")
"""

@bot.command(name='serverStats', help="Gets the statistics of a server.")
async def serverinfo(ctx):
  guild_owner = await bot.fetch_user(ctx.guild.owner.id)
  guild_members = ctx.guild.member_count
  guild_members_no_bots = len([m for m in ctx.guild.members if not m.bot])
  guild_only_members = ctx.guild.member_count - len([m for m in ctx.guild.members if m.bot])

  serverInfo=discord.Embed(title=f"OK, getting the stats of {ctx.guild.name} now.", description="We're just gathering some general basic information about this server...", color=0xfcd602)
  serverInfo.set_author(name="Requested by " + ctx.author.display_name, url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
  serverInfo.add_field(name="All Members Count:", value=f"The total member count (including bots) is: {guild_members}.", inline=True)
  serverInfo.add_field(name="All Bots Count:", value=f"The total bot count (not including actual humans) is: {guild_members_no_bots}.")
  serverInfo.add_field(name="Only Humans Count:", value=f"The total count of members who are actually human (and don't try to be a wise guy/gal) is: {guild_only_members}.", inline=True)
  serverInfo.add_field(name="Server Icon:", value="**Can be seen in the thumbnail.**")
  serverInfo.add_field(name="Server Owner:", value=f"{guild_owner}")
  serverInfo.set_thumbnail(url=f"{ctx.guild.icon_url}")
  serverInfo.set_footer(text="This was an automated message sent to you by Bob Bot 2.0.0. This bot is not responsible for any vulgar slurs, inappropriate content, or insults. If a user has been doing any of these to you, consider reporting them to Discord.")
  serverInfo = await ctx.send(embed=serverInfo)

@bot.command(name='ping', help="Checks the ping of the bot, or in simpler terms, how long it took the bot to reach out to the Discord API and respond to your command.")
async def ping(ctx):
  await ctx.send(f"**Pong!** My ping is `{round(bot.latency * 1000)}`!")

@bot.command(name='pong', help="You're not really supposed to do this...")
async def pong(ctx):
  await ctx.send(f"**Pi- wait**\n\nI can't measure your latency, *{ctx.author.display_name}!* However, you can see my latency (ping) by typing `bob ping`!")

#Note to self: review this function 
@bot.command(name='wlcMsg', aliases=["welcomemsg", "personalwelcomemsg"], help="Sets a personally-made welcome message for new users joining the server.")
@commands.has_role('Admin')
async def personalmsg(ctx, *, message):
  welcomepersonalmsg = str(message)
  print(welcomepersonalmsg)
  await ctx.send(f"**{ctx.author.display_name}, your custom welcome message for new users has been set!**\nReview it below:\n\n*{welcomepersonalmsg}*")

@bot.command(name='dEnd', help="Bablates a user!")
async def dend(ctx, member: discord.User, *, weapon=None):
  if member.id == 804777320123990108 or member.id == 804780050318622730 or member.id == 814958813298819092:
    await ctx.send("Not today sunny boy, you can't blaborate me or either one of my creators")
  elif member.id == 779107655226490880:
    await ctx.send(random.choice(nomrc))
  else:
    if weapon == None:
      await ctx.send(f"Well *{member.mention}* was **{random.choice(finishHim)}** a `{random.choice(weaponsForDend)}` bye bye")
    else:
      await ctx.send(f"Well *{member.mention}* was **{random.choice(finishHim)}** a `{weapon}` bye bye")

@bot.command(name="8ball", help="Asks your question to the magical 8-ball.")
async def eightball(ctx, *message: str):
  ogquestion = ""
  for i in message:
    ogquestion += ('{} ').format(i)
  eightanswer = random.choice(eightballlist)
  eightem = discord.Embed(title=f"*{eightanswer}*", description="The magic 8-ball has spoken!", color=0x0033cc)
  eightem.add_field(name=ogquestion, value="Your original question is above")
  eightem.set_author(name=f"Asked by {ctx.author}", url=random.choice(aintsupposedtobeheresunnyboy), icon_url=ctx.author.avatar_url)
  await ctx.send(embed=eightem)

@bot.command(name="bal")
async def balance(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()
    user = ctx.author
    pocket_amt = users[str(user.id)]["pocket"]
    bigbank_amt = users[str(user.id)]["bigbanks"]
    balem = discord.Embed(title=f"Balance for {ctx.author.display_name}", color=0x66ff99)
    balem.add_field(name="Pocket balance", value=pocket_amt)
    balem.add_field(name="Big banks balance", value=bigbank_amt)
    balem.set_footer(text="do i care")
    await ctx.send(embed=balem)

@bot.command(name="beg")
@commands.cooldown(1, 30, commands.BucketType.user)
async def gamble(ctx):
    people = ["The local bartender", "Aunt Betha", "Uncle Schaffer", "An angel", "Some random dude", "A kind person", "Module64", "Mr.Names", "God", "Dank Memer", "An employee at Microsoft", "Another begger", "Leonardo DiCaprio", "Keanu Reeves"]
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    pock_amt = users[str(user.id)]["pocket"]
    thetitle = ""
    earnings = random.randrange(151)
    if earnings > 100:
        thetitle = f"holy smokes, **`{random.choice(people)}`** gave you a **meaty** `Ω{earnings}`"
    elif earnings < 100 and earnings > 50:
        thetitle = f"good begging skills, **`{random.choice(people)}`** gave you `Ω{earnings}`"
    elif earnings < 50 and earnings > 25:
        thetitle = f"eh, you got a good `Ω{earnings}` from **`{random.choice(people)}`**"
    elif earnings < 25:
        thetitle = f"`😛😛` *suks 2 be u, **`{random.choice(people)}`** g@ve 0nly* `Ω{earnings}`"

    users[str(user.id)]["pocket"] += earnings
    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    begem = discord.Embed(title=thetitle, color=0x21b0fc)
    begem.set_footer(text=f"Pocket money now: §{pock_amt}")
    await ctx.send(embed=begem)

@bot.command(name="work")
@commands.cooldown(1, 30, commands.BucketType.user)
async def jobwork(ctx):
    jobs = ["a bank", "a lemonade stand", "a pet shelter", "a dark web store", "Discord", "Facebook", "meme community", "store for [REDACTED]", "lab rat clinic"]
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    earnings = random.randrange(151)
    title = ""
    if earnings > 100:
        title = f"holy smokes, you worked at **{random.choice(jobs)}** and earned a **saucy** `Ω{earnings}`"
    elif earnings < 100 and earnings > 50:
        title = f"nice work, you worked at **{random.choice(jobs)}** and got a sweet `Ω{earnings}`"
    elif earnings < 50 and earnings > 25:
        title = f"i mean, good enough- you worked at **{random.choice(jobs)}** and took away a good `Ω{earnings}`"
    elif earnings < 25:
        title = f"*OOOF* man worked __12hrs__ at **{random.choice(jobs)}** and only got `Ω{earnings}`"
    balem = discord.Embed(title=title, color=0xff763b)
    balem.set_footer(text="y u not neurosurgeon yet")
    await ctx.send(embed=balem)

    users[str(user.id)]["pocket"] += earnings
    with open("mainbank.json", "w") as f:
        json.dump(users, f)

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["pocket"] = 0
        users[str(user.id)]["bigbanks"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    return True

async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)
    return users

async def update_bank(user, change=0, mode="pocket"):
    users = await get_bank_data()
    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    
    bal = [users[str(user.id)]["pocket"], users[str(user.id)]["bigbanks"]]
    return bal

@bot.command(name="withdraw")
async def withdraw(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Kid you gotta bet some actual omegas (bob's currency)")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("Imaginary omegas don't work here sunny boi, you don't have enough omegas for that transaction")
        return
    if amount < 0:
        await ctx.send("Did ya ever learn math and finance in school? Give a positive value")
        return
    await update_bank(ctx.author, amount, "pocket")
    await update_bank(ctx.author, -1*amount, "bigbanks")
    await ctx.send(f"`Ω{amount}` were just withdrawn from your account, **{ctx.author.display_name}**")

@bot.command(name="deposit", help="Deposits money from your wallet into your bank.", aliases=["dep"])
async def deposit(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Kid you gotta bet some actual omegas (bob's currency)")
        return

    bal = await update_bank(ctx.author)

    if amount == "all":
      amount = bal[0]
    else:
      amount = int(amount)
    if amount > bal[0]:
        await ctx.send("Imaginary omegas don't work here sunny boi, you don't have enough omegas for that transaction")
        return
    if amount < 0:
        await ctx.send("Did ya ever learn math and finance in school? Give a positive value")
        return
    
    await update_bank(ctx.author, -1*amount, "pocket")
    await update_bank(ctx.author, amount, "bigbanks")
    await ctx.send(f"`Ω{amount}` were just deposited from your account, **{ctx.author.display_name}**")

@bot.command(name="send")
async def send(ctx, member: discord.Member, amount = None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send("Kid you gotta bet some actual omegas (bob's currency)")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("Imaginary omegas don't work here sunny boi, you don't have enough omegas for that transaction")
        return
    if amount < 0:
        await ctx.send("Did ya ever learn math and finance in school? Give a positive value")
        return
    
    await update_bank(ctx.author, -1*amount, "bigbanks")
    await update_bank(member, amount, "bigbanks")
    await ctx.send(f"`Ω{amount}` were just put into **{member}**'s account, **{ctx.author.display_name}**")

@bot.command(name="slots")
async def slots(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Kid you gotta bet some actual omegas (bob's currency)")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("Imaginary omegas don't work here sunny boi, you don't have enough omegas for that transaction")
        return
    if amount < 0:
        await ctx.send("Did ya ever learn about money in school? Give a positive value")
        return
    
    final = []
    for i in range(3):
        a = random.choice([":apple:", ":banana:", ":watermelon:"])
        final.append(a)

    for i in final:
        realfinal = str(final).replace("[", " ")

    for j in realfinal:
        realREALfinal = str(realfinal).replace("]", " ")

    for k in realREALfinal:
        absfinal = str(realREALfinal).replace("'", " ")

    for l in absfinal:
        finalfinal = str(absfinal).replace(",", " | ")

    slotem = discord.Embed(title=str(finalfinal), color=0xff9966)
    slotem.add_field(name="SLOT MACHINE", value="Let's see if ya win kid")
    await ctx.send(embed=slotem)
    if final[0] == final[1] or final[0] == final[2] or final[1] == final[2]:
        await update_bank(ctx.author, 2*amount, "pocket")
        slotwinem = discord.Embed(title=f"Good job kid, you won `Ω{2*amount}`", color=0xccff66)
        await ctx.send(embed=slotwinem)
    elif final[0] == final[1] == final[2]:
        await update_bank(ctx.author, 3*amount, "pocket")
        slotallwinem = discord.Embed(title=f"Wow, sweet victory kid, you got `Ω{3*amount}`", color=0xccff66)
        await ctx.send(embed=slotallwinem)
    else:
        await update_bank(ctx.author, -1*amount, "pocket")
        slotloseem = discord.Embed(title=f"Oooh, tough luck kid- you lost `Ω{amount}`", color=0xff3300)
        await ctx.send(embed=slotloseem)

@bot.command(name="steal")
async def steal(ctx, member: discord.Member, amount = None):
    await open_account(ctx.author)
    await open_account(member)

    bal = await update_bank(member)
    bal_robber = await update_bank(ctx.author)

    if bal[0] < 100:
        await ctx.send(f"Sorry **{ctx.author}** but I feel kinda bad for **{member}**, so you can't rob anyone who has less than `Ω100`")
        return
    if bal_robber[0] < 100:
        await ctx.send(f"Oy **{ctx.author}**, make some money on your own first, you better have `Ω100` if you want to steal from someone")
        return
    if member == ctx.author:
        await ctx.send(f"Robbing yourself won't do any good kid")
        return
    
    earnings = random.randrange(0, bal[0]-50)

    await update_bank(ctx.author, earnings, "pocket")
    await update_bank(member, -1*earnings, "pocket")
    await ctx.send(f"**{ctx.author.display_name}** just stole from **{member}** and got `Ω{earnings}`")

@bot.command(name="cart", help="Makes a cart for you where you can store your purchased items from the Bob Bot Shop.")
async def cart(ctx):
  await open_account(ctx.author)
  user = ctx.author
  users = await get_bank_data()

  try:
    cart = users[str(user.id)]["cart"]
  except:
    cart = []

  cartem = discord.Embed(title=f"**{ctx.author}**'s cart", description="Your cart and the items you have", color=0x9999ff)
  for item in cart:
    name = item["item"]
    amount = item["amount"]

    cartem.add_field(name=f"*{name}*", value=amount)
  
  cartem.set_footer(text="moms love shopping")
  await ctx.send(embed=cartem)

@bot.command(name="shop", help="Displays the Bob Bot Shop to buy things.")
async def shop(ctx):
  shopem = discord.Embed(title="Bob Bot Shop", description="Come spend your Omegas here!", color=0x9966ff)

  for item in mainshop:
    name = item["name"]
    price = item["price"]
    desc = item["description"]
    shopem.add_field(name=f"*{name}*", value=f"`Ω{price}` | {desc}")

  await ctx.send(embed=shopem)

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["cart"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["cart"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["cart"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["cart"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"pocket")

    return [True,"Worked"]

async def sell_this(user, item_name, amount, price = None):
  item_name = item_name.lower()
  name_ = None
  for item in mainshop:
    name = item["name"].lower()
    if name == item_name:
      name_ = name
      if price == None:
        price = item["price"]
      break

  if name_ == None:
    return [False, 1]
  
  cost = price * amount
  users = await get_bank_data()
  bal = await update_bank(user)
  
  try:
        index = 0
        t = None
        for thing in users[str(user.id)]["cart"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["cart"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
  except:
      return [False,3]    

  with open("mainbank.json","w") as f:
      json.dump(users,f)

  await update_bank(user,cost,"pocket")

  return [True,"Worked"]

@bot.command(name="buy")
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("The Bob Bot Shop isn't selling that item lol")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money to get **{amount}** `{item}`s")
            return

    await ctx.send(f"*ring ring* Hey **{ctx.author}** here are {amount} `{item}`s")

@bot.command(name="sell")
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("The Bob Bot Shop doesn't have that item lol")
            return
        if res[1]==2:
            await ctx.send(f"You don't have **{amount}** `{item}`s in your cart, kid")
            return
        if res[1]==3:
            await ctx.send(f"You don't have a `{item}` in your cart, kid")
            return

    await ctx.send(f"*ring ring* OK **{ctx.author}**, you just sold {amount} `{item}`s")

@bot.command(name="leaderboard", aliases=["lb"])
async def leaderboard(ctx, ppl=3):
  users = await get_bank_data()
  leader_board = {}
  total = []
  for user in users:
    name = int(user)
    total_amount = users[user]["pocket"] + users[user]["bigbanks"]
    leader_board[total_amount] = name
    total.append(total_amount)

  total = sorted(total, reverse=True)

  leaderem = discord.Embed(title=f"{ppl} Richest Users in **{ctx.guild}**", description="Wealth is calculated based on the amount of money in users' pockets as well as how much they have in their *t h i c c banks*.", color=0xccff66)
  index = 1
  for amt in total:
    id_ = leader_board[amt]
    mem = client.get_user(id_)
    name = mem.name
    leaderem.add_field(name=f"🏅 - {index}. **{name}**", value=f"`{amt}`", inline=False)
    if index == x:
      break
    else:
      index += 1

@bot.command(name='credsWhereDue', help="Just some credits to the creators of this bot and everyone who helped.")
async def credits(ctx):
  await ctx.send("```Bob Bot was created by Module64#8821 and Mr.Names#8920. Their goal was to create a bot that could be used both for utility commands (such as managing your server), as well as being a general chatbot that you could talk with.\nA note from the creators:\n\nThis was one of the most challenging projects we made so far because it required hours of debugging and countless days of messaging the bot back and forth. However, it was also the most enjoyable project we have ever created. We could not have made this bot without our friends stonks#9652 and ysc#6836, who helped with the Python code. StackOverflow was also basically our lifesaver during the making of bot. So, uhhh, yeah.\n\nNot much of an inspirational story, but we weren't meant to write motivational stories anyway! OH YEAH, PARTY TIMMEEEE```")

bot.run(TOKEN)