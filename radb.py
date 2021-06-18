import random
import math

class Radb:
    def __init__(self):
        self.voice_member = []
        self.battle_member = []
        self.ready_mes = None
        self.red_team = []
        self.white_team = []

    def get_voice_member(self, ctx):
        """ボイスチャンネルに接続しているメンバーを取得
        """
        auth = ctx.author.voice
        if auth is None:
            return False
        self.voice_member = [i.name for i in auth.channel.members]
        return True

    def set_ready_mes(self, mes):
        """準備メッセージを保存
        """
        self.ready_mes = mes
    
    async def get_ready_mes(self):
        """準備メッセージを取得
        """
        tx = self.ready_mes.channel
        mes = await tx.fetch_message(self.ready_mes.id)
        return mes
    
    def save_data(self):
        """ユーザの勝敗を記録
        """
        pass

    async def get_battle_member(self, ctx):
        """メッセージのリアクションから対戦メンバーを取得
        """
        mes = await self.get_ready_mes()
        self.battle_member = []
        reactions = mes.reactions
        ct = 0
        for i in reactions:
            if i.emoji == "👍":
                ct = i.count
                await ctx.channel.send(str(ct-1)+"人が参加中")
                async for user in i.users():
                    if not user.bot:
                        self.battle_member.append(user)
        if len(self.battle_member) == 0:
            return False
        return True

    def red_and_white(self):
        """紅白に分割する
        """
        count = len(self.battle_member)
        if count == 0:
            return False
        random.shuffle(self.battle_member)
        devi = math.ceil(count/2)
        print("devi:"+str(devi))
        print("battle_member:"+str(len(self.battle_member)))
        i = 0
        for mem in self.battle_member:
            if i < devi:
                self.red_team.append(mem)
            else:
                self.white_team.append(mem)
            i += 1
        return True