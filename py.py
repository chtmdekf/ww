import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
	print(client.user.id)
	print("Ready!")
	game = discord.Game("s!download")
	await client.change_presence(status=discord.Status.online,activity=game)

@client.event
async def on_message(message):

	if message.content.startswith("s!download"):
		
		embed = discord.Embed(colour = 0x00eeff)
		embed.add_field(name='Check ur DM!', value='Please check your Dm!', inline=False)
		await message.channel.send(embed=embed)

		source = requests.get("https://chtmdekf.github.io/download/s/key.txt").text
		embed2 = discord.Embed(colour = 0x00eeff)
		embed2.add_field(name='console bootstrapper : ', value='https://chtmdekf.github.io/download/s/e02df', inline=False)
		embed2.add_field(name='key : ', value='```' + source + '```', inline=False)
		await message.author.send(embed=embed2)

client.run("NzE4Mzk3MjM1OTY4MjEzMDAz.Xtovjg.pOQO3xll63GytT_es34S-YC9GTw")
