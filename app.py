from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/github-deploy', methods=['POST'])
def github_deploy():
    return 'POST request to /github-deploy received', 200

if __name__ == '__main__':
    app.run(debug=True, port=5002)
