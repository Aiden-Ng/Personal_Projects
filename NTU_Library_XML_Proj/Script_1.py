
from lxml import etree

# Load the XSD schema
path = r"C:\Users\Ng Hong Xi\Desktop\tabular to xml\libres_article_schema5.3.1.xsd"
with open(path, 'rb') as schema_file:
    schema_root = etree.XML(schema_file.read())
    schema = etree.XMLSchema(schema_root)
    schema_tree = etree.ElementTree(schema_root)

schema_tree.write(r'C:\Users\Ng Hong Xi\Desktop\schema.xml', pretty_print=True)






