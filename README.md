# es-chatwork-lambda

## Overview

![画像](https://cdn-ssl-devio-img.classmethod.jp/wp-content/uploads/2018/01/ticket-search-1.png)

- User posts the keywords you want to search on ChatWark
- POST request with ChatWark's Webhook
- Excute AWS Lamdba(Amazon Virtual Private Cloud) using Amazon API Gateway.
  - Amazon API Gatewa created a POST method
  - We used NAT Gateway
  - Use a NAT gateway as internet access is required
  - Search on Amazon Elasticsearch Service on VPC private subnet
- Post search results to ChatWark

## How to use

### ChatWork setting 

lambda_function.py
```python
# constant
MY_ACCOUNT = chatwork_account_id
ROOM_ID = 'your_room_id'
```

client/chatwork.py
```python
# constant
URL = "https://api.chatwork.com/v2"
API_KEY = "your_api_key"
```

### Elasticsearch host url setting          
 
client/es.py
``` python
'host': 'your_host'
```

## References

blog url