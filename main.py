import discord, os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Mark as Resolved", style=discord.ButtonStyle.green)
    async def gray_button(self, interaction, button):
        await interaction.channel.edit(auto_archive_duration=60)
        await interaction.response.defer()
        await interaction.channel.send("This post has been marked as Resolved and will be closed in one hour.\n\nIf you require further assistance on this issue, you can send another message in this post to re-open it.\n\nIf you require further support that is unrelated to this post, please start a new post and do not re-open this one.\n\nThanks for using Plex Meta Manager.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!close') and hasattr(message.channel, "parent_id") and message.channel.parent_id in [1006644783743258635, 1006477130617593906]:
        await message.channel.edit(auto_archive_duration=60)
        await message.channel.send("This post has been marked as Resolved and will be closed in one hour.\n\nIf you require further assistance on this issue, you can send another message in this post to re-open it.\n\nIf you require further support that is unrelated to this post, please start a new post and do not re-open this one.\n\nThanks for using Plex Meta Manager.")
        await message.delete()


@client.event
async def on_thread_create(thread):
    if thread.parent_id in [1006644783743258635, 1006477130617593906]:
        await thread.send("Please complete <#938455615741775902> and someone from the community or one of our <@&938443185347244033> members will respond when they're available.\n\nIncluding the meta.log from the beginning is a huge help use !logs for more information.", view=Buttons())

client.run(os.getenv('DISCORD_TOKEN'))