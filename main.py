import pygame
from game import Game, Phase
from field import Field
from player import Player
from monster import Monster
from monsterlist import MonsterList
from battle import Battle

# Pythonの基本処理
pygame.init()
Game.surface = pygame.display.set_mode([960, 640])
clock = pygame.time.Clock()
pygame.display.set_caption('*** Sample RPG ***')

# 描画用フォント（等幅フォントを使用しているので、使えなかったら変えてください）
smallfont = pygame.font.SysFont('Courier', 36)   # 小さい文字用のフォント
largefont = pygame.font.SysFont(None, 120)   # 大きい文字用のフォント

# ゲーム情報初期化処理
def init_game_info():
    # フィールド表示をスタート状態とする
    Game.phase = Phase.IN_FIELD
    # Ａ－２６Fieldから）フィールド・インスタンスを作成して、ゲームクラスの変数に設定
    Game.field = Field()
    # Ｃ－４４Playerから）プレイヤー・インスタンスを作成して、ゲームクラスの変数に設定
    Game.player = Player()
    # Ｏ－１８１MonsterListから、最後）追加したモンスターを追加する
    # Ｈ－１０３Monsterから)モンスター・インスタンスのリストを作成して、ゲームクラスの変数に設定
    
    
    
    # Ｋ－１４６Battleから）戦闘画面
    

# 基本描画処理
def basic_draw():
    # Ａ－２７最後）フィールドの描画
    Game.field.draw()
    # Ｈ－１０４)モンスター達の描画
    
    
    # Ｃ－４５最後）プレイヤーの描画
    Game.player.draw()
    # Ｄ－５１Playerから）レベルの描画（左空白埋めで５桁）
    level_str = str(Game.player.level).rjust(5)
    level_render = smallfont.render(f'Level:{level_str}',
                                    True, (255, 255, 255))
    Game.surface.blit(level_render, (680, 30))    
    # Ｄ－５２）HPの描画（左空白埋めで５桁）
    hp_str = str(Game.player.hp).rjust(5)
    hp_render = smallfont.render(f'   HP:{hp_str}',
                                True, (255, 255, 255))
    Game.surface.blit(hp_render, (680, 80)) 
    
# メイン処理
def main():
    # ゲーム情報の初期化処理を実行
    init_game_info()

    # ゲームのメインループ
    while True:
        # ゲームのカウンタを１加算
        Game.count += 1
        # イベントチェック処理（終了、キー入力）を実行
        Game.check_event()
        # 画面を黒で塗りつぶす
        Game.surface.fill((0, 0, 0))
        # ===== ゲームフェーズによる処理段階分け =====
        # フィールド上の場合
        if Game.phase == Phase.IN_FIELD:
            # Ｄ－５３最後）プレイヤーの毎回処理
            Game.player.frame_process_img()
            # Ｈ－１０５最後)モンスターの毎回処理
            
            
            # 基本描画処理
            basic_draw()

        # 戦闘中の場合
        elif Game.phase == Phase.IN_BATTLE:
            # Ｎ－１７７Battleから、最後）戦闘中の毎回処理
            
            # 基本描画処理
            basic_draw()
            # Ｋ－１４７最後）戦闘画面描画処理
            
            
        # ゲームオーバーの場合
        elif Game.phase == Phase.GAME_OVER:
            # 基本描画処理
            basic_draw()
            # ゲームオーバーメッセージの描画
            go_str = largefont.render('GAME OVER...',
                                        True, (255, 0, 0))
            Game.surface.blit(go_str, (40, 300))

        pygame.display.update()     # 描画更新処理
        clock.tick(25)              # 一定時間処理

# メイン処理の呼び出し
if __name__ == '__main__':
    main()
