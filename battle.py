import sys
import random
import pygame
from pygame.locals import Rect
from game import Game, Phase

# 先頭シーンクラス
class Battle:
    
    WINDOW_COLOR = (0, 48, 0)               # ウィンドウの色
    FRAME_COLOR  = (255, 255, 255)          # ウィンドウの枠線の色
    FRAME_WIDTH = 5                         # ウィンドウの枠線のサイズ
    WORD_COLOR = (255, 255, 255)            # 文字の色
    SELECT_CMD_COLOR = (255, 150, 100)      # 選択中のコマンドの色
    MSG_MAX_LINE = 7                        # メッセージの行数

    # コンストラクタ
    def __init__(self):
        # メッセージ用のフォント
        self.msg_font = pygame.font.Font('C:/Windows/Fonts/meiryo.ttc', 24)
        # コマンド用のフォント
        self.cmd_font = pygame.font.Font('C:/Windows/Fonts/meiryo.ttc', 36)

        # 表示するコマンド
        self.cmd_list = []
        self.cmd_list.append('たたかう')        # たたかう…０
        self.cmd_list.append('ぼうぎょ')        # ぼうぎょ…１
        self.cmd_list.append('どうぐ')          # どうぐ……２
        self.cmd_list.append('にげる')          # にげる……３

    # 戦闘初期化処理
    def init_data(self):
        # キー保持状態
        self.last_key = None
        # 選択されているコマンド
        self.select_cmd_no = 0
        # 決定したコマンド
        self.decide_cmd_no = -1
        # 表示するメッセージ
        self.msg_list = []
        # 表示するメッセージの段階
        self.msg_step = 0
        # 表示するメッセージの次までの間隔
        self.msg_interval = 0
        # 次にメッセージを表示するタイミング
        self.next_msg_count = 0
        # 入力されているキー情報をクリア
        Game.clear_keymap()
        
    # 戦闘モンスター登録
    def set_monster(self, monster):
        # Ｌ－１４９Monsterから）インスタンス変数のモンスター情報に設定
        pass
        # Ｌ－１５０）モンスター戦闘画像の読込
        
        # Ｌ－１５１）モンスターの表示サイズに合わせて調整
        
        
        # Ｌ－１５２下へ）インスタンス変数のモンスター情報にＨＰを設定
        # その際、主人公のレベル * 2 を追加する
        # ※モンスタークラスのHPを直接減らさないように注意
        
        # Ｍ－１６７最後）敵出現情報をメッセージに追加
        
    
    # ウィンドウ描画処理
    def draw_window(self, x, y, width, height):
        # Ｋ－１４０Monsterから）塗りつぶしでウィンドウを描く
        pass
        
        # Ｋ－１４１）やや内側に、角を丸くした枠線を描く
        
        
        

    # 画面描画処理
    def draw(self):
        # Ｋ－１４２）モンスター表示用のウィンドウを描画
        pass
        # Ｋ－１４３）モンスターウィンドウの中心位置
        
        
        # Ｌ－１５３）モンスターの中心をウィンドウの中心に設定
        
        
        # Ｌ－１５４最後）モンスターの描画
        
        # Ｋ－１４４）コマンド表示用のウィンドウを描画
        
        # Ｋ－１４５mainへ）メッセージ表示用のウィンドウを描画
        
        # Ｍ－１５５最初）メッセージとコマンドの描画
        

    # メッセージ追加処理
    def add_msg(self, msg):
        # Ｍ－１５６）メッセージを追加
        pass
        # Ｍ－１５７）メッセージ数が上限を超えたら、先頭を削除
        
        

    # メッセージとコマンドの描画処理
    def draw_msg_and_command(self):
        # Ｍ－１５８）メッセージの数だけ繰り返し
        pass
            # Ｍ－１５９）メッセージの設定
            
            # Ｍ－１６０）メッセージの描画
            
            
        # Ｍ－１６１）コマンドの数だけ繰り返し
        
            # Ｍ－１６２）選択されているコマンドの場合み色を変える
            
                # Ｍ－１６３）色を選択色に
                
            # Ｍ－１６４）選択されてなければ
            
                # Ｍ－１６５）通常色に
                
            # Ｍ－１６６上へ）コマンドの描画
            

    # コマンド移動、チェック処理
    def cmd_check(self):
        # Ｎ－１６８最初）スペースキーかエンターキーが押された場合
        pass
            # Ｎ－１６９）コマンドを決定する
            
            
            
            # Ｎ－１７０）以降の処理は行わず、関数を終了する
            

        # Ｎ－１７１）それぞれのキーに合わせて、選択コマンドを設定
        # ただし、押したキーを離さないと次のコマンドに行かない
        
        
        
        
        
        
        
        
        
        

        # Ｎ－１７２）コマンド数で割ったあまりにすることで、上下ループできる
        

    # １フレームごとにする戦闘処理
    def frame_process_btl(self):
        # Ｎ－１７３）コマンドが選択されてない場合
        pass
            # Ｎ－１７４）コマンド移動、チェック処理のみ実施
            
            
        
        # Ｎ－１７５）メッセージを表示するタイミングが来た場合
        # （戦闘処理の内部で、タイミングを設定）
        
            # Ｎ－１７６mainへ）戦闘処理を実施
            # ※戦闘処理自体は、今回は実装済みです
            

    # 戦闘処理
    # 選択されたコマンドによって処理を行う
    # 本関数は最初から用意しておきます
    def battle_process(self):
        
        # 最初の処理はコマンドによって異なる
        if self.msg_step == 0:
            # 「たたかう」の場合
            if self.decide_cmd_no == 0:
                # ダメージをランダム（レベル＋０～３の２回分）で決める
                lv = Game.player.level
                dmg = random.randint(lv, lv+3)
                dmg += random.randint(lv, lv+3)
                # メッセージの追加
                self.add_msg('あなたのこうげき！')
                self.add_msg(f'{dmg}点のダメージを与えた！')
                # 敵のHPを減らす
                self.btl_monster_hp -= dmg
                # 敵を倒したら勝利へ（関数を終了）
                if self.btl_monster_hp <= 0:
                    self.msg_step = 2
                    return
            # 「ぼうぎょ」の場合（特に実装していないため、効果はありません）
            elif self.decide_cmd_no == 1:
                self.add_msg('あなたは身構えている…')
            # 「どうぐ」の場合（特に実装していないため、効果はありません）
            elif self.decide_cmd_no == 2:
                self.add_msg('あなたはどうぐを使おうとした！')
                self.add_msg('しかし、何も持っていなかった！')
            # 「にげる」の場合（特に実装していないため、効果はありません）
            elif self.decide_cmd_no == 3:
                self.add_msg('あなたは逃げ出した！')
                self.add_msg('しかし、モンスターに阻まれた！')
            
            self.msg_step = 1
            self.next_msg_count = Game.count + 30

        # 敵の攻撃
        elif self.msg_step == 1:
            # ダメージをモンスターの攻撃力
            # ＋（０～自分のレベル＋１）とする
            dmg = self.monster.attack_power
            dmg += random.randint(0, Game.player.level + 1)
            # メッセージの追加
            self.add_msg(f'{self.monster.name}のこうげき！')
            self.add_msg(f'{dmg}のダメージを受けた！')
            # プレイヤーのHPを減らす
            Game.player.hp -= dmg
            # HPが０以下になったら敗北
            if Game.player.hp <= 0:
                self.add_msg(f'あなたはやられてしまった……')
                self.next_msg_count = Game.count + 15
                self.msg_step = 3
            else:
                # 再びコマンド待ちへ
                self.decide_cmd_no = -1

        # 戦闘に勝利
        elif self.msg_step == 2:
            # メッセージの追加
            self.add_msg(f'{self.monster.name}を倒した！')
            self.add_msg(f'あなたはレベルがあがった！')
            
            # 戦闘していたモンスターを画面外に
            self.monster.set_pos(-1, -1)
            self.monster.set_dpos(0, 0)
            
            # ※経験値を用意していないので、１戦闘でレベルが上がります
            # ※最大HPを用意していないので、１戦闘で全快します
            # レベルとHPを設定
            Game.player.hp = Game.player.PLAYER_HP_1ST + Game.player.level * 3
            Game.player.level += 1
            # 戦闘終了にする
            self.msg_step = 4
            self.next_msg_count = Game.count + 15
            
        # 戦闘に敗北
        elif self.msg_step == 3:
            # スペースキーかエンターキーが押されたらゲームオーバーへ
            if Game.on_enterkey() or Game.on_spacekey():
                Game.phase = Phase.GAME_OVER
            
        # 戦闘終了
        elif self.msg_step == 4:
            # スペースキーかエンターキーが押されたらフィールドに戻る
            if Game.on_enterkey() or Game.on_spacekey():
                Game.phase = Phase.IN_FIELD
