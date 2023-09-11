# How to run

Run the flask and redis containers
```
docker compose up --build -d
```

Test the set endpoint
```
curl -X POST http://localhost:8000/set/ \
-H "Content-Type: application/json" \
-d '{"key": "newkey", "value": "newvaalue"}'
```

There will be three types of responses based on these conditions:
1. if key-value already exist dont overwrite
```
{"message":"Key with this value already exist"}
```
2. if key-value already exist but the value is different do overwrite
```
{"message":"Overwriting key with a new value"}
```
3. if key-value does not exist create a new one
```
{"message":"Key Value write success"}
```
