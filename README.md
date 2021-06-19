# Flex Redis Task Queues

A python-based web application using **flask** to simulates delay and manage **Queue** by getting from Redis in `rq` worker.

## Using

```
rq worker
flask run
```

Next open `http://127.0.0.1:5000/task?n={PUT_ANYTHING}` at your browser.

## Setup

```
python -m venv env
source env/bin/activate
pip install redis flask rq
```

### References

- https://python-rq.org/
- https://python-rq.org/docs/
- https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaQueueinPython.html
- https://www.geeksforgeeks.org/queue-in-python/
- https://pythonise.com/series/learning-flask/flask-rq-task-queue
- https://www.youtube.com/results?search_query=python+redis
- 
© Copyright Max Base, 2021
