import time
from flask import Flask, request
import redis
from rq import Queue

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)

def background_task(n):
	""" Function that simulates a delay """
	delay = 2
	print("Task running")
	print(f"Simulating {delay} second delay")
	time.sleep(delay)
	print(len(n))
	print("Task complete")
	return len(n)

@app.route("/task", methods=["GET", "POST"])
def add_task():
	global q
	if request.args.get("n"):
		n = request.args.get("n")
		print(f"Your n is {n}")
		job = q.enqueue(background_task, n)
		job = q.enqueue(background_task, request.args.get("n"))
		q_len = len(q)
		return f"Task {job.id} added to queue at {job.enqueued_at}. {q_len} tasks in the queue"
	return "N value for n"

if __name__ == "__main__":
	app.run()
