from flask import Flask, request, jsonify

# Mock datastructure for now

class Team():
    def __init__(self, team_id, team_name, owned_devices):
        self.team_id = team_id
        self.team_name = team_name
        self.owned_devices = owned_devices
    
    def __call__(self):
        return {
            'team_id': self.team_id,
            'team_name': self.team_name,
            'owned_devices': self.owned_devices
                }

class Device():
    def __init__(self, device_id):
        self.decive_id = device_id

    def __call__(self):
        return {
            'device_id': self.device_id
        }

ramsey95 = Device(1)
roswell = Team(1, 'Hornets', ramsey95)
print(open('index.html', 'r').read())

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html', 'r').read()

@app.route('/<name>')
def print_name(name):
    return f'Hello {name}'

# if __name__ == '__main__':
app.run()