import os
import random
import discord
import keep_alive
import requests

url = 'https://cataas.com/cat'
filename = 'cat.png'

r = requests.get(url)

with open(filename, 'wb') as f:
  f.write(r.content)

if os.path.exists(filename):
  img = (filename)

ur = 'https://random.imagecdn.app/512/512'
filenam = 'aranara.png'

t = requests.get(ur)

with open(filename, 'wb') as f:
  f.write(t.content)

if os.path.exists(filenam):
  img = (filenam)

bot = discord.Bot()

@bot.event
async def on_ready():
    print('Я запустился, мур мяу!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="в твою душу"))

@bot.slash_command(name='тест', description='Тестовая команда')
async def __test(ctx):
    await ctx.respond('Успешный тест!')

@bot.slash_command(name='числа', description='Простенькая игра')
async def числа(ctx, *, число):
    msgg = random.randint(1, 1000)
    await ctx.respond(число)
    await ctx.send("⬆ Ваше число")
    await ctx.send("⬇ Число котёнка")
    await ctx.send(msgg)

@bot.slash_command(name='кот', description='Показывает случайную картинку кота')
async def кот(ctx):
    url = 'https://cataas.com/cat?unique=' + str(random.randint(1, 1000000))
    filename = 'cat.png'
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
    await ctx.respond(file=discord.File(filename))

@bot.slash_command(name='картинка', description='Показывает случайную картинку')
async def мем(ctx):
    ur = 'https://random.imagecdn.app/512/512?unique=' + str(random.randint(1, 1000000))
    filenam = 'aranara.png'
    t = requests.get(ur)
    with open(filenam, 'wb') as f:
        f.write(t.content)
    await ctx.respond(file=discord.File(filenam))

@bot.slash_command(name='шар', description='Спроси что хочешь')
async def даилинет(ctx, *, вопрос):
   msg1 = random.randint(1, 2)
   if msg1 == 1:
        await ctx.respond("Да!")
   if msg1 == 2:
        await ctx.respond("Нет...")


keep_alive.keep_alive()
bot.run(os.environ["TOKEN"])