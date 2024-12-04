from game import Game
from square import Square

# フィールドチップクラス（画面１マスのクラス）
class Chip(Square):
    # チップ（フィールドの１マス）画像のリスト
    images = None
    
    # コンストラクタ
    def __init__(self):
        # Ａ－１３Squareから）親クラスのコンストラクタを呼び出す
        super().__init__()
        # Ａ－１４）チップ番号に初期値を設定
        self.chip_no = 0
        # Ａ－１５）画像リストが空の場合（初回のみ）
        if Chip.images == None:
            # Ａ－１６）チップ（フィールドの部品）画像を読み込み
            Chip.images = (
                Game.read_image_for_square("image/chip0.png"),
                Game.read_image_for_square("image/chip1.png"),
                Game.read_image_for_square("image/chip2.png"),
                Game.read_image_for_square("image/chip3.png"),
                )
            
    # チップ番号設定
    def set_chip_no(self, no):
        # Ａ－１７）引数の番号を設定
        self.chip_no = no
        # Ａ－１８Fieldへ）番号に対応する画像を設定
        self.set_image(self.images[no])
