# Estudando OpenTelemetry e diferenças nas chamadas de sistema
Utilizando o procotolo OpenTelemetry em conjunto com o Jaeger UI para monitrar a diferença no tempo de execução da função `print` e `sys.stdout.write`.

## Ambiente do projeto

Dependencias do projeto:
```bash
pip install -r requirements.txt
```

Imagem Docker do Jaeger:
```bash
docker run -d --name jaeger -p 4317:4317 -p 16686:16686 -p 14250:14250 jaegertracing/all-in-one:latest
```

## Executando o projeto:

Escolha ente `print` e `write`:
```bash
python3 main.py print
```

Caso seja necessário um range diferente, pode ser inserido após a flag `--range`:
```bash
python3 main.py print --range 123456789
```

Após a execução do programa, acesse o Jaeger UI para conferir o monitoramento:
```bash
http://localhost:16686
```
