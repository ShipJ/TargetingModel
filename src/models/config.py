import os

def get_path():
    cwd = os.getcwd().split('/')
    path = '/'+cwd[1]+'/'+cwd[2]+'/'+cwd[3]+'/'+cwd[4]+'/data/'
    return path
