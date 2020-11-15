from pyrogram import Client

from pyrogram import filters

import time

prefixes = [",", "+", ".", "/", "!"]

app = Client("my_account")

@app.on_message(filters.me & filters.command("info", prefixes))

def inf(app, msg):

       nome = msg.reply_to_message.from_user.first_name

       username = msg.reply_to_message.from_user.username

       id = msg.reply_to_message.from_user.id

       dc = msg.reply_to_message.from_user.dc_id

       is_bot = msg.reply_to_message.from_user.is_bot

       app.edit_message_text(msg.chat.id, msg.message_id, f"**🔎 Informazioni utente \n• 💭 Nome ➯ {nome} \n• 🆔 ID ➯ {id} \n• 💻 Username ➯ @{username} \n• 🤖 Bot ➯ {is_bot} \n• 📡 DataCenter ➯ 🌍 - {dc}")

@app.on_message(filters.me & filters.command("ban", prefixes))

def inf(app, msg):

       nome = msg.reply_to_message.from_user.first_name

       app.edit_message_text(msg.chat.id, msg.message_id, f"**{nome} SEI STATO BANNATO DA ME♦️**")

@app.on_message(filters.me & filters.command("unban", prefixes))

def inf(app, msg):

       nome = msg.reply_to_message.from_user.first_name

       app.edit_message_text(msg.chat.id, msg.message_id, f"**{nome} SEI STATO SBANNATO DA ME♦️**")  

@app.on_message(filters.me & filters.command("dev", prefixes))

def inf(app, msg):

       app.edit_message_text(msg.chat.id, msg.message_id, f"**STO SVILUPPANDO  L'UBOT E QUINDI NON ROMPETEMI ADIOSSSSSS**")

@app.on_message(filters.me & filters.command("tornato", prefixes))

def inf(app, msg):

       app.edit_message_text(msg.chat.id, msg.message_id, f"**SONO TORNATO BELLIIIIIIIII**")

@app.on_message(filters.me & filters.command("block", prefixes))

def nome(client, message):

  app.edit_message_text(message.chat.id, message.message_id, f"**BLOCCATO L'EBREO✔🌚**")

  app.block_user(message.reply_to_message.from_user.id)

@app.on_message(filters.me & filters.command("unblock", prefixes))

def nome(client, message):

  app.edit_message_text(message.chat.id, message.message_id, f"**SBLOCCATO L'EBREO✔🌚**")

  app.unblock_user(message.reply_to_message.from_user.id)

@app.on_message(filters.me & filters.command("on", prefixes))

def nome(client, message):

  app.edit_message_text(message.chat.id, message.message_id, f"**✅ONLINE**")

  app.update_profile(first_name="LX|∂αяκℓυκє🪐[online]")

@app.on_message(filters.me & filters.command("off", prefixes))

def nome(client, message):

  app.edit_message_text(message.chat.id, message.message_id, f"**✅OFFLINE**")

  app.update_profile(first_name="LX|∂αяκℓυκє🪐[offline]")

@app.on_message(filters.me & filters.command("del", prefixes))

def inf(client, message):

  app.edit_message_text(message.chat.id, message.message_id, f"**Messaggio cancellato con successo!👌**")

  message.reply_to_message.delete()

  app.delete_messages(message.chat.id, message.message_id) 

@app.on_message(filters.me & filters.command("kickme", prefixes))

def nome(app, msg):

       chat_id = msg.chat.id

       app.edit_message_text(msg.chat.id, msg.message_id, f"**Bye bye❄️**")  

       app.leave_chat(chat_id)

@app.on_message(filters.me & filters.command("lol", prefixes))

def inf(app, msg):

       app.edit_message_text(msg.chat.id, msg.message_id, "╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ \n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ \n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ \n╱┗━━━┛╰━━━╯┗━━━┛╱")

@app.on_message(filters.me & filters.command("help", prefixes))

def inf(app, msg):

       app.edit_message_text(msg.chat.id, msg.message_id, f"ECCO A TE I COMANDI DISPONIBILI!! \ninfo \nblock \nunblock \nlol \ndev \ntornato \non \noff \nkickme \ndel \nban \nunban")

@app.on_message(filters.me & filters.command("ora", prefixes))

def inf(app, msg):

       named_tuple = time.localtime() # get struct_time

       time_string = time.strftime("%H:%M:%S, del %m/%d/%Y", named_tuple)

       print(time_string) 

       app.edit_message_text(msg.chat.id, msg.message_id, f"**Sono esattamente le {time_string}**")          

       

app.run()
