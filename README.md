<p align="center">
  <h3 align="center">Balanced Geometry API</h3>

  <p align="center">
    Backend microservice cluster to support the Balanced DEX Frontend
    <br />
</p>

### Overview 
### Endpoints 
| Service | Endpoint | Description | 
| :--- | :--- | :--- | 
| Rest API | /api/v1/loans/{address} | GET loans contract transactions and log events by address |
| Rest API | /api/v1/dex/stats/{market_id} | GET dex market stats by market_id |
| Rest API | /api/v1/dex/balance-of/{address}/{market_id} | GET dex balance by address and market_id |
| Rest API | /api/v1/dex/swap-chart/{market_id}/{interval}/{from_timestamp}/{to_timestamp} | GET dex swap chart prices and volumes in candle format |
| Rest API | /api/v1/coin-gecko/pairs | GET coingecko [/pairs](https://docs.google.com/document/d/1v27QFoQq1SKT3Priq3aqPgB70Xd_PnDzbOCiuoCyixw/edit#heading=h.1xheanl497lm) endpoint |
| Rest API | /api/v1/coin-gecko/tickers | GET coingecko [/tickers](https://docs.google.com/document/d/1v27QFoQq1SKT3Priq3aqPgB70Xd_PnDzbOCiuoCyixw/edit#heading=h.6c8atucyo0ri) endpoint |
| Rest API | /api/v1/coin-gecko/historical_trades | GET coingecko [/historical_trades](https://docs.google.com/document/d/1v27QFoQq1SKT3Priq3aqPgB70Xd_PnDzbOCiuoCyixw/edit#heading=h.7ez4fklzmo7c) endpoint |
| Websocket API | /ws/loans | Websocket connection for all loans contract transactions and log events |
| Websocket API | /ws/oracle-price | Websocket connection to poll dex contract for latest prices on all pools |
| Websocket API | /ws/sicx-ratio | Websocket connection to poll band oracle contract for latest sicx/icx ratio |
| Websocket API | /ws/dex/swap-prices/{market_id} | Websocket connection for dex swap events by market_id |
| Websocket API | /ws/dex/balance-of/{market_id}/{address} | Websocket connection for changing balance by address |
| Websocket API | /ws/dex/stats/{market_id} | Websocket connection for changing market stats by market_id |

> All endpoints are served through a reverse proxy on port `:80`

> All Rest API endpoints are listed on the Swagger docs located at `/api/v1/docs`


### Containers

| Name | Description |  
| :--- | :---------- | 

To clone all dependencies into this repo, checkout the developer section for instructions.  

### Requirements 

Minimum:
- docker 
- docker-compose 

### Usage 

To run the entire stack, simply run. 
```shell script
docker-compose up -d
```

### Development 
#### License

Apache 2.0

