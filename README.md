# ecommerce-microservices-demo

This repository contains a small microservices-style demo for an e-commerce app. It includes multiple Flask-based services and a simple API gateway that forwards requests to service containers.

Services and ports (as defined in the services' `app.py` files):

- gateway (host: `gateway`) — port 5000
- auth_service (host: `auth_service`) — port 5001
- user_service (host: `user_service`) — port 5002
- product_service (host: `product_service`) — port 5003
- order_service (host: `order_service`) — port 5004
- payment_service (host: `payment_service`) — port 5005
- notification_service (host: `notification_service`) — port 5006
- redis_cache (host: `redis_cache`) — port 6379
- db_users and db_orders directories represent local DB containers/services

