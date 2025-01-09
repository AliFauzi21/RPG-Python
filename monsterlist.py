from game import Game
# モンスターリストクラス
class MonsterList:
    
    # Ｏ－１７８最初）モンスターリストの番号を追加する
    # モンスターリストの番号
    MON_NO_DOG = 0
    MON_NO_BEE = 1
    MON_NO_SKELETON = 2

    # モンスター情報取得関数各種
    @classmethod
    def get_monster_name(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][0]
    @classmethod
    def get_monster_image_list(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][1]
    @classmethod
    def get_monster_move_interval(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][2]
    @classmethod
    def get_monster_dir_interval(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][3]
    @classmethod
    def get_monster_stop_interval(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][4]
    @classmethod
    def get_monster_unmovable_chips(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][5]
    @classmethod
    def get_monster_attack_power(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][6]
    @classmethod
    def get_monster_hp(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][7]
    @classmethod
    def get_monster_battle_image_file(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][8]
    @classmethod
    def get_monster_battle_image_size(cls, monster_no):
        return MonsterList.MONSTER_LIST[monster_no][9]
    
    # =============== モンスター情報 ===============
    # 名前
    # マップ上での画像リスト
    # 移動間隔時間
    # 方向変更間隔時間
    # 停止時間
    # 移動出来ないマップデータのリスト
    # 攻撃力
    # ＨＰ
    # 戦闘時の画像ファイル
    # 戦闘時の画像サイズ
    
    # モンスター１
    MONSTER_DOG = (
        'Dog Fighter',
        (Game.read_image_for_square('image/enemy2.png'),
        Game.read_image_for_square('image/enemy2.png')),
        5,
        20,
        10,
        [3],
        1,
        25,
        'image/enemy2.png',
        (500//3, 500//3)
    )

    # モンスター２
    MONSTER_BEE = (
        'Killer Bee',
        (Game.read_image_for_square('image/enemy5.png'),
        Game.read_image_for_square('image/enemy5.png')),
        2,
        12,
        5,
        [],
        2,
        10,
        'image/enemy5.png',
        #(440, 540)
        (500//3, 500//3)
    )
    # Ｏ－１７９）上のモンスターを参考に、
    # モンスター情報を追加する
    MONSTER_Skeleton = (
        'Iron Skull',
        (Game.read_image_for_square('image_other/enemy4.png'),
        Game.read_image_for_square('image_other/enemy4.png')),
        4,
        20,
        3,
        [],
        2,
        10,
        'image_other/enemy4.png',
        (500//3, 500//3)
    )
    # モンスターリスト
    # Ｏ－１８０mainへ）追加したモンスターをモンスターリストに追加する
    MONSTER_LIST = (
        MONSTER_DOG,
        MONSTER_BEE,
        MONSTER_Skeleton
    )