import json
from camera import Camera


def load_config(file):
    with open(file) as opened_file:
        target = json.load(opened_file)
    return target

def test():
    camera = Camera(camera_id='DM150')
    camera.add_camera()


if __name__ == '__main__':
    test()
