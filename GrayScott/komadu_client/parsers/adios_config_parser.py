from lxml import etree
from komadu_client.models.ingest_models import attributesType, attributeType
from komadu_client.util.util import get_attributes


def parse_adios2xml(file):
    root = etree.parse(file).getroot()
    # removing comments
    comments = root.xpath('//comment()')
    for comment in comments:
        c_parent = comment.getparent()
        c_parent.remove(comment)

    attributes = get_attributes(flatten_xml_file(root))
    attribute = attributeType()
    attribute.property_ = "location"
    attribute.value_ = str(file)
    attributes.append(attribute)
    return attributes


def flatten_xml_file(root, prefix=""):
    fmap = {}
    for child in root:
        if len(child.getchildren()) > 0:
            values = flatten_xml_file(child, prefix + "_" + child.attrib.values()[0] )
            fmap.update(values)
        else:
            # remove unnecessary '_' in the key
            prefix = prefix.strip('_')
            if child.get("key") is not None:
                # when there are no parameters, just the engine declaration
                fmap[prefix + "_" + child.get("key")] = child.get("value")
            else:
                fmap[prefix] = child.attrib.values()[0]
    return fmap
