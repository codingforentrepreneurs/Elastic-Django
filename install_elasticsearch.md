Installing elasticsearch is easy thanks to [this guide](https://www.elastic.co/guide/en/elasticsearch/reference/7.10/install-elasticsearch.html)

__Elasticsearch Version__: _7.10.1_


## Docker

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.10.1
```

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.1

```



## macOS with HomeBrew ([ref](https://www.elastic.co/guide/en/elasticsearch/reference/7.10/brew.html))

```
brew tap elastic/tap
brew install elastic/tap/elasticsearch-full
```

```
elasticsearch -E http.port=9231 -E transport.tcp.port=9332
```