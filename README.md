# Creating Q Table  
* 先手と後手両方のQテーブルを作る

先手：  
| | L | C | R |  
| --- | --- | --- | --- |  
| 1 | | | |  
| 2 | | | |  
| 3 | | | |  
| 4 | | | |  
| 5 | | | |  

後手：  
| | L | C | R |  
| --- | --- | --- | --- |  
| 1 | | | |  
| 2 | | | |  
| 3 | | | |  
| 4 | | | |  
| 5 | | | |   

-> 縦の長さはどうなるか？
左右対称を同一局面として考えると、Qテーブルの長さを減らせる。

$$ Q(x_t, a), + \max _ a Q(x_{t+1}, a) $$

# Simulate board options  

可能な盤面の組み合わせを生成する  
```bash
$ pip install -r requirements.txt
$ python3 util/simulateBoard.py
```
  
# pseudo code  

先手盤のQテーブル

ランダムに盤面を選択する
そこから期待利益が最大のものを選ぶ（イコールであればランダム）
盤面変化ー＞

後手盤のQテーブルに移動
後手盤の期待利益が最大のものを選ぶ（イコールであればランダム）
盤面変化ー＞

先手盤のQテーブルに移動


->ゲーム終了
リワードを割り引いて，遡ってQテーブルの選択肢にフィードバック

**注意** penalize or rule out impossible moves (when a column is full)

save Qtable as csv


# References  
https://colab.research.google.com/drive/1N9CuTjHRZt27sbaMHEL3x4aTgn6AVY8F?usp=sharing
