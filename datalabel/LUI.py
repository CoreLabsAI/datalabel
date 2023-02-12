


import pandas as pd
import time
import subprocess
import requests
import os
import socket
import subprocess
import webbrowser


def kill_process_on_port(port):
    try:
        output = subprocess.check_output(["lsof", "-i:" + str(port)])
    except subprocess.CalledProcessError:
        return
    
    if output:
        process_ids = output.decode().split("\n")[1:-1]
        process_ids = [line.split()[1] for line in process_ids]
        for pid in process_ids:
            subprocess.call(["kill", "-9", pid])

kill_process_on_port(8080)


import requests
def is_running_on_aws():
    try:
        response = requests.get("http://169.254.169.254/latest/meta-data/", timeout=0.1)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        return False




PATHTOMAIN = str(os.path.dirname(os.path.abspath(__file__))) + '/class_utils/main.py'
PORTNUM = 8080
class LabelService:
    """
    msgs = ['hello', 'hi', 'how are you']
    from EliseAI.labs.UI import LabelService
    ls = LabelService()
    df = ls.label(msgs)
"""
    def __init__(self, silent = True):
        kill_process_on_port(8080)
        #wait til the port is free
        while not subprocess.call(["lsof", "-i:" + str(PORTNUM)]) == 1:
            time.sleep(0.1)


        self.url = self._get_current_host_url()
        self.endpoint = self.url + '/store_messages'
        self.server = None
        self.silent = silent
        self._start_server()
        # print("Server URL: " + self.url)
        

    def _get_current_host_url(self):
        #check if you are on aws or local

        if is_running_on_aws():
            self.aws = True
            
            host_url = socket.gethostbyname(socket.gethostname()).strip()
            host_url = 'http://' + host_url + ':8080'
            return host_url

        else:
            self.aws = False
            host_url = 'http://localhost:8080'
            return host_url

            

    def _ping_server(self):
        try:
            r = requests.get(self.url)
            return True
        except:
            return False
        
    def _start_server(self):
        # print("Starting server...")
        # print(PATHTOMAIN)
        if self.silent:
            devnull = open(os.devnull, 'w')

            process = subprocess.Popen(["python", PATHTOMAIN], stdout=devnull, stderr=subprocess.STDOUT)
        else:
            process = subprocess.Popen(["python", PATHTOMAIN])
        time.sleep(0.5)
        while not self._ping_server():
            time.sleep(0.15)
        # print("Server started!")

    def _send_messages(self, messages, tags_list = None, labels = None, classes = None):
        print("Server URL: " + self.url)
        # print("Sending messages to server..." )
        if tags_list:
            assert len(messages) == len(tags_list), "messages and tags_list must be the same length"
            for i in range(len(tags_list)):
                if not isinstance(tags_list[i], list):
                    tags_list[i] = [tags_list[i]]
        if labels:
            assert len(messages) == len(labels), "messages and labels must be the same length"
        if classes:
            assert len(messages) == len(classes), "messages and classes must be the same length"
            
        json_dict = {'message': messages}
        if tags_list:
            json_dict['tags_list'] = tags_list
        if labels:
            json_dict['labels'] = labels
        if classes:
            json_dict['classes'] = classes

        r = requests.post(self.endpoint, json=json_dict)
        
            
        return r.json()['length']
    
    def get_labeled_messages(self):
        endpoint = self.url + '/labeled_messages'
        r = requests.get(endpoint)
        return pd.DataFrame(r.json())
    

    def check_if_done(self):
        endpoint = self.url + '/check_if_done'
        r = requests.get(endpoint)
        return r.json()['done']

    def label(self, messages, tags_list = None, labels = None, classes = None):
        self._send_messages(messages, tags_list, labels, classes)
        #open the browser
        if not self.aws :
            # print("Opening browser...")
            webbrowser.open(self.url)

        time.sleep(2)
        while not self.check_if_done():
            time.sleep(0.2)
        return self.get_labeled_messages()


    def __del__(self):
        # print("Killing server...")
        #use lsof to get the pid of the server on 8080 and kill it
        os.system("lsof -i:8080 | awk 'NR!=1 {print $2}' | xargs kill -9")

    def stop(self):
        self.__del__()




def __init__(self):
    return LabelService()