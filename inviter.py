import asyncio
from pyrogram import Client


from pyrogram import enums

api_id =  
api_hash = ""
async def wel():
    async with Client("acc", api_id, api_hash) as csg:

        
        x = []
        
        try:
            async for lists in csg.get_chat_members(chat_id=input('Откуда : '), limit=80):
                x.append(lists)
        except Exception as f:
                  print(f)
        
        
        
        for invite in x:
        
            try:
                await asyncio.sleep(5)
                await csg.add_chat_members(chat_id=input(Куда : ), user_ids=invite.user.id)

            except Exception as f:
                print(invite.user.id)
                print(f)




asyncio.run(wel())
