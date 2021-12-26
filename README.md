#### Celery

Celery is configured to run it, type the following command 
```shell
celery -A eShop worker -l info
```

#### Flower
Flower is a tool used to monitor the celery tasks, to check the status of the tasks, type the following command.
```shell
celery -A eShop flower
```