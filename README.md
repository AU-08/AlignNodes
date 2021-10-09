ezAlignNodes
==========================
選択したノードを右揃え、左揃え、中央揃え...と整理するスクリプトです。

Installation
==========================

1. Download ZIPからフォルダをダウンロードします。

2. ZIPファイルを解凍し以下の通りに配置します。pythonフォルダがない場合はフォルダごとコピペしてください。    
`C: > Users > .nuke > python > ezAlignNodes.py`  

3. init.pyに以下のコマンドを追加します。(3,4のコマンドはダウンロードしたinit.py, menu.pyからコピペして構いません)  
```py
nuke.pluginAddPath('./python')
```

4. menu.pyに以下のコマンドを追加します。  
```py
# Align Nodes
nuke.menu('Nodes').addCommand('Align Nodes / alighn on right', ezAlignNodes.alignNodesRight)

nuke.menu('Nodes').addCommand('Align Nodes / alighn on left', ezAlignNodes.alignNodesLeft)

nuke.menu('Nodes').addCommand('Align Nodes / alighn on top', ezAlignNodes.alignNodesTop)

nuke.menu('Nodes').addCommand('Align Nodes / alighn on bottom', ezAlignNodes.alignNodesBottom)

nuke.menu('Nodes').addCommand('Align Nodes / alighn on center', ezAlignNodes.alignNodesCenter)
```

5. Nukeを再起動し、ツールバーにボタンが追加されていれば完了です。


How to use
==========================

1. 整理したいノードを選択します。  

2. 揃えたい方法のボタンをクリックします。
