import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP
from pygame.locals import K_LEFT, K_RIGHT, K_DOWN, K_UP, K_SPACE, K_RETURN
from enum import Enum

# ゲームの基本情報クラス
class Game:
    
    # ========== クラス定数 ==========
    MAP_WIDTH = 3                   # マップの横サイズ（フィールド数）
    MAP_HEIGHT = 3                  # マップの縦サイズ（フィールド数）
    MAP_COUNT = MAP_WIDTH * MAP_HEIGHT  # マップ数
    FIELD_WIDTH = 10                # 画面の横サイズ（スクエア数）
    FIELD_HEIGHT = 10               # 画面の縦サイズ（スクエア数）
    CHIP_IN_FIELD = FIELD_WIDTH * FIELD_HEIGHT  # 画面のスクエア数
    SQ_LEN = 64                     # １スクエアの幅と高さ
    SQ_SIZE = (SQ_LEN, SQ_LEN)      # １スクエアのサイズ（幅、高さ）
    
    START_FIELD = 1                 # 初期位置のマップNo
    START_PLAYER_POS_X = 5          # プレイヤーの初期位置（横）
    START_PLAYER_POS_Y = 5          # プレイヤーの初期位置（縦）

    # ========== クラス変数 ==========
    surface = None          # 表示するウィンドウ
    count = 0               # ゲームカウンタ
    is_gameover = False     # ゲームオーバーフラグ
    phase = None            # 処理段階
    keymap = []             # キー押下情報

    field = None            # フィールド
    player = None           # プレイヤー
    monsters = None         # モンスター
    battle = None           # 戦闘画面
    
    # クラスメソッド：拡大縮小付き画像読み込み
    @classmethod
    def read_image_for_square(cls, image_file_path):
        # Ａ－１最初）イメージファイルを読み込む
        image = pygame.image.load(image_file_path)
        # Ａ－２Squareへ）画面のスクエアサイズに合わせて変形させたものを返却
        return pygame.transform.scale(image, Game.SQ_SIZE)
    
    # クラスメソッド：イベントチェック処理
    @classmethod
    def check_event(cls):
        # イベント処理ループ
        for event in pygame.event.get():
            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーダウン処理
            elif event.type == KEYDOWN:
                if not event.key in Game.keymap:
                    Game.keymap.append(event.key)
            # キーアップ処理
            elif event.type == KEYUP:
                if event.key in Game.keymap:
                    Game.keymap.remove(event.key)

    # クラスメソッド：キーチェック処理
    @classmethod
    def on_upkey(cls):
        return K_UP in Game.keymap
    @classmethod
    def on_downkey(cls):
        return K_DOWN in Game.keymap
    @classmethod
    def on_leftkey(cls):
        return K_LEFT in Game.keymap
    @classmethod
    def on_rightkey(cls):
        return K_RIGHT in Game.keymap
    @classmethod
    def on_spacekey(cls):
        return K_SPACE in Game.keymap
    @classmethod
    def on_enterkey(cls):
        return K_RETURN in Game.keymap
    # クラスメソッド：キー情報クリア処理
    @classmethod
    def clear_keymap(cls):
        Game.keymap.clear

# 処理段階（列挙型クラス）
class Phase(Enum):
    TITLE = 1           # タイトル画面
    GAME_START = 2      # ゲーム開始
    
    IN_FIELD = 11       # フィールド画面
    
    BATTLE_START = 30   # バトル開始
    IN_BATTLE = 31      # バトル中
    BATTLE_FINISH = 32  # バトル終了
    
    GAME_OVER = 99      # ゲームオーバー
