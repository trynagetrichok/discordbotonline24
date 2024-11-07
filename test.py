import os
import discord
from discord.ext import commands

from myserver import server_on

bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print ('bot online')
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1301930591503126630) 
    
    link_channel_id = 1301930510213189682
    guild_id = member.guild.id  # ใช้ ID เซิร์ฟเวอร์ของสมาชิก

    # สร้างลิงก์ที่จะไปยังห้อง
    link = f"https://discord.com/channels/{guild_id}/{link_channel_id}"
    
    
    text = f"สวัสดีคุณ {member.mention} !"
    
    
    emmbed = discord.Embed(
        title='ร้าน TRY DDC ยินดีต้อนรับ กรุณายืนยันตัวตน ก่อนเข้าใช้งาน !',
        description=f"{text} กรุณายืนยันตัวตน ที่ห้อง ({link}) ก่อนเข้าใช้งาน!",
        color=0x66FFFF
    )
    
    await channel.send(text)
    await channel.send(embed = emmbed)

server_on()   
    
bot.run(os.getenv('TOKEN'))