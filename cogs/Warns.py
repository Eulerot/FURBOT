import discord
from discord.ext import commands


class Warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        current_warn_count = len(await self.bot.warns.find_mane_by_custom(
            {
                "user_id": member.id
            }
        )
                                 ) + 1
        warn_filter = {"user_id": member.id, "number": current_warn_count}
        warn_data = {"reason": reason, "timestamp": ctx.message.created_at, "warned_by": ctx.author.id}

        await self.bot.warns.upsert_custom(warn_filter, warn_data)
        embed = discord.Embed(
            title="You are being warned:",
            description=f"__**Reason**__:\n{reason}",
            colour=discord.Colour.red(),
            timestamp=ctx.message.created_at
        )
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"Warn: {current_warn_count}")

        try:
            await member.send(embed=embed)
            await ctx.send("Warned that user in dm's for you.")
        except discord.HTTPException:
            await ctx.send(member.mention, embed=embed)


def setup(bot):
    bot.add_cog(Warns(bot))
