import discord,asyncio
import datetime
client=discord.Client()

@client.event
async def on_ready():
    print('Logged in as: '+client.user.name)
    print('Bot ID: '+client.user.id)
    print('------')

async def channel_cleanup():
    await client.wait_until_ready()
    for server in client.servers:
        channel_list=dict( (channel.name,channel) for channel in server.channels)
    mlist=[]
    async for message in client.logs_from(channel_list['builds-ephemere']):
        tdiff=(datetime.datetime.now()-message.timestamp).days
        if tdiff>=1:
            mlist.append(message)
    if len(mlist)>0:
        await client.delete_messages(mlist)
    await asyncio.sleep(300)

client.loop.create_task(channel_cleanup())
client.run('NDE3MjE5MjExMTcwMDIxMzk2.DXR-3A.9Qla_yjvuJEqjpVBPCdpWIgc-ec')