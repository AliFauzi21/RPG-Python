from game import Game
from character import Character

# プレイヤークラス
class Player(Character):
    # 移動不能チップの番号リスト（チップの番号と合わせること）
    UNMOVABLE_CHIP_LIST = [2, 3]
    # 初期レベル
    PLAYER_LV_1ST = 1
    # 初期ヒットポイント
    PLAYER_HP_1ST = 10
    
    # コンストラクタ
    def __init__(self):
        # Ｃ－３８Characterから）親クラスのコンストラクタを呼び出し
        super().__init__()
        # Ｃ－３９）プレイヤーの位置を設定（親クラスのメソッド）
        self.set_pos(Game.START_PLAYER_POS_X, Game.START_PLAYER_POS_Y)
        # Ｃ－４０）レベルを設定
        self.level = Player.PLAYER_LV_1ST
        # Ｃ－４１）ヒットポイントを設定
        self.hp = Player.PLAYER_HP_1ST
        # Ｃ－４２）プレイヤーの画像リストを作成
        pl_images = (Game.read_image_for_square('image/hero1.png'),
                     Game.read_image_for_square('image/hero2.png'))
        # Ｃ－４３mainへ）画像を設定（親クラスの関数）
        self.set_image_list(pl_images)
        
    # １フレームごとにする画像・処理
    def frame_process_img(self):
        # === 上下左右キーが押されている場合にキャラを移動 ===
        # Ｅ－５７Characterから）
        # 現在位置を取得（Squareクラスのメソッド）
        posx, posy = self.get_pos()
        dx, dy = self.get_dpos()

        # Ｅ－５８）それぞれのキーに合わせて、移動後のずれ位置を設定
        if Game.on_downkey():
            dy += Character.MOVE_STEP
        elif Game.on_upkey():
            dy -= Character.MOVE_STEP
        elif Game.on_leftkey():
            dx -= Character.MOVE_STEP
        elif Game.on_rightkey():
            dx += Character.MOVE_STEP
        # Ｅ－５９）ずれ位置の加算／減算後の値で、プレイヤーの位置を計算
        posx, posy, dx, dy = self.calc_chara_pos(posx, posy, dx, dy)
        
        # Ｆ－８１最後）マップ移動チェック
        posx, posy, dx, dy, is_changed = self.check_map_move(posx, posy, dx, dy)
        
        # Ｇ－９３Characterから）マップを変更していない場合
        if not is_changed:
            # Ｇ－９３）移動可能チェックで移動可能の場合
            if self.check_chara_move(posx, posy, dx, dy, Player.UNMOVABLE_CHIP_LIST):
                # Ｇ－９４）移動する（移動不可なら位置を変更しない）
                self.set_pos(posx, posy)
                self.set_dpos(dx, dy)
        # Ｇ－９５最後）マップを変更した場合は移動可能に関わらず移動
        else:
        # Ｅ－６０最後）加算後の値で、プレイヤーの位置を計算
            self.set_pos(posx, posy)
            self.set_dpos(dx, dy)
        
        # Ｄ－５０）Characterから、mainへ
        # キャラクターの画像設定
        self.set_chara_animation()

    # マップ移動チェック
    def check_map_move(self, posx, posy, dx, dy):
        # Ｆ－６９Fieldから）マップ変更フラグ
        is_changed = True
        # Ｆ－７０）右マップへ移動（一番右＋dxが正）
        if posx == Game.FIELD_WIDTH - 1 and dx > 0:
            # Ｆ－７１）マップを右へ、プレイヤー位置を左へ
            Game.field.change_field(1, 0)
            posx, dx = 0, 0
        # Ｆ－７２）左マップへ移動（一番左より左）
        elif posx < 0:
            # Ｆ－７３）マップを左へ、プレイヤー位置を右へ
            Game.field.change_field(-1, 0)
            posx, dx = Game.FIELD_WIDTH - 1, 0
        # Ｆ－７４）下マップへ移動（一番下＋dyが正）
        elif posy == Game.FIELD_HEIGHT - 1 and dy > 0:
            # Ｆ－７５）マップを下へ、プレイヤー位置を上へ
            Game.field.change_field(0, 1)
            posy, dy = 0, 0
        # Ｆ－７６）上マップへ移動（一番上より上）
        elif posy < 0:
            # Ｆ－７７）マップを上へ、プレイヤー位置を下へ
            Game.field.change_field(0, -1)
            posy, dy = Game.FIELD_HEIGHT - 1, 0
        # Ｆ－７８）どれにも当てはまらない場合
        else:
            # Ｆ－７９）マップ変更なし
            is_changed = False

        # Ｆ－８０上へ）マップ変更後（変更してない場合も）の位置と変更フラグを返却
        return posx, posy, dx, dy, is_changed
