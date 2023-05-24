class Device:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type

    def __call__(self):
        return {'decive_id': self.device_id, 'device_type': self.device_type}
    
    def connect(self, device_ip):
        self.device_ip = device_ip
        pass