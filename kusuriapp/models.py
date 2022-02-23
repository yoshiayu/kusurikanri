import datetime
from tabnanny import verbose
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from time import time
from django.contrib.auth.base_user import BaseUserManager
from kusuriapp.models import Kusuri_Data

class Question(models.Model):
    pass
class Kusuri_Data(models.Model):
    pass


def get_upload_file_name(filename):
    return  "uploaded_files/%s_%s" % (str(time()).replace(".", "_"), filename)

class UserModel(BaseUserManager):
    
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
  
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')  
        
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin) :
   
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True) 
    
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=('Designates whether this user should be treated as active.' 'Unselect this instead of deleting accounts.'),
    )
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    
    objects = UserModel()
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
  
    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
  
    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name
  
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
    user_id = models.IntegerField(
        verbose_name='ユーザーID',
        blank=True,
        null=True,
        default=0,
    )
    login_id = models.IntegerField(
        verbose_name='ログイン',
        blank=True,
        null=True,
        default=0,
    )
    create_data = models.DateField(auto_now_add=True)
    update_data = models.DateField(auto_now=True)
    delete_data = models.DateField(default=None, null=True, blank=True)
class MedicineNameManagement(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    name = models.CharField(
        verbose_name='服用者',
        blank=True,
        null=True,
        max_length=50,
        default='',
    )
    def __str__(self):
        return self.name

TAKING_UNIT = (
        ('0', '錠'),
        ('1', '包'),
        ('2', '滴'),
        ('3', 'mg'),
        ('4', 'ml'),
    )
TAKING_TIME = (
        ('0', '朝'),
        ('1', '昼'),
        ('2', '夕'),
        ('3', '寝る前'),
        ('4', '朝食前'),
        ('5', '昼食前'),
        ('6', '夕食前'),
        ('7', '朝食後'),
        ('8', '昼食後'),
        ('9', '夕食後'),
        ('10', '食間（朝昼）'),
        ('11', '食間（昼夕）'),
    )
class MedicineMangement(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    name = models.ForeignKey(MedicineNameManagement, on_delete=models.CASCADE, verbose_name='服用者')
    medicine = models.ForeignKey('MedicineRegister', on_delete=models.CASCADE, default=None, verbose_name='服用薬') 
    taking_dossage = models.IntegerField(verbose_name='服用量',
        blank=True,
        null=True,
        default=0,
    )
    taking_unit = models.IntegerField(verbose_name='服用単位',
        blank=True,
        null=True,
        default=0,
        choices=TAKING_UNIT
    )
    taking_time = models.ManyToManyField('TakingTimeAlarm', verbose_name='服用時刻')
    taking_start = models.DateTimeField(
        verbose_name='服用開始',
        blank=True,
        null=True,
        default=datetime.datetime.now()
    )
    def __str__(self):
        return self.taking_start
    
    taking_end = models.DateTimeField(
        verbose_name='服用終了',
        blank=True,
        null=True,
        default=datetime.datetime.now()
    )
    def __str__(self):
        return self.taking_end
    
    text = models.TextField(
        verbose_name='薬メモ',
        blank=True,
        null=True,
        max_length=1000,
    )
KINDS_LIST = (
        ('0', '処方'),
        ('1', '処方（ジェネリック）'),
        ('2', '処方（漢方）'),
        ('3', '市販薬'),
        ('4', '市販薬（子供用）'),
        ('5', 'セルフメディケーション税剤対象'),
    )
DOSAGE_FORM = (
        ('0', '散剤'),
        ('1', '錠剤'),
        ('2', 'カプセル'),
        ('3', '液剤'),
        ('4', '外用薬'),
        ('5', '注射剤'),
        ('6', '自己注射剤'),
        ('7', 'その他'),
    )
COMPANY_LIST = (
        ('0', '株式会社浅田飴'),
        ('1', '旭化成ファーマ株式会社'),
        ('2', 'アサヒグループ食品株式会社'),
        ('3', 'アサヒフードアンドヘルスケア株式会社'),
        ('4', 'あすか製薬株式会社'),
        ('6', 'アステラス製薬株式会社'),
        ('7', 'アストラゼネカ株式会社'),
        ('8', '阿蘇製薬株式会社'),
        ('9', 'アッヴィ合同会社'),
        ('10', 'アミカス・セラピューティクス株式会社'),
        ('11', 'あゆみ製薬株式会社'),
        ('12', 'アラクス株式会社'),
        ('13', 'アルフレッサファーマ株式会社'),
        ('14', 'アース製薬株式会社'),
        ('15', '株式会社池田模範堂'),
        ('16', 'イスクラ産業株式会社'),
        ('17', '伊丹製薬'),
        ('18', 'イチジク製薬株式会社'),
        ('19', '井藤漢方製薬株式会社'),
        ('20', '岩城製薬株式会社'),
        ('21', 'EAファーマ株式会社'),
        ('22', 'うすき製薬株式会社'),
        ('23', '宇津救命丸株式会社'),
        ('24', 'エスエス製薬株式会社'),
        ('25', '株式会社 エッセンシャルファーマ'),
        ('26', 'エフピー株式会社'),
        ('27', 'Me ファルマ株式会社'),
        ('28', 'MSD株式会社'),
        ('29', 'エムジーファーマ株式会社'),
        ('30', 'LTLファーマ株式会社'),
        ('31', 'エーザイ株式会社'),
        ('32', '株式会社大石膏盛堂'),
        ('33', '大木製薬株式会社'),
        ('34', '大杉製薬株式会社'),
        ('35', '株式会社太田胃散'),
        ('36', '大塚製薬株式会社'),
        ('37', '株式会社 大塚製薬工場'),
        ('38', '大原薬品工業株式会社'),
        ('39', '岡山大鵬薬品株式会社'),
        ('40', '奥田製薬株式会社'),
        ('41', '株式会社奥田又右衛門膏本舗'),
        ('42', '樋屋製薬株式会社'),
        ('43', '小野薬品工業株式会社'),
        ('44', '株式会社オーファンパシフィック'),
        ('45', '株式会社オーヤラックス'),
        ('46', 'ヴィーブヘルスケア株式会社'),
        ('47', 'カイゲンファーマ株式会社'),
        ('48', '化研生薬株式会社'),
        ('49', '科研製薬株式会社'),
        ('50', '兼一薬品工業株式会社'),
        ('51', '株式会社キタニ'),
        ('52', '北日本製薬株式会社'),
        ('53', 'キッセイ薬品工業株式会社'),
        ('54', '救心製薬株式会社'),
        ('55', '共創未来ファーマ株式会社'),
        ('56', '杏林製薬株式会社'),
        ('57', '協和化学工業株式会社'),
        ('58', '共和クリティケア株式会社'),
        ('59', '共和薬品工業株式会社'),
        ('60', '協和薬品工業株式会社'),
        ('61', 'キョーリンリメディオ株式会社'),
        ('62', '株式会社金冠堂'),
        ('63', '金陽製薬'),
        ('64', 'ギリアド・サイエンシズ株式会社'),
        ('65', 'クラシエ薬品株式会社'),
        ('67', 'グラクソ・スミスクライン株式会社'),
        ('68', 'グラクソ・スミスクライン・CHJ'),
        ('69', '啓芳堂製薬株式会社'),
        ('70', '株式会社恵命堂'),
        ('71', '健栄製薬株式会社'),
        ('72', '皇漢堂製薬株式会社'),
        ('73', '興和株式会社'),
        ('74', '小太郎漢方製薬株式会社'),
        ('75', '株式会社近江兄弟社'),
        ('76', '小林化工株式会社'),
        ('77', '小林製薬株式会社'),
        ('78', '小林薬品工業株式会社'),
        ('79', 'コーアイセイ株式会社'),
        ('80', 'コーアバイオテックベイ株式会社'),
        ('81', '株式会社阪本漢法製薬'),
        ('82', '千金丹ケアーズ株式会'),
        ('83', '佐藤製薬株式会社'),
        ('84', 'サノフィ株式会社'),
        ('85', 'サラヤ株式会社'),
        ('86', '沢井製薬株式会社'),
        ('87', '株式会社三九製薬'),
        ('88', 'サンスター'),
        ('89', '参天製薬株式会社'),
        ('90', 'サンド株式会社'),
        ('91', 'サンファーマ株式会社'),
        ('92', '三宝製薬株式会社'),
        ('93', '株式会社三和化学研究所'),
        ('94', '三和生薬株式会社'),
        ('95', '剤盛堂薬品株式会社'),
        ('96', 'シオエ製薬株式会社'),
        ('97', '塩野義製薬株式会社'),
        ('98', 'シオノギヘルスケア'),
        ('99', 'シオノケミカル株式会社'),
        ('100', '滋賀県製薬株式会社'),
        ('101', '資生堂薬品株式会社'),
        ('102', '昭和薬品化工株式会社'),
        ('103', '新新薬品工業株式会社'),
        ('104', '神農製薬株式会社'),
        ('105', 'CSLベーリング株式会社'),
        ('106', 'JCRファーマ株式会社'),
        ('107', 'ジェイドルフ製薬株式会社'),
        ('108', 'ジェーピーエス製薬株式会社'),
        ('109', 'ジャパンメディック株式会社'),
        ('110', 'ジョンソン・エンド・ジョンソン株式会社'),
        ('111', '翠松堂製薬'),
        ('112', 'スノーデン株式会社'),
        ('113', '生晃栄養薬品株式会社'),
        ('114', 'セオリア ファーマ株式会社'),
        ('115', 'セルトリオン・ヘルスケア・ジャパン株式会社'),
        ('116', '千寿製薬株式会社'),
        ('117', 'ゼネル薬品工業株式会社'),
        ('118', 'ゼリア新薬工業株式会社'),
        ('119', '全星薬品工業株式会社'),
        ('120', '全薬工業株式会社'),
        ('121', 'ゾンネボード製薬株式会社'),
        ('122', '大幸薬品株式会社'),
        ('123', '大正製薬株式会社'),
        ('124', 'タイヘイ薬品株式会社'),
        ('125', '大鵬薬品工業株式会社'),
        ('126', '太陽ファルマ株式会社'),
        ('127', '大和製薬株式会社'),
        ('128', '高田製薬株式会社'),
        ('129', '株式会社タカミツ'),
        ('130', '武田コンシューマーヘルスケア'),
        ('131', '武田テバファーマ株式会社'),
        ('132', '武田テバ薬品株式会社'),
        ('133', '武田薬品工業株式会社'),
        ('134', '辰巳化学株式会社'),
        ('135', '株式会社建林松鶴堂'),
        ('136', '田辺三菱製薬株式会社'),
        ('137', '玉川衛材株式会社'),
        ('138', '株式会社田村治照堂'),
        ('139', '田村薬品工業株式会社'),
        ('140', '丹平製薬株式会社'),
        ('141', '第一三共株式会社'),
        ('142', '第一三共エスファ株式会社'),
        ('143', '第一三共ヘルスケア株式会社'),
        ('144', '第一薬品産業株式会社'),
        ('145', '大興製薬株式会社'),
        ('146', '大東製薬工業株式会社'),
        ('147', 'ダイト株式会社'),
        ('148', '大日本住友製薬株式会社'),
        ('149', 'ダイヤ製薬株式会社'),
        ('150', '株式会社大和生物研究所'),
        ('151', 'ダンヘルスケア株式会社'),
        ('152', '中外製薬株式会社'),
        ('153', '長生堂製薬株式会社'),
        ('154', '株式会社ツムラ'),
        ('155', '鶴原製薬株式会社'),
        ('156', 'テイカ製薬株式会社'),
        ('157', '帝國製薬株式会社'),
        ('158', 'テイコクファルマケア株式会社'),
        ('159', '帝人ファーマ株式会社'),
        ('160', 'テルモ株式会社'),
        ('162', '東亜新薬株式会社'),
        ('163', '株式会社東京甲子社'),
        ('164', '東光クリエート株式会社'),
        ('165', '東菱薬品工業株式会社'),
        ('166', '東和薬品株式会社'),
        ('167', '常盤薬品工業株式会社'),
        ('168', '株式会社トクホン'),
        ('169', '富山めぐみ製薬'),
        ('170', '鳥居薬品株式会社'),
        ('171', 'トーアエイヨー株式会社'),
        ('172', '内外薬品株式会社'),
        ('173', '中北薬品株式会社'),
        ('174', '長野県製薬株式会社'),
        ('175', '日医工株式会社'),
        ('176', 'ニチバン'),
        ('177', '日新製薬株式会社'),
        ('178', '日新薬品工業'),
        ('179', '日水製薬医薬品販売株式会社'),
        ('180', '日東メディック株式会社'),
        ('181', '日東薬品工業株式会社'),
        ('182', '日邦薬品工業株式会社'),
        ('183', '一般社団法人 日本血液製剤機構'),
        ('184', 'ニプロ株式会社'),
        ('185', 'ニプロESファーマ株式会社'),
        ('186', 'ニプロファーマ株式会社'),
        ('187', '日本アルコン株式会社'),
        ('188', '日本イーライリリー株式会社'),
        ('189', '日本化薬株式会社'),
        ('190', '日本ケミファ株式会社'),
        ('191', '日本歯科薬品株式会社'),
        ('192', '日本新薬株式会社'),
        ('193', '日本ジェネリック株式会社'),
        ('194', '日本製薬株式会社'),
        ('195', '日本臓器製薬株式会社'),
        ('196', '株式会社日本点眼薬研究所'),
        ('197', '日本ベーリンガーインゲルハイム株式会社'),
        ('198', '日本薬品工業株式会社'),
        ('199', '株式会社ヤクルト本社'),
        ('200', 'ノバルティスファーマ株式会社'),
        ('201', 'ノボノルディスクファーマ株式会社'),
        ('202', 'ノーベルファーマ株式会社'),
        ('203', '原沢製薬工業'),
        ('204', 'バイエル薬品+G4:G27株式会社'),
        ('205', 'バイオジェン・ジャパン株式会社'),
        ('206', '光製薬株式会社'),
        ('207', '久光製薬株式会社'),
        ('208', '七ふく製薬'),
        ('209', '日野製薬株式会社'),
        ('210', 'ビオフェルミン製薬株式会社'),
        ('211', '株式会社ビオメディクス'),
        ('212', '備前化成'),
        ('213', '株式会社ビーブランド・メディコーデンタル'),
        ('214', 'ファイザー株式会社'),
        ('215', 'フェリング・ファーマ株式会社'),
        ('216', '株式会社フェルゼンファーマ'),
        ('217', '株式会社伏見製薬所'),
        ('218', '富士化学工業株式会社'),
        ('219', '富士製薬工業株式会社'),
        ('220', '藤永製薬株式会社'),
        ('221', '藤本製薬株式会社'),
        ('222', '株式会社富士薬品'),
        ('223', '扶桑薬品工業株式会社'),
        ('224', 'ブリストル・マイヤーズ スクイブ株式会社'),
        ('225', '報国製薬株式会社'),
        ('226', '堀井薬品工業株式会社'),
        ('227', '本草製薬'),
        ('228', 'マイランEPD合同会社'),
        ('229', 'マイラン製薬株式会社'),
        ('230', '松浦漢方株式会社'),
        ('231', '松浦薬業株式会社'),
        ('232', '松田薬品工業株式会社'),
        ('233', '松本製薬工業株式会社'),
        ('234', '摩耶堂製薬株式会社'),
        ('235', '丸石製薬株式会社'),
        ('236', 'マルホ株式会社'),
        ('237', '三笠製薬株式会社'),
        ('238', '株式会社ミズホメディー'),
        ('239', '株式会社 ミノファーゲン製薬'),
        ('240', 'ミヤリサン製薬株式会社'),
        ('241', 'ムネ製薬株式会社'),
        ('242', 'ムンディファーマ株式会社'),
        ('243', '株式会社メイクトモロー'),
        ('244', '株式会社明治'),
        ('245', 'Meiji Seika ファルマ株式会社'),
        ('246', '明治薬品'),
        ('247', '持田製薬株式会社'),
        ('248', '森下仁丹株式会社'),
        ('249', '八ツ目製薬株式会社'),
        ('250', '株式会社山崎帝国堂'),
        ('251', '山本漢方製薬'),
        ('252', 'ヤンセン ファーマ株式会社'),
        ('253', '祐徳薬品工業株式会社'),
        ('254', 'ユニテックメディカル'),
        ('255', 'ユーシービージャパン株式会社'),
        ('256', 'ユースキン製薬株式会社'),
        ('257', '株式会社陽進堂'),
        ('258', '養命酒製造株式会社'),
        ('259', '横山製薬株式会社'),
        ('260', '吉田製薬株式会社'),
        ('261', '米田薬品株式会社'),
        ('262', 'ライオン株式会社'),
        ('263', '株式会社龍角散'),
        ('264', 'レキットベンキーザー・ジャパン株式会社'),
        ('265', 'ロート製薬株式会社'),
        ('266', 'わかもと製薬株式会社'),
        ('267', '株式会社和漢薬研究所'),
        ('268', '湧永製薬株式会社'),
        ('269', 'ワダカルシウム製薬株式会社'),
    )    
class MedicineRegister(models.Model) :
    name = models.ForeignKey(MedicineNameManagement, on_delete=models.CASCADE, verbose_name='服用者')
    medicine = models.CharField(
        verbose_name='服用薬',
        blank=True,
        null=True,
        max_length=50,
        default='',
    )
   
    kinds = models.CharField(
        verbose_name='種別',
        blank=True,
        null=True,
        max_length=50,
        default='',
        choices=KINDS_LIST
    )
    def __str__(self):
        return self.kinds
    
    dosage_form = models.CharField(
        verbose_name='剤型',
        blank=True,
        null=True,
        max_length=50,
        default='',
        choices=DOSAGE_FORM
    )
    def __str__(self):
        return self.dosage_form
   
    socienty = models.CharField(
        verbose_name='メーカー',
        blank=True,
        null=True,
        max_length=50,
        default='',
        choices=COMPANY_LIST
    )
    def __str__(self):
        return self.socienty

class TakingDosage(models.Model) :
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    name = models.ForeignKey(MedicineNameManagement, on_delete=models.CASCADE, verbose_name='服用者')
    medicine = models.ForeignKey(MedicineMangement, on_delete=models.CASCADE, verbose_name='服用薬')  
    taking_dosage = models.IntegerField(
        verbose_name='服用量',
        blank=True,
        null=True,
        default=0,
    )
    taking_unit = models.IntegerField(
        verbose_name='服用単位',
        blank=True,
        null=True,
        default=0,
    )
    taking_number = models.IntegerField(
        verbose_name='服用回数',
        blank=True,
        null=True,
        default=0,
    )
class TakingTimeAlarm(models.Model) :
    taking_time = models.TimeField(default=None, verbose_name='服用時刻')
    def __str__(self):
        return str(self.taking_time)

class CompanyMedicineName(models.Model) :
    company_id = models.IntegerField(verbose_name='会社ID', blank=True, null=True)
    company_name = models.CharField(max_length=20, verbose_name='会社名', blank=True, null=True)
    medicine_id = models.IntegerField(verbose_name='薬ID', blank=True, null=True)
    medicine_name = models.CharField(max_length=30, verbose_name='薬名', blank=True, null=True)
    initials = models.CharField(max_length=1, verbose_name='頭文字', blank=True, null=True)   
    class Meta:
        db_table = 'link'
        verbose_name_plural = '薬及び会社リスト'
