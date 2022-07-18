Installation
```
git clone https://github.com/aquilino/Telegram-Bot-Consult.git
cd Telegram-Bot-Consult
edit bot.env ad to token tlegram
```

If you want to work with Traefik,
```
docker-compose -f docker-compose.yml -f docker-compose.traefik.yml up -d
docker-compose logs -f
```

If you want to work with Caddy,
```
docker-compose -f docker-compose.yml -f docker-compose.caddy.yml up -d
docker-compose logs -f
```

```
Gracias a atareao con linux (Lorenzo Carbonell) me encata su metodo de trabajo.
```