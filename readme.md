# 概要

Flask x mediapipe facemesh x ブラウザからのカメラデータの取得を行うアプリケーション。

1/6で未完成、作成しながら更新する。

1/7 現状、参考資料を元に/pictureに対してPOSTを行った。flaskでPOSTが来ているので届いているとは思うが、imageが正しく送られているかはわからない。今後確認。imageが正しく送られて居れば、setImage関数を変更するため、@app.route()で新しく画像返却用のメソッド作成を作り、ルーティング。jsの方は、then以降一度if文を通っているが、(json.statusで)setImageでエラーをおこしてcatchされている。
${}の書き方はできない？javascriptわからないので、Pythonのf'{val}'のように使うときの接頭字を知りたい。

## パッケージに関して

pythonのバージョンは3.9
pipenvを使用してプロジェクト管理.
使用ライブラリはopencv, mediapipe,flask.
フロントエンドは素のJS + html.
CSSライブラリとしてskeletonを使用するかも。
dockerの勉強にも使用するかも。
pytestも入れるかも。

## 参考資料

[][https://qiita.com/yshi12/items/9502c6232e96d7dfa29d]
[][https://nacl-ltd.github.io/2017/05/18/get_user_media.html]
[HTML5 カメラをJSで操作して写真を撮影する][https://blog.katsubemakito.net/html5/camera1]
[canvasを画像に変換しサーバへ送信][https://blog.katsubemakito.net/html5/canvas-sendserver]

