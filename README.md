# Read json Python

Pythonでjsonをいい感じに読み込んで扱う方法を調査する。

## 実行

### dataclass <-> dict 変換のサンプル

``` sh
docker-compose run python test.py
```

### json -> dict -> dataclass 変換のサンプル

``` sh
docker-compose run python app.py
```

#### 備考

1. jsonにあってdataclassにないキーが存在する場合はエラーになる。
2. jsonになくてdataclassにあるキーが存在する場合は、
  - 最上位要素の場合はNoneで生成される。
  - 最上位要素以外は何も生成されない。

## 参考

- [Pythonのdataclassをdictやjsonと相互に変換する方法を解説！:浜介ブログ](https://1kara-hajimeru.com/2021/02/1691/)
