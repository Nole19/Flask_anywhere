from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/github-deploy', methods=['POST'])
def github_deploy():
    if request.method == 'POST':
        # Assuming your project directory is correctly set up in your PythonAnywhere account
        # and that your PythonAnywhere account has been configured to use SSH keys for GitHub
        try:
            # Pull the latest changes from the GitHub repository
            # Replace '/home/yourusername/yourrepository' with the actual path to your repository on PythonAnywhere
            subprocess.run(['git', '-C', '/home/nole19/Flask_anywhere', 'pull'], check=True)
            # Return a success message
            return 'Updated code successfully', 200
        except subprocess.CalledProcessError as e:
            # Log the error for debugging
            print("Error occurred while pulling changes:", e)
            return 'Failed to update code', 500

if __name__ == '__main__':
    app.run(debug=True)
