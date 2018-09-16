# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
# セクション名とは問題26で参考情報として紹介されているマークアップ早見表の「見出し」を指しているもよう

import nlp20

data_uk = nlp20.read_uk('text').splitlines()
level = 1
for d in data_uk:
  midashi = '=='
  if midashi in d:
    print(level, d)
