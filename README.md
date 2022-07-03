# Url shortener

Aiohttp and postgres based realization of url shortener backend server.

### Install requirements:
```
$ git clone [repo url]
$ cd shortener
```

### Run application:
```
$ docker-compose up
```

### Shortify url:
```
$ curl -X POST -H "Content-Type: application/json" --data '{"url":"http://ya.ru"}' localhost:9002/shortify
```

### Open shortified url (or in browser):
```
$ curl -v -X GET localhost:9002/a
```

### Remove link:
```
$ curl -v -X DELETE localhost:9002/a
```
