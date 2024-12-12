from game import Game
from pygame.locals import Rect

# スクエア（画面に表示する１マス）クラス
# 同サイズで描画するものは、すべてこのクラスを継承します
class Square:
    
    # コンストラクタ
    def __init__(self):
        # Ａ－３Gameから）画像
        self.image = None
        # Ａ－４）フィールド上の位置（初期値は画面外としておく）
        self.pos = [-100, -100]
        # Ａ－５）スクエア単位の位置からのずれ
        self.dxy = [0, 0]

    # 画像を設定
    def set_image(self, image):
        # Ａ－６）画像を設定
        self.image = image

    # 位置を取得
    def get_pos(self):
        # Ａ－７）画像位置を返却
        return self.pos

    # 位置を設定
    def set_pos(self, posx, posy):
        # Ａ－８）画像位置を設定
        self.pos = [posx, posy]

    # ずれ位置を取得
    def get_dpos(self):
        # Ａ－９）画像のずれ位置を返却
        return self.dxy

    # ずれ位置を設定
    def set_dpos(self, dx, dy):
        # Ａ－１０）画像のずれ位置を設定
        self.dxy = [dx, dy]
    
    # 画面に描画
    def draw(self):
        # Ａ－１１）描画位置の座標を計算
        x = self.pos[0] * Game.SQ_LEN + self.dxy[0]
        y = self.pos[1] * Game.SQ_LEN + self.dxy[1]
        # Ａ－１２Chipへ）画面に描画
        Game.surface.blit(self.image, (x, y),
                          (0, 0, Game.SQ_LEN, Game.SQ_LEN))
    
    
    # このスクエアの位置・サイズのRectを取得
    def get_rect(self):
        # Ｊ－１２４最初）位置を設定
        x = self.pos[0] * Game.SQ_LEN + self.dxy[0]
        y = self.pos[1] * Game.SQ_LEN + self.dxy[1]
        # Ｊ－１２５Fieldへ）四角形を作成し、戻り値として返却
        return Rect(x, y, Game.SQ_LEN, Game.SQ_LEN)
