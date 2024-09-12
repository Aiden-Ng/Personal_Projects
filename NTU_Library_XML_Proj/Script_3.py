import pandas as pd 
from lxml import etree
import xmlschema
print("Sucessfully imported all modules")


XSD_Path = r"C:\Users\Ng Hong Xi\Desktop\tabular to xml\libres_article_schema5.3.1.xsd"
XML_Path = r"C:\Users\Ng Hong Xi\Desktop\tabular to xml\test_article_20240806.xml"

def print_xsd_string():
    with open(XSD_Path, 'rb') as schema_file:
        schema_root = etree.XML(schema_file.read())
        schema_tree = etree.ElementTree(schema_root)
        xml_str = etree.tostring(schema_tree, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        xml_str = xml_str.decode('utf-8')
        #xml_str = xml_str.replace('\\n', '\n').replace('\\t', '\t')
        
        print(xml_str)

def convert_xsd_to_xml_skeleton():
        schema = xmlschema.XMLSchema(XSD_Path)
        xml_data = xmlschema.to_dict(XML_Path, XSD_Path)
        # xml_data = xmlschema.to_dict(XML_Path)
        print(xml_data)
        # xml_skeleton = xmlschema.to_etree(schema)
        # xml_str = etree.tostring(xml_skeleton, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode('utf-8')
        # print(xml_str)


convert_xsd_to_xml_skeleton()    


    





