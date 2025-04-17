# ai-codegen-example

## How to use

[Install by uv](https://aider.chat/docs/install.html#install-with-uv)

```shell
uv tool install --force --python python3.12 aider-chat@latest
```

Copy files

```shell
cp {template,}.env
cp {template,}.aider.conf.yml
```

Generate file

```shell
aider --no-gitignore --config .aider.conf.yml --message-file ./prompts/generate_server.md src/ai_codegen_example/main.py
```
