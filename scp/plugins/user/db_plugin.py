
from scp import user
from pyrogram.types import Message
import json

@user.on_message(
	user.filters.me &
	user.filters.command(
        ['sql'],
        prefixes=user.cmd_prefixes,
    ),
)
async def sql_exec(_, message: Message):
    message.__str__
    sql_raw = user.get_non_cmd(message)
    try:
        results = user.db.execute(sql_raw)
    except Exception as e:
        txt = user.html_bold('Error:\n') + user.html_mono(f"{e}")
        return await message.reply_text(txt)
    
    if not results:
        return await message.reply_text('No output.')

    txt = user.html_mono(json.dump(results, indent=4, ensure_ascii=False))
    return await message.reply_text(txt)

