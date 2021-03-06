"""
hash関数は 、 「数値として同じ値」は「同じハッシュ値」を返す 。
これはhashがその計算の根拠を 、 オブジェクトとして等しいかどうかに置いているためだ 。
一方 、 idはメモリ空間のどこにそのオブジェクトがあるかを 計算の根拠にしている 。
1と1.0は整数と小数で本来別のオブジェクトなので 、 メモリ空間では別の場所に保持されている 。
このため、idの戻り値は全く異なったものとなる。
Pythonでは数値や文字列を含め、すべての値はオブジェクトです。
オブジェクトのID（識別値）を調べるにはid()関数を使用します。
変数名を引数にid()関数を実行すると参照しているオブジェクトのIDを表示します。
"""
