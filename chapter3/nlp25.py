# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import nlp20
import re

data_uk = nlp20.read_uk('text')
print(data_uk)
# for d in data_uk:
#   if "基礎情報" in d:
#     print(d)