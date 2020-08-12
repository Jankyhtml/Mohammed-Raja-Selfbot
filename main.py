import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

import discord
import time
from discord.ext import commands
from colorama import Fore, init 
import requests
import os 
import base64
import random
 
# Dont just skid it, gimme some credits, thank you - Janky 
 # Dont just skid it, gimme some credits, thank you - Janky
  # Dont just skid it, gimme some credits, thank you - Janky
   # Dont just skid it, gimme some credits, thank you - Janky
    # Dont just skid it, gimme some credits, thank you - Janky
     # Dont just skid it, gimme some credits, thank you - Janky 
      # Dont just skid it, gimme some credits, thank you - Janky
       # Dont just skid it, gimme some credits, thank you - Janky
        # Dont just skid it, gimme some credits, thank you - Janky
         # Dont just skid it, gimme some credits, thank you - Janky
          # Dont just skid it, gimme some credits, thank you - Janky
           # Dont just skid it, gimme some credits, thank you - Janky
            # Dont just skid it, gimme some credits, thank you - Janky

prefix = "."

JANKY = commands.Bot(command_prefix=prefix, self_bot=True)
JANKY.remove_command('help')

@JANKY.event
async def on_connect():
    print(f'''{Fore.RED}

 ▄▄▄██▀▀▀▄▄▄       ███▄    █  ██ ▄█▀▓██   ██▓
   ▒██  ▒████▄     ██ ▀█   █  ██▄█▒  ▒██  ██▒
   ░██  ▒██  ▀█▄  ▓██  ▀█ ██▒▓███▄░   ▒██ ██░
▓██▄██▓ ░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██ █▄   ░ ▐██▓░
 ▓███▒   ▓█   ▓██▒▒██░   ▓██░▒██▒ █▄  ░ ██▒▓░
 ▒▓▒▒░   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒   ██▒▒▒ 
 ▒ ░▒░    ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒ ▒░ ▓██ ░▒░ 
 ░ ░ ░    ░   ▒      ░   ░ ░ ░ ░░ ░  ▒ ▒ ░░  
 ░   ░        ░  ░         ░ ░  ░    ░ ░     
                                     ░ ░     
                                                                                           
                                                                                                                                     
                                                                       
            {Fore.WHITE}[+] MADE BY JANKY
              {Fore.WHITE}_________________    
                {Fore.WHITE}
                {Fore.WHITE}[-]    J
                  {Fore.WHITE}[-]   A
                    {Fore.WHITE}[-]  N
                     {Fore.WHITE}[-]  K
                       {Fore.WHITE}[-] Y
                                                                                               
                                                                               ''')
@JANKY.command()
async def help(ctx):
    embed = discord.Embed(title="𝙈𝙤𝙝𝙖𝙢𝙢𝙚𝙙 𝙍𝙖𝙟𝙖 𝙎𝙚𝙡𝙛𝙗𝙤𝙩", color= discord.Color(random.randint(0x000000, 0x000000)))
    embed.add_field(name="`Token`", value="**Grabs the niggas token.**\n", inline=False)
    embed.add_field(name="`PLookup`", value="**Gives info based off phone number.**\n", inline=False)  
    embed.add_field(name="`Cookie`", value="**Cookie grabs people on roblox.**\n", inline=False)
    embed.add_field(name="`Wizz`", value="**Wizzes any server without admin.**\n", inline=False)
    embed.add_field(name="`Scam`", value="**Grabs the niggas payment methods.**\n", inline=False)
    embed.add_field(name="`Boot`", value="**Loads up a ip booter.**\n", inline=False)
    embed.add_field(name="`Dox`", value="**Doxx anything brah.**\n", inline=False)
    embed.add_field(name='**MADE BY JANKY**', value="`JANKY MADE THIS (SKIDS K)`", inline=False)
    embed.set_footer(text=f"Logged in as : {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://media.tenor.com/images/bcf91b3dff01f14933bedf801ebaaec4/tenor.gif")
    await ctx.send(embed=embed)

@JANKY.command()
async def Token(ctx):
    await ctx.message.delete()
    await ctx.send('`Token Found...`')
    await ctx.send('**HDSIGHSGHIOSDHGIODNSIONIN2IO3NIOIO6236N73ION7IO324N7IO435NIO23NIO3N7**')

