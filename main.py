import xml.etree.cElementTree as ET


def editEML(filename):
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()

    camera = tree.find('.//Cameras/')
    camera.attrib['Id'] = 'DataMan152'

    print (camera.attrib)
    tree = ET.ElementTree(root)
    with open('FinalPackBag.xml', 'wb') as f:
         tree.write(f)


if __name__ == '__main__':
    editEML('FinalPackBag.xml')
