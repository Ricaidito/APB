import discord
from discord.ext import commands
from utils import load_token, load_prefix, check_if_config_exists


if __name__ == "__main__" and check_if_config_exists():

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=load_prefix(), intents=intents)

    @bot.event
    async def on_ready():
        await bot.tree.sync()
        print("Bot is online")

    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")

    @bot.command()
    async def add(ctx, number1, number2):
        if number1.isdigit() and number2.isdigit():
            await ctx.send(int(number1) + int(number2))
        else:
            await ctx.send("Please provide valid numbers")

    @bot.command()
    async def hello(ctx):
        await ctx.send("Hello!")

    @bot.tree.command(name="salute", description="Salute!")
    async def salute(interaction: discord.Interaction):
        await interaction.response.send_message("Salute!")

    bot.run(load_token())

else:
    print(
        "Config file not found. Please create a config.json file with the token and prefix."
    )
