---
marp: true
theme: "gaia"
header: "授業スライド"
footer: "©2024 seiya sugimoto. All rights reserved."
backgroundColor: white
headingDivider: 1
paginate: true
size: 16:9
---

# count関数
カウントだけ取って来る
```sql
SELECT count(id) FROM likes;
```

# count関数とwhere句の組み合わせ
投稿についたいいねの件数を取得するSQL
```sql
SELECT count(id) FROM likes WHERE post_id=3;
```

# limit句
投稿についたいいねの最初の10件を取得するSQL
```sql
SELECT * FROM likes WHERE post_id=3 LIMIT 10;
```

# offset句
投稿についたいいねの11件目から20件目を取得するSQL
```sql
SELECT * FROM likes WHERE post_id=3 LIMIT 20 OFFSET 10;
```

# ページネーション
* ここまでのクエリを組み合わせるとページネーションを行える
* ページ数の表示にはcount関数
  * ページネーション対象総件数 / 1ページあたりの件数
* LIMIT句 OFFSET句を利用して各ページを表示
  * LIMIT ページ数 * 1ページあたりの件数
  * OFFSET (ページ数 - 1) * 1ページあたりの件数
参考 https://getbootstrap.jp/docs/5.3/components/pagination/ 

# IN演算子
id=1, id=3, id=5のいずれかに一致する。複数の条件でまとめて取れる。
```sql
SELECT * FROM likes WHERE id IN (1, 3, 5);
```

# サブクエリ
* クエリの中にクエリが含まれている
* 副問い合わせとも呼ばれる
* より高い表現力

# EXIST演算子
* まずメインクエリ(主問い合わせ)が実行される
* メインクエリの各行に対してサブクエリが実行される
* サブクエリが値を1行以上返すとメインクエリの結果が返される

# 例
```sql
SELECT *
FROM likes
WHERE EXISTS (
    SELECT likes
    FROM posts
    WHERE posts.id = likes.post_id AND posts.user_id = 3
)
ORDER BY likes.created_at DESC
LIMIT 10;
```
