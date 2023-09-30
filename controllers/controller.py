from flask import Flask, request, abort
from factory.algo_factory import AlgoFactory

app = Flask(__name__)

factory = AlgoFactory()

@app.get('/limited')
def limitedCalls():
    algo_type = request.args.get('algoType', 'fixedWindow')
    print(f'Limited, Do NOT over use me! :{request.remote_addr}')
    result = factory.getAlgo(algo_type).serveRequest(request.remote_addr)
    print(result)
    if result == 'Too many requests (429)':
        print("Too many requests to Controller")
        abort(429) 
    return result

@app.get('/unlimited')
def unlimitedCalls():
    return "Unlimited"
