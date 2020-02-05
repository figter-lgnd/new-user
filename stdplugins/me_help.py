""" 
Syntax: .info .help .howto
Customized by @meanii 
Please Don't remove credit name 
"""

import sys
from telethon import events, functions, __version__
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="info ?(.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    splugin_name = event.pattern_match.group(1)
    if splugin_name in borg._plugins:
        s_help_string = borg._plugins[splugin_name].__doc__
    else:
        s_help_string = "****:"
    help_string = """@kaitoxd ( **Custom Built By** @meanii ) \n**Verified Account**: ✅\n
Pithun {}
Talethrun {}
 
**Custom Built Fork**: https://github.com/mitshuhataki/kaito """.format(
        sys.version,
        __version__
    )
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER  # pylint:disable=E0602
    if tgbotusername is not None:
        results = await borg.inline_query(  # pylint:disable=E0602
            tgbotusername,
            help_string + "\n\n" + s_help_string
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        await event.reply(help_string + "\n\n" + s_help_string)
        await event.delete()


@borg.on(admin_cmd(pattern="dc"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await event.edit(f"Country : `{result.country}`\n"
                     f"Nearest Datacenter : `{result.nearest_dc}`\n"
                     f"This Datacenter : `{result.this_dc}`")


@borg.on(admin_cmd(pattern="help(.*)"))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.reply("Haye, My name is kaito 👨🏻‍💻!!\n👉🏻I'm Userbot Customized by @meanii\n👉🏻You can use following cammands.\n\n👉🏻`.ud` To urban dictionary\n👉🏻`.ddg` <Query> To Duck Duck GO 🦆\n👉🏻`.gs` <Query> To Google Search\n👉🏻`.gi` <Query> To Google Image Search\n👉🏻`.grs`(with reply image) To Google Reverse Search\n👉🏻`.qbot` To Quotly\n👉🏻`.anii` To Animation sticker to Video\n👉🏻`.download` To Downlaod file\n👉🏻`.upload` To upload file\n👉🏻`.howto`<plugin name> To know about and cmds about Plugins\n👉🏻`.help` For your help! 😉\n👉🏻 `.info` to know about more.\n\n🌚**Sudo Commands**\n👉🏻`.stat` To know how many connected current users, bots, channels & Groups. \n👉🏻`.exec` <cmd> For Bash Commands.\n👉🏻`.cpin` To pin message.\n👉🏻`.type`<Your Words> To typing as typewriter.\n👉🏻`.spam`<num> To Spam")


@borg.on(admin_cmd(pattern="howto ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)
    if plugin_name in borg._plugins:
        help_string = borg._plugins[plugin_name].__doc__
        unload_string = f"Use `.unload {plugin_name}` to remove this plugin."
        if help_string:
            plugin_syntax = f"Syntax for plugin **{plugin_name}**:\n\n{help_string}\n{unload_string}"
        else:
            plugin_syntax = f"No DOCSTRING has been setup for {plugin_name} plugin."
    else:
        plugin_syntax = "Enter valid **Plugin** name.\nDo `.stdplugins` or `.info` to get list of valid plugin names."
    await event.edit(plugin_syntax)
