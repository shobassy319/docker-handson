# Go simple HTTP server 

Dockerfileを確認してベストプラクティスを適用してください。  
DockerとGoを使用するのが初めての方は[こちらのチュートリアル](https://docs.docker.com/language/golang/build-images/)を確認することをお勧めします。

Read this page in other language: [_English_](https://github.com/AvintonCode/docker-handson/blob/main/go-sample/README.md), [_日本語_](https://github.com/AvintonCode/docker-handson/blob/main/go-sample/README-ja.md)

## コンテナのビルドと実行
1. コンテナイメージのビルド
```
docker build -t go-simple:v01 . 
```

2. コンテナの実行 
```
docker run --rm --name go-simple-app -p 8080:8080 -d go-simple:v01
```

- `--rm`: コンテナ停止時にコンテナを削除
- `--name`: コンテナに名前を付与
- `-p`: ホストOSのポート8080にバインディング
- `-d`: デタッチモードで実行(バックグラウンドで実行)

3. アプリケーションの稼働を確認: `/` と `/ping`のエンドポイントへリクエスト
```
curl -X GET http://localhost:8080/
curl -X GET http://localhost:8080/ping
```

4. コンテナの停止
```
docker stop go-simple-app
```

## 課題

### 1. イメージのサイズを小さくする
イメージのサイズは1GBを超えています。  
30MB程度まで削減してください。

### 2. コンテナプロセスにrootユーザー以外を使用する
root以外のユーザーでコンテナプロセスが開始されるように修正してください。

### 3. コンテナの脆弱性を解消する
コンテナに脆弱性のあるパッケージが含まれています。  
脆弱性を可能な限り減らしてください。

> 注: 修正がまだ利用可能ではない脆弱性は無視できます。

### 4. ビルド時間の改善
`server.go`を編集し、再度`docker build`を行うと`go mod download`も再度実行されます。   
`go mod download`は`go.mod`の変更時のみ実行されれば十分です。  
Dockerfileを修正してビルド時間を改善してください。