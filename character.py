from game import Game
from square import Square

# キャラクタークラス（プレイヤーとモンスターの共通的な部分のクラス）
class Character(Square):
    
    # 画像を変える間隔
    CHANGE_IMAGE_INTERVAL = 10
    # キャラクターの移動距離
    MOVE_STEP = 16
    
    # コンストラクタ
    def __init__(self):
        # Ｃ－３２最初）親クラスのコンストラクタを呼び出し
        super().__init__()
        # Ｃ－３３）画像リスト
        self.image_list = None
        # Ｃ－３４）画像変更タイミングを算出
        self.next_img_count = Game.count + Character.CHANGE_IMAGE_INTERVAL

    # 画像リスト設定
    def set_image_list(self, image_list):
        # Ｃ－３５）画像リストを設定
        self.image_list = image_list
        # Ｃ－３６）画像番号に初期値を設定
        self.img_no = 0
        # Ｃ－３７Playerへ）画像を設定（親クラスの関数）
        self.set_image(self.image_list[self.img_no])

    # キャラクターの画像（アニメーション）設定
    def set_chara_animation(self):
        # Ｄ－４６最初）画像を変えるタイミングの場合、画像を変更
        if self.next_img_count <= Game.count:
            # Ｄ－４７）画像番号を１加算して、画像の数を超えた場合０に戻す
            #       （余りの算出で設定）
            self.img_no = (self.img_no + 1) % len(self.image_list)
            # Ｄ－４８）親クラス（Square）の画像を設定
            self.set_image(self.image_list[self.img_no])
            # Ｄ－４９Playerへ）次の画像変更タイミングを設定
            self.next_img_count = Game.count + Character.CHANGE_IMAGE_INTERVAL

    # キャラクターの位置を計算
    def calc_chara_pos(self, posx, posy, dx, dy):
        # スクエアに対する端数が１スクエア分を以上になる
        # またはマイナスになる場合に値を調整する
        # Ｅ－５４最初）横方向の位置を計算
        if dx < 0:
            posx -= 1
            dx += Game.SQ_LEN
        elif dx >= Game.SQ_LEN:
            posx += 1
            dx -= Game.SQ_LEN
        # Ｅ－５５）縦方向の位置を計算
        if dy < 0:
            posy -= 1
            dy += Game.SQ_LEN
        elif dy >= Game.SQ_LEN:
            posy += 1
            dy -= Game.SQ_LEN
        # Ｅ－５６Playerへ）計算後の値を戻り値に設定
        return posx, posy, dx, dy

    # キャラクター移動チェック
    def check_chara_move(self, posx, posy, dx, dy, unmovable_chip_list):
        # Ｇ－８７Fieldから）チェック位置リスト
        pass
        # Ｇ－８８）トチェック対象に、移動先のposx, posyを追加
        
        # Ｇ－８９）もし、上下方向にずれがある場合、ひとつ下のマスもチェック対象に追加
        
        
        # Ｇ－９０）もし、左右方向にずれがある場合、ひとつ右のマスもチェック対象に追加
        
        
        # Ｇ－９１）もし、両方にずれがある場合、右下のマスもチェック対象に追加
        
        
        # Ｇ－９２Playerへ）フィールドクラスのチェックを実施し、その結果を戻り値に設定
        
