# docker-handson 
サンプルDockerfileとクイズを通して、Dockerのベストプラクティスを学ぶ。

このレポジトリではいくつかの欠陥のあるDockerfileがあります。
DockerfileはシンプルなHTTPサーバーアプリケーションを実装しています。
Dockerfileを調べて修正することで、Dockerのベストプラクティスを学ぶことが目的です。

## 言語
現在は2つの言語をサポートしています: Go または Python
クイズに対しては各言語の知識が少しだけ必要になりますが、修正が必要なファイルはDockerfileのみです。

## 必要なもの 
- Docker
- コンテナ脆弱性スキャンツール (例 [Trivy](https://github.com/aquasecurity/trivy), [`docker scan`](https://docs.docker.com/engine/scan/) など)

## はじめかた 
1. このレポジトリをクローンする
```
git clone https://github.com/AvintonCode/docker-handson.git
```

2. `go-sample` または `python-sample` ディレクトリからそれぞれの`Dockerfile`を見つけてください。
各ディレクトリ内のREADMEにイメージのビルド方法とタスクが記載されています。

## ヒント

### Dockerのベストプラクティスについての記事を読む
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) by Docker
- [Image-building best practices](https://docs.docker.com/get-started/09_image_best/) by Docker
- [Docker development best practices](https://docs.docker.com/develop/dev-best-practices/) by Docker
- [Best practices for building containers](https://cloud.google.com/architecture/best-practices-for-building-containers) by Google
- [Best practices writing a Dockerfile](https://docs.bitnami.com/tutorials/best-practices-writing-a-dockerfile) by Bitnami

### 脆弱性スキャンにTrivyを使用する
[Trivy](https://github.com/aquasecurity/trivy) はオープンソースの脆弱性スキャンツールです。

スキャンの実行には、次のように`--ignore-unfixed`オプションを付けることをお勧めします。
```
trivy image --ignore-unfixed go-simple:latest
```
