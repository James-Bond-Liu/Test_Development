from multiprocessing import Process
import requests

class Run(Process):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def run(self):
        res = requests.request(method='**', url='**', json='**')
        res.elapsed.total_seconds()




