import xml.etree.cElementTree as ET
from xml.dom import minidom



class Camera:
    def __init__(self):
        pass

    def add_camera(self,camera_id,camera_name=None, connected=None, trigger_type=None):
        tree = ET.ElementTree(file='FinalPackBag.xml')
        root = tree.getroot()
        camera_list = tree.findall(".//Cameras/")
        for item in camera_list:
            if item.attrib['Id'] == camera_id:
                print('Item Exist')
        new_cam = ET.SubElement(tree.find(".//Cameras"),'Camera',{'Id':camera_id})
        FactoryConfigObject = ET.SubElement(new_cam,'FactoryConfigObject')
        FactoryConfigObject.text = 'CameraMachineConfig'
        DisplayName = ET.SubElement(new_cam,'DisplayName')
        DisplayName.text = camera_name + '\n'
        FactoryObject = ET.SubElement(new_cam, 'FactoryObject')
        FactoryObject.text = '\nManualCamera'
        Connected = ET.SubElement(new_cam,'Connected')
        Connected.text = connected
        tree = ET.ElementTree(root)
        with open("FinalPackBag2.xml", "wb") as f:
            tree.write(f)



    def prettiffy(self,elem):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

