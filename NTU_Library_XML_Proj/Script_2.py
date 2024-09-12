import xmlschema
from lxml import etree

import xmlschema
from lxml import etree

print("Hello World")

try:
    print("Loading XSD schema...")
    # Load the XSD schema
    xsd_path = r"C:\Users\Ng Hong Xi\Desktop\tabular to xml\libres_article_schema5.3.1.xsd"
    schema = xmlschema.XMLSchema(xsd_path)
    print("XSD schema loaded successfully.")

    print("Generating XML skeleton...")
    # Generate an XML skeleton
    xml_skeleton = schema.to_etree()
    print("XML skeleton generated successfully.")

    print("Writing XML skeleton to file...")
    # Write the XML skeleton to a file
    tree = etree.ElementTree(xml_skeleton)
    tree.write(r"C:\Users\Ng Hong Xi\Desktop\generated_skeleton.xml", pretty_print=True, xml_declaration=True, encoding='UTF-8')
    print("XML skeleton written to file successfully!")

except Exception as e:
    print("An error occurred while generating the XML skeleton:")
    print(e)