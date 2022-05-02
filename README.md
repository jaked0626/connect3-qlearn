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
