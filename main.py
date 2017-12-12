import json
from camera import Camera


def load_config(file):
    with open(file) as opened_file:
        target = json.load(opened_file)
    return target

def test():
    camera = Camera()
    camera.add_camera(camera_id='DM150',camera_name = 'DataMan 150',connected = 'true')


if __name__ == '__main__':
    test()
