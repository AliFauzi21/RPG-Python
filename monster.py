import random
from game import Game, Phase
from character import Character
from monsterlist import MonsterList

# モンスタークラス
class Monster(Character):

    # 移動方向リスト
    MOVE_DIR_LIST = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # コンストラクタ
    def __init__(self, pos, monster_no):
        # Ｈ－９６最初）親クラスのコンストラクタを呼び出し
        
        # Ｈ－９７）モンスター番号を設定
        
        # Ｈ－９８）モンスターの位置を設定（親クラスのメソッド）
        
        # Ｈ－９９）次移動開始時間
        
        # Ｈ－１００）移動方向
        
        # Ｈ－１０１下へ）残り移動回数
        
        
        # ===== MonsterList クラスから、モンスターの情報を取得する =====
        # モンスターの画像を作成＆設定
        mon_images = MonsterList.get_monster_image_list(monster_no)
        self.set_image_list(mon_images)
        # 名前
        self.name = MonsterList.get_monster_name(monster_no)
        # 攻撃力
        self.attack_power = MonsterList.get_monster_attack_power(monster_no)
        # ヒットポイント
        self.hp = MonsterList.get_monster_hp(monster_no)
        # 移動不能チップリスト
        self.unmovable_chips = MonsterList.get_monster_unmovable_chips(monster_no)
        # 移動インターバル
        self.move_interval = MonsterList.get_monster_move_interval(monster_no)
        # 移動方向変更タイミング
        self.direction_interval = MonsterList.get_monster_dir_interval(monster_no)
        # 移動後停止時間
        self.stop_interval = MonsterList.get_monster_stop_interval(monster_no)
        # 戦闘時の画像
        self.battle_image_file = MonsterList.get_monster_battle_image_file(monster_no)
        # 戦闘時の画像サイズ
        self.battle_image_size = MonsterList.get_monster_battle_image_size(monster_no)

    # マップ移動チェック
    # プレイヤーのマップ移動チェックと同様だが、
    # マップ外に出る場合にマップを変更しない
    def check_map_move(self, posx, posy, dx, dy):
        # 右マップへ移動してしまう（一番右＋dxが正）
        if posx == Game.FIELD_WIDTH - 1 and dx > 0:
            return False
        # 左マップへ移動（一番左より左）
        if posx < 0:
            return False
        # 下マップへ移動（一番下＋dyが正）
        if posy == Game.FIELD_HEIGHT - 1 and dy > 0:
            return False
        # 上マップへ移動（一番上より上）
        if posy < 0:
            return False
        return True
    
    # １フレームごとにする画像・処理
    def frame_process_img(self):
        # Ｉ－１０６最初）移動中でない場合
        pass
            # Ｉ－１０７）移動タイミングを超えている場合
            
                # Ｉ－１０８）移動方向をランダムに設定
                
                # Ｉ－１０９）残り移動回数を設定
                
        # Ｉ－１１０）移動中の場合
        
            # Ｉ－１１１）移動タイミングを超えている場合
            
                # --- 上下左右キーが押されている場合にキャラを移動 ---
                # Ｉ－１１２）現在位置を取得
                
                
                # Ｉ－１１３）移動方向に仮移動
                
                
                # Ｉ－１１４）加算後の値で、位置を計算
                
                # Ｉ－１１５）マップ移動チェックで移動可能な場合
                # ※Monsterクラスのマップ移動チェックは用意済み
                # Playerと同様だが、マップ移動してしまう場合は移動不可としている
                
                    # Ｉ－１１６）移動可能チェックで移動可能の場合
                    
                        # Ｉ－１１７）移動後の位置を設定する（移動不可なら位置を変更しない）
                        
                        

                # Ｉ－１１８）残り移動回数を１減算
                
                # Ｉ－１１９）移動回数が０になったら
                
                    # Ｉ－１２０）次の移動タイミングを停止時間後に設定
                    
                    # Ｉ－１２１）移動方向をなしに
                    
                # Ｉ－１２２）移動回数が０でない場合
                
                    # Ｉ－１２３最後）次の移動タイミングを設定
                    
        
        # Ｊ－１３２Fieldから）モンスターとプレイヤーの四角を取得
        
        
        # Ｊ－１３３）重なった場合
        
            # Ｊ－１３４）モンスターを画面外に
            # （画面外に設定すると、移動チェックで出てこれなくなる）
            
            
            # Ｋ－１３７最初）戦闘フェイズにする
            
            # Ｋ－１３８）戦闘処理の初期化
            
            # Ｌ－１４８最初Battleへ）戦闘クラスに、モンスター情報を設定
            
            
            # Ｋ－１３９Battleへ）戦闘画面化するので、下の処理をコメントにする
            # Ｊ－１３５）プレイヤーのHPをモンスターの攻撃力分減らす
            
            # Ｊ－１３６最後）プレイヤーのHPが０以下になったら、フェイズをゲームオーバーにする
            
            
        
        # Ｈ－１０２mainへ）キャラクターの画像設定
        
