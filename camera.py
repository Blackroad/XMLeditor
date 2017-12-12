import xml.etree.cElementTree as ET



class Camera:
    def __init__(self,camera_id=None, camera_name=None, connected:bool=True, trigger_type=None):
        self.camera_id = camera_id
        self.camera_name = camera_name
        self.connected = connected
        self.trigger_type = trigger_type



    def add_camera(self):
        camera_id = self.camera_id
        tree = ET.ElementTree(file='FinalPackBag.xml')
        root = tree.getroot()
        camera_list = tree.findall(".//Cameras/")
        for item in camera_list:
            if item.attrib['Id'] == camera_id:
                print('Item Exist')
        new_cam = ET.SubElement(ET.Element('Cameras'),'Camera',{'id':camera_id})
        new_cam.text = 'badass'
        root.append(new_cam)
        tree = ET.ElementTree(root)
        with open("FinalPackBag2.xml", "wb") as f:
            tree.write(f)




