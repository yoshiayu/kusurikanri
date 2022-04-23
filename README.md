![薬](./medicine04.webp)  

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=yoshiayu&layout=compact)](https://github-readme-stats.vercel.app/api/top-langs/?username=yoshiayu&layout=compact&theme=dracula)  ![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=yoshiayu&show_icons=true&theme=radical)  

# 薬管理アプリのポートフォリオ  
# (Of the drug management portfolio)

## ポートフォリオについて(About the portfolio)  

このリポジトリは@yoshiayuのポートフォリオを公開するためのものです。  
画像、薬データ【約28,000件】及び製造メーカー【273社】が格納されています。  
本人だけではなく、家族二人分の服用薬を管理することができ、一人5種類の服用薬の登録及び  
プッシュ通知により服用時間を通知できるアプリとなっています。  
しかしながら、まだまだ不完全な実装であり、更に改善する必要性があります。  
This repository is for publishing @ yoshiayu's portfolio.  
Images, drug data [about 28,000] and manufacturers [273 companies] are stored.  
It is possible to manage not only the person but also the medicines taken by two family members,  
and registration of 5 kinds of medicines per person and  
It is an application that can notify the dosing time by push notification.  
However, it is still an incomplete implementation and needs further improvement.  

# 実装にあたり使用した言語等  
# (Language etc. used for implementation)
* Python/Django
* HTML/CSS
* javascript
* スクレイピング(Scraping)
* webp(画像:image)
* SQLでのデータベース整理(Database organization with SQL)  

# 使用方法  
```mermaid
    graph TD;
            A[サインイン/signin]-->|メールEmail/アドレスAddress|B(ログイン/login);
            B-->C{薬管理/Top};
            C-->|服用者,薬名,服用期間,服用間隔,服用時刻,アラームスイッチ,薬メモ|D[薬の管理/managementtop];
            C-->|薬名,種別,剤型|E[登録薬/medicineregistration];
            C-->|薬の管理,家族管理,アラーム設定|F[設定/settingtop];
            F-->|服用者,薬名,服用期間,服用間隔,服用時刻,アラームスイッチ,薬メモ|G[薬の管理/medicineregistration];
            F-->|服用者3名,服用薬5種|H[家族管理/takermanegement];
            F-->|服用時間管理,  朝  昼  夕等|I[アラーム時間設定/timesetting];
            D-->C;
            E-->C;
            F-->C;
            G-->C;
            H-->C;
            I-->C;
```
# ポートフォリオ実装状態チェック
- [x] アプリケーション決定
- [x] 画面設計図
- [x] 画面遷移図
- [x] データーベース設計
- [x] ファイル生成（GitHub）
- [x] 装飾整理
- [ ] テスト起動確認
- [ ] デプロイ

# 実装者  
## Ayumu Yoshinaga  
https://twitter.com/yoshiayu1  
https://www.instagram.com/ayumuyoshi

# kusurikanriapp
