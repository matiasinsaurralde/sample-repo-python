# Hello API

FastAPI service. Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+.

## Run

Install dependencies and start the server:

```bash
uv sync
uv run fastapi dev main.py
```

The API listens on `http://127.0.0.1:8000`. Interactive docs: `http://127.0.0.1:8000/docs`.

## Example

```bash
curl -X POST http://127.0.0.1:8000/hello \
  -H 'Content-Type: application/json' \
  -d '{"name": "world"}'
```

Response:

```json
{"name": "world"}
```

List a path:

```bash
curl 'http://127.0.0.1:8000/ls?path=/tmp'
```
