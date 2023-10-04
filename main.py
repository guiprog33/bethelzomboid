import discord
from datetime import datetime
import re


 
class MyClient(discord.Client):
    async def on_ready(self):
        print(self)
        print(dir(self))
        print(dir(self.intents))
        print(self.guilds[0])
        print(self.intents._has_flag)

        channel = self.get_channel(int(CHANNEL_ID))
        await channel.send("Hello I'm zombie bot")

    async def on_message(self, message):
        if message.author == self.user:
            return  

        arg = message.content.split()
        if message.content == 'ping':
            await message.channel.send('pong {0.author.mention}'.format(message))
        elif arg[0] =="/join" :
            self.get_all_channels
        elif arg[0] == "/kill" :
            kill = arg[1]
            if kill.isdecimal() :
                killNum = int(kill)
                rank = ""
                if killNum < 100 :
                    rank = "훈련병"
                elif killNum < 500 :
                    rank = "이등병"
                elif killNum < 1000 :
                    rank = "일병"
                elif killNum < 1500 :
                    rank = "상병"
                elif killNum < 2000 :
                    rank = "병장"
                elif killNum < 2500 :
                    rank = "하사"
                elif killNum < 3000 :
                    rank = "중사"
                elif killNum < 3500 :
                    rank = "상사"
                elif killNum < 4000 :
                    rank = "원사"
                elif killNum < 4500 :
                    rank = "준위"
                elif killNum < 5000 :
                    rank = "소위"
                elif killNum < 5500 :
                    rank = "중위"
                elif killNum < 6000 :
                    rank = "대위"
                elif killNum < 7000 :
                    rank = "소령"
                elif killNum < 8000 :
                    rank = "중령"
                elif killNum < 10000 :
                    rank = "대령"
                elif killNum < 15000 :
                    rank = "준장"
                elif killNum < 20000 :
                    rank = "소장"
                elif killNum < 30000 :
                    rank = "중장"
                elif killNum < 50000 :
                    rank = "대장"
                else :
                    rank = "원수"

                old = message.author

                new = message.author

                new.nick.replace("#훈련병","") 
                new.nick.replace("#이등병","") 
                new.nick.replace("#일병","") 
                new.nick.replace("#상병","") 
                new.nick.replace("#병장","") 
                new.nick.replace("#하사","") 
                new.nick.replace("#중사","") 
                new.nick.replace("#상사","") 
                new.nick.replace("#원사","") 
                new.nick.replace("#준위","") 
                new.nick.replace("#소위","") 
                new.nick.replace("#중위","") 
                new.nick.replace("#대위","") 
                new.nick.replace("#소령","") 
                new.nick.replace("#중령","") 
                new.nick.replace("#대령","") 
                new.nick.replace("#준장","") 
                new.nick.replace("#소장","") 
                new.nick.replace("#중장","") 
                new.nick.replace("#대장","") 
                new.nick.replace("#원수","") 
                nickname = new.nick+"#"+rank

                
                await message.channel.send("킬로그 수집 :" + kill + ", 당신의 계급은 " + rank + "입니다.")
                print(dir(self))
                print(self.get_guild(message.guild.id))
                guild = self.get_guild(message.guild.id)
                print(guild)
                user = guild.get_member(message.author.id)
                print(user)



                # print(message.author)
                # print(type(message.author))
                
                # print(dir(message.author))
                # print(message.author.nick)
                await user.edit(nick=nickname )
                # for user in self.users :
                #     print(user)
                #     print("------------------")
                #     if user == message.author :
                        
                #         print(dir(user))
                #         print(user.id)
                #         print(" Check in ")
                


            else:
                await message.channel.send("킬 정보는 숫자만 입력해주세요.")
 

 
TOKEN = 'MTE1MTgzMjY0MzkxMTA0NTEyMA.GWyQ_M.bRR-rG6sRzAlw8x89-YiGCMJ5w7ssYeRouxKsA'
CHANNEL_ID = '1144299845478252545'


intents = discord.Intents.all()
print( intents)
client = MyClient(intents=intents)
client.run(TOKEN)