import sqlite3

# データベースに接続
# データベースに接続
conn = sqlite3.connect('C:\\Users\\harumaru870PC\\Desktop\\djangoProject\\rentalsystem\\db.sqlite3')
cursor = conn.cursor()

# 新しいレコードを挿入するためのデータのリスト
item_names = ["レリーズケーブル(Canon)",
    "レリーズケーブル(Nikon)",
    "Canon EOS Kiss X5",
    "Canon EOS Kiss X50",
    "Nikon D5100",
    "Nikon F100",
    "Nikon F",
    "可変NDフィルター(58mm)",
    "NDフィルター(ND8)",
    "Nikkor 50mm f1.8",
    "Canon 50mm f1.8",
    "Nikkor 105mm",
    "TAMRON 90mm f2.8 macro",
    "Ai-s 28mm f3.5",
    "撮影用照明",
    "ストロボ(Canon用)",
    "ストロボ(Nikon用)",
    "三脚(ベルボン)",
    "三脚(マクトレム)",
    "三脚(K&F)",
    "三脚2(K&F)",
    "レンズメンテナンス用品",
    "背景布(グリーンバック)",
    "レンズサッカー",
    "レンズオープナー",
    "Nikon 55-200mm",
    "かに目レンチ",
    "Canon 10-18mm",
    "Canon 100-300mm",
    "NDフィルター(ND8) 77mm",
    "カメラバッグ",
    "Asahi Pentax 50mm",
    "Nikkor 200-500mm f5.6",
    "ステップアップリング",
    "Micro Nikkor 200mm",
    "PLフィルター"]

# データベースにデータを挿入
for item_name in item_names:
    cursor.execute("INSERT INTO cms_item (item_name, status, category, mount) VALUES (?, 'avaliable', '', NULL)", (item_name,))
    conn.commit()

# データベース接続を閉じる
conn.close()

print("データの追加が完了しました。")
