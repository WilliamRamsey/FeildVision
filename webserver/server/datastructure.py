class Team():
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name

    
    def __call__(self):
        return {'team_id': self.team_id,
                'team_name': self.team_name}

class Player():
    def __init__(self, player_id, player_number, player_name_last, player_name_first, player_devices):
        self.player_id = player_id
        self.player_number = player_number
        self.player_name_last = player_name_last
        self.player_name_first = player_name_first
        self.player_devices = player_devices
    
    def __call__(self):
        return {'player_id': self.player_id,
                'player_number': self.player_number,
                'player_name_last': self.player_name_last,
                'player_name_first': self.player_name_first,
                'player_devices': self.player_devices}

class Device():
    def __init__(self, device_id):
        self.device_id = device_id

    def __call__(self):
        return {
            'device_id': self.device_id
        }