import discord
import asyncio
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('디엠으로 공지 보내는중! 받기 싫으시면 차단 해주세요')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    #메시지 관리권한이 있을시 사용가능
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(color=0x1DDB16, timestamp=message.created_at)
                        embed.add_field(name="📢 AENT에서 메일 한 통이 도착했습니다. 📢", value=msg, inline=True)
                        embed.set_footer(text="받기 싫으시면 차단 부탁드립니다 XD ")
                        await i.send(embed=embed)
                except:
                    pass


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
