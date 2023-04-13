import discord
import logging


TOKEN = "MTA5NjA2MTUzMTg3NzI4NjAyOQ.Ga92RG.6SaXnCqnB9hmV_9ktRFRTHYo4twGzdq9IUG6bA"

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)


class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "привет" in message.content.lower():
            await message.channel.send("И тебе привет")
        else:
            await message.channel.send("Спасибо за сообщение")


intents = discord.Intents.default()

client = YLBotClient(intents=intents)
client.run(TOKEN)