@JANKY.command()
async def Cookie(ctx):
    await ctx.message.delete()
    await ctx.send('`Cookie Found...`')
    await ctx.send('**HDSIGHSGHIOSDHGIODNSIONIN2IO3NIOIO6236N73ION7IO324N7IO435NIO23NIO3N7HDSIGHSGHIOSDHGIODNSIONIN2IO3NIOIO6236N73ION7IO324N7IO435NIO23NIO3N7HDSIGHSGHIOSDHGIODNSIONIN2IO3NIOIO6236N73ION7IO324N7IO435NIO23NIO3N7HDSIGHSGHIOSDHGIODNSIONIN2IO3NIOIO6236N73ION7IO324N7IO435NIO23NIO3N7HDSIGHSGHIOSDHGIODNSIONIN2IO3NIOIO6236N73ION7IO324N7IO435NIO23NIO3N7HDSIGHSGHIOSDHGIODNSIONIN2IO3NIOIO6236N73ION7IO324N7IO435NIO23NIO3N7HDSIGHSGHIOSDHGIODNSIONIN2IO3NIOIO6236N73ION7IO324N7IO435NIO23NIO3N7**')

@JANKY.command()
async def PLookup(ctx):
    await ctx.message.delete()
    await ctx.send('`Looking up 1800-241-LUNA...`')
    await ctx.send('**NAME** : LUNA')
    await ctx.send('**MOMS NAME** : LUNA MOM')
    await ctx.send('**DADS NAME** : LUNA DAD')
    await ctx.send('**ADRESS** : LUNA WORKSHOP 36236 ANTARTICA')
    await ctx.send('**JOB** : IDK REPAIRS SHIT')

@JANKY.command()
async def Wizz(ctx):
    await ctx.message.delete()
    await ctx.send('`Banning All...`')
    await ctx.send('`Creating Channels...`')
    await ctx.send('`Deleting Emojis...`')
    await ctx.send('`Deleting Template...`')
    await ctx.send('`Deleting Roles...`')
    await ctx.send('`Deleting Roles...`')
    await ctx.send('`Selling Server For 20$...`')
    await ctx.send('`Done...`')

@JANKY.command()
async def Scam(ctx):
    await ctx.message.delete()
    await ctx.send('`Credit Card Found...`')
    await ctx.send('**CARD BRAND** : AMERICAN EXPRESS COMPANY')
    await ctx.send('**CARD NUMBER** : 3764485069062076')
    await ctx.send('**BANK** : AGILLITAS SERVICOS DE PAGAMENTOS, S.A')
    await ctx.send('**NAME** : Nasmah Carvalho')
    await ctx.send('**ADDRESS** : Rua Dona Firmina 1639')
    await ctx.send('**COUNTRY** : BRAZIL')
    await ctx.send('**MONEY RANGE** : $625')
    await ctx.send('**CVV/CVV2** : 215')
    await ctx.send('**EXPIRY (MM/YYYY)** : 08/2026')
    await ctx.send('**CARD PIN** : 4452')

@JANKY.command()
async def Boot(ctx):
    await ctx.message.delete()
    await ctx.send('`Staring up booter...`')
    await ctx.send('**LOOK AT CONSOLE**')
    print('BOOTING IP 125.62.3624362.2')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('SENDING BOTNETS TO 125.62.3624362...')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')
    print('[OFFLINE] IP WAS SLAIN BY RAJA BOOTER')

@JANKY.command()
async def Doxx(ctx):.Scam
    await ctx.message.delete()
    await ctx.send('`Doxxing Adress...`')
    await ctx.send('`Doxxing 901 Shelby Drive...`')
    await ctx.send('**NAME** : SHELBY')
    await ctx.send('**MOMS NAME** : SHELBY MOM')
    await ctx.send('**DADS NAME** : SHELBY DAD')
    await ctx.send('**ADRESS** : 901 SHELBY DRIVE')
    await ctx.send('**JOB** : PORN STAR AND HOOKER')
    await ctx.send('**BANK** : BANK OF INDIA')
    await ctx.send('**SOCIALS** : SHELBYHASSEX123')
    await ctx.send('**PICS** : IDK')
    await ctx.send('Doxx Finished...')


JANKY.run('YOUR TOKEN HERE', bot=False)