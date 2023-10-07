# # インストールした discord.py を読み込む
# import discord

# # 自分のBotのアクセストークンに置き換えてください
# TOKEN = 'MTAzNDAxMDY0MTMyNjkzMTk4OA.GmfOh5.NbHYoERmGF9SjO1WN7PuRoLa5I-PywbtR5aXdc'

# # 接続に必要なオブジェクトを生成
# client = discord.Client()

# # 起動時に動作する処理
# @client.event
# async def on_ready():
#     # 起動したらターミナルにログイン通知が表示される
#     print('ログインしました')

# # メッセージ受信時に動作する処理
# @client.event
# async def on_message(message):
#     # メッセージ送信者がBotだった場合は無視する
#     if message.author.bot:
#         return
#     # 「/neko」と発言したら「にゃーん」が返る処理
#     if message.content == '/neko':
#         await message.channel.send('にゃーん')

# # Botの起動とDiscordサーバーへの接続
# client.run(TOKEN)


import discord

intents =discord.Intents.default()
intents.typing=False
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

# Botの起動とDiscordサーバーへの接続
CHANNEL_ID = "1028275292436959325"
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')

@client.event
async def on_ready():
    await greet() 

client.run("トークンをここに入力")
