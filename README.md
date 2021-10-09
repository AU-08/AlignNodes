AlignNodes
==========================
選択したノードを整理するスクリプトです。

Installation
==========================

1. Download ZIPからフォルダをダウンロードします。

2. ZIPファイルを解凍し以下の通りに配置します。   
`C: > Users > .nuke > python > ezAlignNodes`  

3. init.pyに以下のコマンドを追加します。  
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

5. Nukeを再起動し、ツールバーにアイコンが表示されていれば完了です。


How to use
==========================

1. Depthチャンネルを含んだノードにNormalizeDepthを接続する。  

2. ROIが画像サイズと合っていなければ、"Reset"を押して調整する。 

3. "start"を押すとポップアップメニューが表示されるので、フレームレンジを設定しOKを押すとシーンの解析が始まる。

4. "gamma"で後から微調整が可能。
