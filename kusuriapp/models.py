import datetime
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from time import time
from django.contrib.auth.base_user import BaseUserManager

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
    taking_time = models.ManyToManyField('TakingTimeAlarm', verbose_name='服用時刻', choices=TAKING_TIME)
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
SOCIENTY_LIST = (
        ('0', '日医工株式会社'),
        ('1', '沢井製薬株式会社'),
        ('2', '東和薬品株式会社'),
        ('3', '日本ジェネリック株式会社'),
        ('4', 'ファイザー株式会社'),
        ('6', 'ニプロ株式会社（528）'),
        ('7', '武田テバファーマ株式会社'),
        ('8', '株式会社陽進堂'),
        ('9', '共和薬品工業株式会社'),
        ('10', 'Meiji Seika ファルマ株式会社'),
        ('11', '高田製薬株式会社'),
        ('12', '辰巳化学株式会社'),
        ('13', '第一三共株式会社'),
        ('14', 'サンド株式会社'),
        ('15', '日本ケミファ株式会社'),
        ('16', 'キョーリンリメディオ株式会社'),
        ('17', '日新製薬株式会社'),
        ('18', '鶴原製薬株式会社'),
        ('19', '田辺三菱製薬株式会社'),
        ('20', '小林化工株式会社'),
        ('21', '共創未来ファーマ株式会社'),
        ('22', '第一三共エスファ株式会社'),
        ('23', '株式会社ツムラ'),
        ('24', '富士製薬工業株式会社'),
        ('25', '日本薬品工業株式会社'),
        ('26', 'アルフレッサファーマ株式会社'),
        ('27', '株式会社三和化学研究所'),
        ('28', '大原薬品工業株式会社'),
        ('29', '大塚製薬株式会社'),
        ('30', '丸石製薬株式会社'),
        ('31', 'エーザイ株式会社'),
        ('32', '協和キリン株式会社'),
        ('33', 'ニプロESファーマ株式会社'),
        ('34', '科研製薬株式会社'),
        ('35', '塩野義製薬株式会社'),
        ('36', 'ノバルティスファーマ株式会社'),
        ('37', '持田製薬株式会社'),
        ('38', '大日本住友製薬株式会社'),
        ('39', 'アステラス製薬株式会社'),
        ('40', '扶桑薬品工業株式会社'),
        ('41', '健栄製薬株式会社'),
        ('42', 'あすか製薬株式会社'),
        ('43', 'テルモ株式会社'),
        ('44', '吉田製薬株式会社'),
        ('45', 'グラクソ・スミスクライン株式会社'),
        ('46', 'サノフィ株式会社'),
        ('47', '日本化薬株式会社'),
        ('48', '鳥居薬品株式会社'),
        ('49', '大杉製薬株式会社'),
        ('50', 'バイエル薬品株式会社'),
        ('51', '帝國製薬株式会社'),
        ('52', '日本新薬株式会社'),
        ('53', '中外製薬株式会社'),
        ('54', 'ヤンセン ファーマ株式会社'),
        ('55', 'キッセイ薬品工業株式会社'),
        ('56', 'サンファーマ株式会社'),
        ('57', '岩城製薬株式会社'),
        ('58', 'クラシエ薬品株式会社'),
        ('59', '小太郎漢方製薬株式会社'),
        ('60', '武田薬品工業株式会社'),
        ('61', '久光製薬株式会社'),
        ('62', '参天製薬株式会社'),
        ('63', '小野薬品工業株式会社'),
        ('64', '光製薬株式会社'),
        ('65', 'ダイト株式会社'),
        ('67', '日東メディック株式会社'),
        ('68', '武田テバ薬品株式会社'),
        ('69', '全星薬品工業株式会社'),
        ('70', 'ヴィアトリス製薬株式会社'),
        ('71', '興和株式会社'),
        ('72', '富士フイルム富山化学株式会社'),
        ('73', '帝人ファーマ株式会社'),
        ('74', 'マイランEPD合同会社'),
        ('75', '大鵬薬品工業株式会社'),
        ('76', '日本イーライリリー株式会社'),
        ('77', 'MSD株式会社'),
        ('78', 'コーアイセイ株式会社'),
        ('79', '日本臓器製薬株式会社'),
        ('80', 'ノボノルディスクファーマ株式会社'),
        ('81', '株式会社日本点眼薬研究所'),
        ('82', 'LTLファーマ株式会社'),
        ('83', 'アストラゼネカ株式会社'),
        ('84', '共和クリティケア株式会社'),
        ('85', 'わかもと製薬株式会社'),
        ('86', '杏林製薬株式会社'),
        ('87', '大正製薬株式会社'),
        ('88', '株式会社フェルゼンファーマ'),
        ('89', '旭化成ファーマ株式会社'),
        ('90', '本草製薬'),
        ('91', 'あゆみ製薬株式会社'),
        ('92', 'EAファーマ株式会社'),
        ('93', '千寿製薬株式会社'),
        ('94', 'トーアエイヨー株式会社'),
        ('95', '日本ベーリンガーインゲルハイム株式会社'),
        ('96', 'CSLベーリング株式会社'),
        ('97', '一般社団法人 日本血液製剤機構'),
        ('98', 'ラクール薬品販売株式会社'),
        ('99', 'ブリストル・マイヤーズ スクイブ株式会社'),
        ('100', 'ゼリア新薬工業株式会社'),
        ('101', 'マルホ株式会社'),
        ('102', 'セオリア ファーマ株式会社'),
        ('103', '佐藤製薬株式会社'),
        ('104', '太陽ファルマ株式会社'),
        ('105', 'テイカ製薬株式会社'),
        ('106', '太虎精堂製薬株式会社'),
        ('107', '株式会社 大塚製薬工場'),
        ('108', 'オルガノン株式会社'),
        ('109', '皇漢堂製薬株式会社'),
        ('110', '三和生薬株式会社'),
        ('111', 'シオエ製薬株式会社'),
        ('112', '小堺製薬'),
        ('113', '藤永製薬株式会社'),
        ('114', '株式会社ビオメディクス'),
        ('115', 'Me ファルマ株式会社'),
        ('116', '三笠製薬株式会社'),
        ('117', '藤本製薬株式会社'),
        ('118', 'カイゲンファーマ株式会社'),
        ('119', '祐徳薬品工業株式会社'),
        ('120', '株式会社ヤクルト本社'),
        ('121', '株式会社 エッセンシャルファーマ'),
        ('122', 'シオノケミカル株式会社'),
        ('123', '中北薬品株式会社'),
        ('124', '寿製薬株式会社'),
        ('125', 'アッヴィ合同会社'),
        ('126', '堀井薬品工業株式会社'),
        ('127', 'ノーベルファーマ株式会社'),
        ('128', 'フェリング・ファーマ株式会社'),
        ('129', '松浦薬業株式会社'),
        ('130', '昭和薬品化工株式会社'),
        ('131', 'ギリアド・サイエンシズ株式会社'),
        ('132', '岡山大鵬薬品株式会社'),
        ('133', '株式会社オーファンパシフィック'),
        ('134', '株式会社 ミノファーゲン製薬'),
        ('135', 'ヴィーブヘルスケア株式会社'),
        ('136', 'メルクバイオファーマ株式会社'),
        ('137', 'JCRファーマ株式会社'),
        ('138', 'DSファーマプロモ株式会社'),
        ('139', 'レコルダティ・レア・ディジーズ・ジャパン株式会社'),
        ('140', 'コーアバイオテックベイ株式会社'),
        ('141', 'ジェイドルフ製薬株式会社'),
        ('142', '東菱薬品工業株式会社'),
        ('143', 'ジョンソン・エンド・ジョンソン株式会社'),
        ('144', 'ムンディファーマ株式会社'),
        ('145', 'アムジェン株式会社'),
        ('146', '株式会社富士薬品'),
        ('147', '日本アルコン株式会社'),
        ('148', '日本製薬株式会社'),
        ('149', '富士化学工業株式会社'),
        ('150', 'バイオジェン・ジャパン株式会社'),
        ('151', '大興製薬株式会社'),
        ('152', '協和化学工業株式会社'),
        ('153', 'ビオフェルミン製薬株式会社'),
        ('154', '長生堂製薬株式会社'),
        ('155', '化研生薬株式会社'),
        ('156', '全薬工業株式会社'),
        ('157', '原沢製薬工業'),
        ('158', 'ユーシービージャパン株式会社'),
        ('159', '日本歯科薬品株式会社'),
        ('160', 'ゾンネボード製薬株式会社'),
        ('162', '天藤製薬株式会社'),
        ('163', '田村薬品工業株式会社'),
        ('164', 'サラヤ株式会社'),
        ('165', '株式会社ビーブランド・メディコーデンタル'),
        ('166', '第一薬品産業株式会社'),
        ('167', '東亜新薬株式会社'),
        ('168', 'セルトリオン・ヘルスケア・ジャパン株式会社'),
        ('169', 'SKIファーマ株式会社'),
        ('170', 'アボットジャパン合同会社'),
        ('171', 'シンバイオ製薬株式会社'),
        ('172', '森下仁丹株式会社'),
        ('173', 'ミヤリサン製薬株式会社'),
        ('174', '株式会社伏見製薬所'),
        ('175', '生晃栄養薬品株式会社'),
        ('176', 'ニチバン'),
        ('177', '株式会社龍角散'),
        ('178', '日東薬品工業株式会社'),
        ('179', 'サンスター'),
        ('180', 'アミカス・セラピューティクス株式会社'),
        ('181', '日本セルヴィエ株式会社'),
        ('182', 'インサイト・バイオサイエンシズ・ジャパン合同会社'),
        ('183', 'インスメッド合同会社'),
        ('184', '楽天メディカル株式会社'),
        ('185', 'ニプロファーマ株式会社'),
        ('186', 'エフピー株式会社'),
        ('187', 'マイラン製薬株式会社'),
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
        choices=SOCIENTY_LIST
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
    taking_time = models.TimeField(
        verbose_name='服用時刻',
        default=None,
    )
    def __str__(self):
        return self.taking_time
