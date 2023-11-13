# 仮配属ゼミ(5年11月16日)

> バール・シュテファン (Stefan Baar)

## トマト - 検出 - 追跡

このノートブックでは、yoloV8 を使用して個々のトマトを検出および追跡する簡単な手順を説明します。
インスタンスの分割には、「YOLOv8x-seg」に基づく事前トレーニング済みモデルが使用されます。 モデルは少数の画像のみでトレーニングされています。 ただし、トレーニングおよび検証のデータセットは、幾何学的拡張によって拡張されています。
ノートブックを実行するには次のモジュールが必要です。


Task:
- 全てのフレームを通して、3つのトマトを追跡します。
- no False Positives/Negatives (0FN / 0FP)

<video src='https://youtu.be/SfG3to6wOK0' width=180/><video />

[![tomato tracking](https://youtu.be/SfG3to6wOK0/0.jpg)](https://youtu.be/SfG3to6wOK0 "tomato tracking")

## さらに詳しい情報

Yolo V8 について：
- https://github.com/ultralytics/ultralytics

Instance segementation について：

- https://docs.ultralytics.com/tasks/segment/

Object tracking:

- https://docs.ultralytics.com/modes/track/#why-choose-ultralytics-yolo-for-object-tracking

- Bot-SORT: https://github.com/NirAharon/BoT-SORT

- ByteTrack: https://github.com/ifzhang/ByteTrack

model training について：

- https://docs.ultralytics.com/modes/train/#why-choose-ultralytics-yolo-for-training
