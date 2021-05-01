
class Radb:
    def __init__(self):
        self.voice_member = []
        self.battle_member = []
        self.ready_mes = None

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

    def get_battle_member(self):
        """メッセージのリアクションから対戦メンバーを取得
        """
        pass
