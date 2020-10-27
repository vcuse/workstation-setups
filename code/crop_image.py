import os
from PIL import Image
import xml.etree.ElementTree as ElementTree

def parse_xml(xml_filepath):
    document = ElementTree.parse(xml_filepath)
    root_node = document.getroot()
    image_filename = root_node.find('filename').text
    objects = {}

    for element_object in root_node.findall('object'):
        object_name = element_object.find('name').text
        bndbox = element_object.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        xmax = int(bndbox.find('xmax').text)
        ymin = int(bndbox.find('ymin').text)
        ymax = int(bndbox.find('ymax').text)
        coordinates = (xmin, ymin, xmax, ymax)

        if not object_name in objects:
            objects[object_name] = []

        objects[object_name].append(coordinates)
    
    return image_filename, objects

def crop_objects_in_image(image_filepath, objects, output_directory):
    image = Image.open(image_filepath)
    image_filename = os.path.basename(image_filepath)

    for object_name in objects:
        object_dir = os.path.join(output_directory, object_name)

        if not os.path.isdir(object_dir):
            os.makedirs(object_dir)

        for index, coordinates in enumerate(objects[object_name]):
            image_crop = image.crop(coordinates)
            image_crop_filepath = os.path.join(object_dir, image_filename.replace('.', '_' + str(index) + '.'))
            image_crop.save(image_crop_filepath)

output_dir = 'C:\\Users\\fronchettl\\Documents\\GitHub\\reddit\\data\\analysis\\Objects'
xml_directories = ['C:\\Users\\fronchettl\\Documents\\GitHub\\reddit\\data\\analysis\\Group 0 (XML)',
                   'C:\\Users\\fronchettl\\Documents\\GitHub\\reddit\\data\\analysis\\Group 1 (XML)',
                   'C:\\Users\\fronchettl\\Documents\\GitHub\\reddit\\data\\analysis\\Group 2 (XML)']

for index, xml_directory in enumerate(xml_directories):
    for xml_filename in os.listdir(xml_directory):
        xml_filepath = os.path.join(xml_directory, xml_filename)
        image_filename, objects = parse_xml(xml_filepath)
        image_directory = xml_directory.replace('(XML)', '(IMG)')
        image_filepath = os.path.join(image_directory, image_filename)
        crop_objects_in_image(image_filepath, objects, output_dir)