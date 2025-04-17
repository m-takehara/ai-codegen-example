以下の [Input](#input) と [Output](#output) に示す仕様を満たす、REST API を実装してください。
依存ライブラリとして fastapi と markitdown を与えますので、それを使ってください。
その他、標準ライブラリは使用可としますが、fastapi と markitdown 以外の外部ライブラリの使用は禁止します。

## Input

```shell
curl 'localhost:8080/v1/markitdown' -XPOST -d '{ "url": "https://example.com" }'
```

## Output

### レスポンスヘッダー

```
Content-Type: text/markdown; charset=utf-8
```

### レスポンスボディ

```md
# Example Domain

This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.

[More information...](https://www.iana.org/domains/example)
```
