# B3Mモータの実験自動化ツール
B3Mモータを動かすと同時にデータ記録を行う

# pC側の設定
まずはPCとモータを接続するための設定をする必要があります。
[公式サイト](https://kondo-robot.com/faq/b3m_settings1) を見たら設定できると思います。



# 必須ライブラリ
使用するライブラリは以下の通りです。

* serial
* time
* datetime
* matplotlib

# インストール

コマンドプロンプト(黒い画面)で次のようにしてライブラリをインストールします。

```bash
pip install serial
pip install time
pip install datetime
pip install matplotlib
```
# ファイル説明
## 位置制御、角速度制御、トルク制御
以下のファイルを実行することによって様々な制御をテストすることができます。  
これらのファイルはデータの記録は行われないので注意してください。  
test_pos.py:位置制御  
test_omega.py:角速度制御  
test_tor.py:トルク制御  

## 角度のpd制御
pd_log.pyファイルにより、モータのpd制御とデータの記録を同時に行います。  
ファイルを中止した(ctr + C)直後、自動的にトルクのグラフが表示されます。  
角度、角速度、トルクのデータはlogディレクトリに自動的に記録されます。  



# 使い方

コマンドプロンプトで次のようにするだけで、プログラムを実行できます。

```bash
git clone https://github.com/oshima-yoppi/motor_experiment.git
python pd_log.py
```
## プログラムの詳細説明

さらに詳細な説明を知りたい場合は[公式サイト](https://kondo-robot.com/faq/b3m_tutorial_py1)を参考にしてください。プログラムの詳細説明が載っていると思います。

# Author


* oshima-yoppi
* kimura-lab

