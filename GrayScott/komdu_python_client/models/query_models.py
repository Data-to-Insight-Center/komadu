# ./query_model/py.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e2251efd35c50feaf4e3d75ec49fa66be38fd868
# Generated 2019-06-19 16:51:10.392908 by PyXB version 1.2.6 using Python 3.7.0.final.0
# Namespace http://komadu.d2i.indiana.edu/query

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f7964440-92d3-11e9-8720-f0189815b4ad')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import komdu_python_client.models._komadu as _ImportedBinding__komadu
import komdu_python_client.models._prov as _ImportedBinding__prov

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://komadu.d2i.indiana.edu/query', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_prov = _ImportedBinding__prov.Namespace
_Namespace_prov.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://komadu.d2i.indiana.edu/query}detailEnumType
class detailEnumType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'detailEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 40, 4)
    _Documentation = None
detailEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=detailEnumType, enum_prefix=None)
detailEnumType.COARSE = detailEnumType._CF_enumeration.addEnumeration(unicode_value='COARSE', tag='COARSE')
detailEnumType.FINE = detailEnumType._CF_enumeration.addEnumeration(unicode_value='FINE', tag='FINE')
detailEnumType._InitializeFacetMap(detailEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'detailEnumType', detailEnumType)
_module_typeBindings.detailEnumType = detailEnumType

# Atomic simple type: {http://komadu.d2i.indiana.edu/query}entityEnumType
class entityEnumType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entityEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 47, 4)
    _Documentation = None
entityEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=entityEnumType, enum_prefix=None)
entityEnumType.FILE = entityEnumType._CF_enumeration.addEnumeration(unicode_value='FILE', tag='FILE')
entityEnumType.BLOCK = entityEnumType._CF_enumeration.addEnumeration(unicode_value='BLOCK', tag='BLOCK')
entityEnumType.COLLECTION = entityEnumType._CF_enumeration.addEnumeration(unicode_value='COLLECTION', tag='COLLECTION')
entityEnumType.GENERIC = entityEnumType._CF_enumeration.addEnumeration(unicode_value='GENERIC', tag='GENERIC')
entityEnumType._InitializeFacetMap(entityEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'entityEnumType', entityEnumType)
_module_typeBindings.entityEnumType = entityEnumType

# Complex type {http://komadu.d2i.indiana.edu/query}getActivityDetailRequestType with content type ELEMENT_ONLY
class getActivityDetailRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getActivityDetailRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getActivityDetailRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 56, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}uniqueURIList uses Python identifier uniqueURIList
    __uniqueURIList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uniqueURIList'), 'uniqueURIList', '__httpkomadu_d2i_indiana_eduquery_getActivityDetailRequestType_httpkomadu_d2i_indiana_eduqueryuniqueURIList', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 59, 16), )

    
    uniqueURIList = property(__uniqueURIList.value, __uniqueURIList.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}uniqueIDList uses Python identifier uniqueIDList
    __uniqueIDList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uniqueIDList'), 'uniqueIDList', '__httpkomadu_d2i_indiana_eduquery_getActivityDetailRequestType_httpkomadu_d2i_indiana_eduqueryuniqueIDList', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 62, 16), )

    
    uniqueIDList = property(__uniqueIDList.value, __uniqueIDList.set, None, None)

    _ElementMap.update({
        __uniqueURIList.name() : __uniqueURIList,
        __uniqueIDList.name() : __uniqueIDList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getActivityDetailRequestType = getActivityDetailRequestType
Namespace.addCategoryObject('typeBinding', 'getActivityDetailRequestType', getActivityDetailRequestType)


# Complex type {http://komadu.d2i.indiana.edu/query}getActivityDetailResponseType with content type ELEMENT_ONLY
class getActivityDetailResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getActivityDetailResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getActivityDetailResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 67, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}activityDetailList uses Python identifier activityDetailList
    __activityDetailList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityDetailList'), 'activityDetailList', '__httpkomadu_d2i_indiana_eduquery_getActivityDetailResponseType_httpkomadu_d2i_indiana_eduqueryactivityDetailList', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 69, 12), )

    
    activityDetailList = property(__activityDetailList.value, __activityDetailList.set, None, None)

    _ElementMap.update({
        __activityDetailList.name() : __activityDetailList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getActivityDetailResponseType = getActivityDetailResponseType
Namespace.addCategoryObject('typeBinding', 'getActivityDetailResponseType', getActivityDetailResponseType)


# Complex type {http://komadu.d2i.indiana.edu/query}getEntityDetailRequestType with content type ELEMENT_ONLY
class getEntityDetailRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getEntityDetailRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getEntityDetailRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 73, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}entityIDList uses Python identifier entityIDList
    __entityIDList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityIDList'), 'entityIDList', '__httpkomadu_d2i_indiana_eduquery_getEntityDetailRequestType_httpkomadu_d2i_indiana_eduqueryentityIDList', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 75, 12), )

    
    entityIDList = property(__entityIDList.value, __entityIDList.set, None, None)

    _ElementMap.update({
        __entityIDList.name() : __entityIDList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getEntityDetailRequestType = getEntityDetailRequestType
Namespace.addCategoryObject('typeBinding', 'getEntityDetailRequestType', getEntityDetailRequestType)


# Complex type {http://komadu.d2i.indiana.edu/query}getEntityDetailResponseType with content type ELEMENT_ONLY
class getEntityDetailResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getEntityDetailResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getEntityDetailResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 79, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}entityDetailList uses Python identifier entityDetailList
    __entityDetailList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityDetailList'), 'entityDetailList', '__httpkomadu_d2i_indiana_eduquery_getEntityDetailResponseType_httpkomadu_d2i_indiana_eduqueryentityDetailList', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 81, 12), )

    
    entityDetailList = property(__entityDetailList.value, __entityDetailList.set, None, None)

    _ElementMap.update({
        __entityDetailList.name() : __entityDetailList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getEntityDetailResponseType = getEntityDetailResponseType
Namespace.addCategoryObject('typeBinding', 'getEntityDetailResponseType', getEntityDetailResponseType)


# Complex type {http://komadu.d2i.indiana.edu/query}findEntityRequestType with content type ELEMENT_ONLY
class findEntityRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}findEntityRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'findEntityRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 85, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}blockName uses Python identifier blockName
    __blockName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'blockName'), 'blockName', '__httpkomadu_d2i_indiana_eduquery_findEntityRequestType_httpkomadu_d2i_indiana_eduqueryblockName', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 89, 20), )

    
    blockName = property(__blockName.value, __blockName.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}blockContent uses Python identifier blockContent
    __blockContent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'blockContent'), 'blockContent', '__httpkomadu_d2i_indiana_eduquery_findEntityRequestType_httpkomadu_d2i_indiana_eduqueryblockContent', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 90, 20), )

    
    blockContent = property(__blockContent.value, __blockContent.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}blockMD5Checksum uses Python identifier blockMD5Checksum
    __blockMD5Checksum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'blockMD5Checksum'), 'blockMD5Checksum', '__httpkomadu_d2i_indiana_eduquery_findEntityRequestType_httpkomadu_d2i_indiana_eduqueryblockMD5Checksum', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 91, 20), )

    
    blockMD5Checksum = property(__blockMD5Checksum.value, __blockMD5Checksum.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}blockSize uses Python identifier blockSize
    __blockSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'blockSize'), 'blockSize', '__httpkomadu_d2i_indiana_eduquery_findEntityRequestType_httpkomadu_d2i_indiana_eduqueryblockSize', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 92, 20), )

    
    blockSize = property(__blockSize.value, __blockSize.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}fileName uses Python identifier fileName
    __fileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileName'), 'fileName', '__httpkomadu_d2i_indiana_eduquery_findEntityRequestType_httpkomadu_d2i_indiana_eduqueryfileName', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 95, 20), )

    
    fileName = property(__fileName.value, __fileName.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}fileURI uses Python identifier fileURI
    __fileURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileURI'), 'fileURI', '__httpkomadu_d2i_indiana_eduquery_findEntityRequestType_httpkomadu_d2i_indiana_eduqueryfileURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 96, 20), )

    
    fileURI = property(__fileURI.value, __fileURI.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}fileOwnerID uses Python identifier fileOwnerID
    __fileOwnerID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileOwnerID'), 'fileOwnerID', '__httpkomadu_d2i_indiana_eduquery_findEntityRequestType_httpkomadu_d2i_indiana_eduqueryfileOwnerID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 97, 20), )

    
    fileOwnerID = property(__fileOwnerID.value, __fileOwnerID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}fileCreationDate uses Python identifier fileCreationDate
    __fileCreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileCreationDate'), 'fileCreationDate', '__httpkomadu_d2i_indiana_eduquery_findEntityRequestType_httpkomadu_d2i_indiana_eduqueryfileCreationDate', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 98, 20), )

    
    fileCreationDate = property(__fileCreationDate.value, __fileCreationDate.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}fileMD5Checksum uses Python identifier fileMD5Checksum
    __fileMD5Checksum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileMD5Checksum'), 'fileMD5Checksum', '__httpkomadu_d2i_indiana_eduquery_findEntityRequestType_httpkomadu_d2i_indiana_eduqueryfileMD5Checksum', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 99, 20), )

    
    fileMD5Checksum = property(__fileMD5Checksum.value, __fileMD5Checksum.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}fileSize uses Python identifier fileSize
    __fileSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileSize'), 'fileSize', '__httpkomadu_d2i_indiana_eduquery_findEntityRequestType_httpkomadu_d2i_indiana_eduqueryfileSize', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 100, 20), )

    
    fileSize = property(__fileSize.value, __fileSize.set, None, None)

    _ElementMap.update({
        __blockName.name() : __blockName,
        __blockContent.name() : __blockContent,
        __blockMD5Checksum.name() : __blockMD5Checksum,
        __blockSize.name() : __blockSize,
        __fileName.name() : __fileName,
        __fileURI.name() : __fileURI,
        __fileOwnerID.name() : __fileOwnerID,
        __fileCreationDate.name() : __fileCreationDate,
        __fileMD5Checksum.name() : __fileMD5Checksum,
        __fileSize.name() : __fileSize
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.findEntityRequestType = findEntityRequestType
Namespace.addCategoryObject('typeBinding', 'findEntityRequestType', findEntityRequestType)


# Complex type {http://komadu.d2i.indiana.edu/query}findEntityResponseType with content type ELEMENT_ONLY
class findEntityResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}findEntityResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'findEntityResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 106, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}uniqueBlockIDList uses Python identifier uniqueBlockIDList
    __uniqueBlockIDList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uniqueBlockIDList'), 'uniqueBlockIDList', '__httpkomadu_d2i_indiana_eduquery_findEntityResponseType_httpkomadu_d2i_indiana_eduqueryuniqueBlockIDList', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 109, 16), )

    
    uniqueBlockIDList = property(__uniqueBlockIDList.value, __uniqueBlockIDList.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}uniqueFileURIList uses Python identifier uniqueFileURIList
    __uniqueFileURIList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uniqueFileURIList'), 'uniqueFileURIList', '__httpkomadu_d2i_indiana_eduquery_findEntityResponseType_httpkomadu_d2i_indiana_eduqueryuniqueFileURIList', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 112, 16), )

    
    uniqueFileURIList = property(__uniqueFileURIList.value, __uniqueFileURIList.set, None, None)

    _ElementMap.update({
        __uniqueBlockIDList.name() : __uniqueBlockIDList,
        __uniqueFileURIList.name() : __uniqueFileURIList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.findEntityResponseType = findEntityResponseType
Namespace.addCategoryObject('typeBinding', 'findEntityResponseType', findEntityResponseType)


# Complex type {http://komadu.d2i.indiana.edu/query}findActivityRequestType with content type ELEMENT_ONLY
class findActivityRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}findActivityRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'findActivityRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 117, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpkomadu_d2i_indiana_eduquery_findActivityRequestType_httpkomadu_d2i_indiana_eduqueryname', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 119, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}hostName uses Python identifier hostName
    __hostName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hostName'), 'hostName', '__httpkomadu_d2i_indiana_eduquery_findActivityRequestType_httpkomadu_d2i_indiana_eduqueryhostName', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 120, 12), )

    
    hostName = property(__hostName.value, __hostName.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}architecture uses Python identifier architecture
    __architecture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'architecture'), 'architecture', '__httpkomadu_d2i_indiana_eduquery_findActivityRequestType_httpkomadu_d2i_indiana_eduqueryarchitecture', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 121, 12), )

    
    architecture = property(__architecture.value, __architecture.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}workflowID uses Python identifier workflowID
    __workflowID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'workflowID'), 'workflowID', '__httpkomadu_d2i_indiana_eduquery_findActivityRequestType_httpkomadu_d2i_indiana_eduqueryworkflowID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 126, 12), )

    
    workflowID = property(__workflowID.value, __workflowID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}serviceID uses Python identifier serviceID
    __serviceID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serviceID'), 'serviceID', '__httpkomadu_d2i_indiana_eduquery_findActivityRequestType_httpkomadu_d2i_indiana_eduqueryserviceID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 127, 12), )

    
    serviceID = property(__serviceID.value, __serviceID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}nextActivityID uses Python identifier nextActivityID
    __nextActivityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nextActivityID'), 'nextActivityID', '__httpkomadu_d2i_indiana_eduquery_findActivityRequestType_httpkomadu_d2i_indiana_eduquerynextActivityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 128, 12), )

    
    nextActivityID = property(__nextActivityID.value, __nextActivityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}attributeList uses Python identifier attributeList
    __attributeList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributeList'), 'attributeList', '__httpkomadu_d2i_indiana_eduquery_findActivityRequestType_httpkomadu_d2i_indiana_eduqueryattributeList', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 129, 12), )

    
    attributeList = property(__attributeList.value, __attributeList.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __hostName.name() : __hostName,
        __architecture.name() : __architecture,
        __workflowID.name() : __workflowID,
        __serviceID.name() : __serviceID,
        __nextActivityID.name() : __nextActivityID,
        __attributeList.name() : __attributeList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.findActivityRequestType = findActivityRequestType
Namespace.addCategoryObject('typeBinding', 'findActivityRequestType', findActivityRequestType)


# Complex type {http://komadu.d2i.indiana.edu/query}findActivityResponseType with content type ELEMENT_ONLY
class findActivityResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}findActivityResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'findActivityResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 133, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}uniqueURIList uses Python identifier uniqueURIList
    __uniqueURIList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uniqueURIList'), 'uniqueURIList', '__httpkomadu_d2i_indiana_eduquery_findActivityResponseType_httpkomadu_d2i_indiana_eduqueryuniqueURIList', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 136, 16), )

    
    uniqueURIList = property(__uniqueURIList.value, __uniqueURIList.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}activityIDList uses Python identifier activityIDList
    __activityIDList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityIDList'), 'activityIDList', '__httpkomadu_d2i_indiana_eduquery_findActivityResponseType_httpkomadu_d2i_indiana_eduqueryactivityIDList', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 139, 16), )

    
    activityIDList = property(__activityIDList.value, __activityIDList.set, None, None)

    _ElementMap.update({
        __uniqueURIList.name() : __uniqueURIList,
        __activityIDList.name() : __activityIDList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.findActivityResponseType = findActivityResponseType
Namespace.addCategoryObject('typeBinding', 'findActivityResponseType', findActivityResponseType)


# Complex type {http://komadu.d2i.indiana.edu/query}getContextWorkflowGraphRequestType with content type ELEMENT_ONLY
class getContextWorkflowGraphRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getContextWorkflowGraphRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getContextWorkflowGraphRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 144, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}contextWorkflowURI uses Python identifier contextWorkflowURI
    __contextWorkflowURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contextWorkflowURI'), 'contextWorkflowURI', '__httpkomadu_d2i_indiana_eduquery_getContextWorkflowGraphRequestType_httpkomadu_d2i_indiana_eduquerycontextWorkflowURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 146, 12), )

    
    contextWorkflowURI = property(__contextWorkflowURI.value, __contextWorkflowURI.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}informationDetailLevel uses Python identifier informationDetailLevel
    __informationDetailLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel'), 'informationDetailLevel', '__httpkomadu_d2i_indiana_eduquery_getContextWorkflowGraphRequestType_httpkomadu_d2i_indiana_eduqueryinformationDetailLevel', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 147, 12), )

    
    informationDetailLevel = property(__informationDetailLevel.value, __informationDetailLevel.set, None, None)

    _ElementMap.update({
        __contextWorkflowURI.name() : __contextWorkflowURI,
        __informationDetailLevel.name() : __informationDetailLevel
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getContextWorkflowGraphRequestType = getContextWorkflowGraphRequestType
Namespace.addCategoryObject('typeBinding', 'getContextWorkflowGraphRequestType', getContextWorkflowGraphRequestType)


# Complex type {http://komadu.d2i.indiana.edu/query}getContextWorkflowGraphResponseType with content type ELEMENT_ONLY
class getContextWorkflowGraphResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getContextWorkflowGraphResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getContextWorkflowGraphResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 151, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/prov#}document uses Python identifier document
    __document = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_prov, 'document'), 'document', '__httpkomadu_d2i_indiana_eduquery_getContextWorkflowGraphResponseType_httpwww_w3_orgnsprovdocument', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/prov-20130307.xsd', 648, 2), )

    
    document = property(__document.value, __document.set, None, None)

    _ElementMap.update({
        __document.name() : __document
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getContextWorkflowGraphResponseType = getContextWorkflowGraphResponseType
Namespace.addCategoryObject('typeBinding', 'getContextWorkflowGraphResponseType', getContextWorkflowGraphResponseType)


# Complex type {http://komadu.d2i.indiana.edu/query}getActivityGraphRequestType with content type ELEMENT_ONLY
class getActivityGraphRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getActivityGraphRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getActivityGraphRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 157, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}activityURI uses Python identifier activityURI
    __activityURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityURI'), 'activityURI', '__httpkomadu_d2i_indiana_eduquery_getActivityGraphRequestType_httpkomadu_d2i_indiana_eduqueryactivityURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 159, 12), )

    
    activityURI = property(__activityURI.value, __activityURI.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}informationDetailLevel uses Python identifier informationDetailLevel
    __informationDetailLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel'), 'informationDetailLevel', '__httpkomadu_d2i_indiana_eduquery_getActivityGraphRequestType_httpkomadu_d2i_indiana_eduqueryinformationDetailLevel', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 160, 12), )

    
    informationDetailLevel = property(__informationDetailLevel.value, __informationDetailLevel.set, None, None)

    _ElementMap.update({
        __activityURI.name() : __activityURI,
        __informationDetailLevel.name() : __informationDetailLevel
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getActivityGraphRequestType = getActivityGraphRequestType
Namespace.addCategoryObject('typeBinding', 'getActivityGraphRequestType', getActivityGraphRequestType)


# Complex type {http://komadu.d2i.indiana.edu/query}getActivityGraphResponseType with content type ELEMENT_ONLY
class getActivityGraphResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getActivityGraphResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getActivityGraphResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 164, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/prov#}document uses Python identifier document
    __document = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_prov, 'document'), 'document', '__httpkomadu_d2i_indiana_eduquery_getActivityGraphResponseType_httpwww_w3_orgnsprovdocument', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/prov-20130307.xsd', 648, 2), )

    
    document = property(__document.value, __document.set, None, None)

    _ElementMap.update({
        __document.name() : __document
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getActivityGraphResponseType = getActivityGraphResponseType
Namespace.addCategoryObject('typeBinding', 'getActivityGraphResponseType', getActivityGraphResponseType)


# Complex type {http://komadu.d2i.indiana.edu/query}getEntityGraphRequestType with content type ELEMENT_ONLY
class getEntityGraphRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getEntityGraphRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getEntityGraphRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 170, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}entityURI uses Python identifier entityURI
    __entityURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityURI'), 'entityURI', '__httpkomadu_d2i_indiana_eduquery_getEntityGraphRequestType_httpkomadu_d2i_indiana_eduqueryentityURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 172, 12), )

    
    entityURI = property(__entityURI.value, __entityURI.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}entityType uses Python identifier entityType
    __entityType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityType'), 'entityType', '__httpkomadu_d2i_indiana_eduquery_getEntityGraphRequestType_httpkomadu_d2i_indiana_eduqueryentityType', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 173, 12), )

    
    entityType = property(__entityType.value, __entityType.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}informationDetailLevel uses Python identifier informationDetailLevel
    __informationDetailLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel'), 'informationDetailLevel', '__httpkomadu_d2i_indiana_eduquery_getEntityGraphRequestType_httpkomadu_d2i_indiana_eduqueryinformationDetailLevel', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 174, 12), )

    
    informationDetailLevel = property(__informationDetailLevel.value, __informationDetailLevel.set, None, None)

    _ElementMap.update({
        __entityURI.name() : __entityURI,
        __entityType.name() : __entityType,
        __informationDetailLevel.name() : __informationDetailLevel
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getEntityGraphRequestType = getEntityGraphRequestType
Namespace.addCategoryObject('typeBinding', 'getEntityGraphRequestType', getEntityGraphRequestType)


# Complex type {http://komadu.d2i.indiana.edu/query}getEntityGraphResponseType with content type ELEMENT_ONLY
class getEntityGraphResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getEntityGraphResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getEntityGraphResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 178, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/prov#}document uses Python identifier document
    __document = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_prov, 'document'), 'document', '__httpkomadu_d2i_indiana_eduquery_getEntityGraphResponseType_httpwww_w3_orgnsprovdocument', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/prov-20130307.xsd', 648, 2), )

    
    document = property(__document.value, __document.set, None, None)

    _ElementMap.update({
        __document.name() : __document
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getEntityGraphResponseType = getEntityGraphResponseType
Namespace.addCategoryObject('typeBinding', 'getEntityGraphResponseType', getEntityGraphResponseType)


# Complex type {http://komadu.d2i.indiana.edu/query}getAgentGraphRequestType with content type ELEMENT_ONLY
class getAgentGraphRequestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getAgentGraphRequestType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getAgentGraphRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 184, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}agentID uses Python identifier agentID
    __agentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agentID'), 'agentID', '__httpkomadu_d2i_indiana_eduquery_getAgentGraphRequestType_httpkomadu_d2i_indiana_eduqueryagentID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 186, 12), )

    
    agentID = property(__agentID.value, __agentID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}informationDetailLevel uses Python identifier informationDetailLevel
    __informationDetailLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel'), 'informationDetailLevel', '__httpkomadu_d2i_indiana_eduquery_getAgentGraphRequestType_httpkomadu_d2i_indiana_eduqueryinformationDetailLevel', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 187, 12), )

    
    informationDetailLevel = property(__informationDetailLevel.value, __informationDetailLevel.set, None, None)

    _ElementMap.update({
        __agentID.name() : __agentID,
        __informationDetailLevel.name() : __informationDetailLevel
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getAgentGraphRequestType = getAgentGraphRequestType
Namespace.addCategoryObject('typeBinding', 'getAgentGraphRequestType', getAgentGraphRequestType)


# Complex type {http://komadu.d2i.indiana.edu/query}getAgentGraphResponseType with content type ELEMENT_ONLY
class getAgentGraphResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}getAgentGraphResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'getAgentGraphResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 191, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/prov#}document uses Python identifier document
    __document = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_prov, 'document'), 'document', '__httpkomadu_d2i_indiana_eduquery_getAgentGraphResponseType_httpwww_w3_orgnsprovdocument', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/prov-20130307.xsd', 648, 2), )

    
    document = property(__document.value, __document.set, None, None)

    _ElementMap.update({
        __document.name() : __document
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.getAgentGraphResponseType = getAgentGraphResponseType
Namespace.addCategoryObject('typeBinding', 'getAgentGraphResponseType', getAgentGraphResponseType)


# Complex type {http://komadu.d2i.indiana.edu/query}activityDetailListType with content type ELEMENT_ONLY
class activityDetailListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}activityDetailListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'activityDetailListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 197, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}activityDetail uses Python identifier activityDetail
    __activityDetail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityDetail'), 'activityDetail', '__httpkomadu_d2i_indiana_eduquery_activityDetailListType_httpkomadu_d2i_indiana_eduqueryactivityDetail', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 199, 12), )

    
    activityDetail = property(__activityDetail.value, __activityDetail.set, None, None)

    _ElementMap.update({
        __activityDetail.name() : __activityDetail
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.activityDetailListType = activityDetailListType
Namespace.addCategoryObject('typeBinding', 'activityDetailListType', activityDetailListType)


# Complex type {http://komadu.d2i.indiana.edu/query}activityDetail with content type ELEMENT_ONLY
class activityDetail (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}activityDetail with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'activityDetail')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 204, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__httpkomadu_d2i_indiana_eduquery_activityDetail_httpkomadu_d2i_indiana_eduquerytype', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 206, 12), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}workflowID uses Python identifier workflowID
    __workflowID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'workflowID'), 'workflowID', '__httpkomadu_d2i_indiana_eduquery_activityDetail_httpkomadu_d2i_indiana_eduqueryworkflowID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 207, 12), )

    
    workflowID = property(__workflowID.value, __workflowID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}serviceID uses Python identifier serviceID
    __serviceID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serviceID'), 'serviceID', '__httpkomadu_d2i_indiana_eduquery_activityDetail_httpkomadu_d2i_indiana_eduqueryserviceID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 208, 12), )

    
    serviceID = property(__serviceID.value, __serviceID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}timestep uses Python identifier timestep
    __timestep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timestep'), 'timestep', '__httpkomadu_d2i_indiana_eduquery_activityDetail_httpkomadu_d2i_indiana_eduquerytimestep', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 209, 12), )

    
    timestep = property(__timestep.value, __timestep.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}workflowNodeID uses Python identifier workflowNodeID
    __workflowNodeID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'workflowNodeID'), 'workflowNodeID', '__httpkomadu_d2i_indiana_eduquery_activityDetail_httpkomadu_d2i_indiana_eduqueryworkflowNodeID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 210, 12), )

    
    workflowNodeID = property(__workflowNodeID.value, __workflowNodeID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}instanceOf uses Python identifier instanceOf
    __instanceOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'instanceOf'), 'instanceOf', '__httpkomadu_d2i_indiana_eduquery_activityDetail_httpkomadu_d2i_indiana_eduqueryinstanceOf', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 211, 12), )

    
    instanceOf = property(__instanceOf.value, __instanceOf.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_eduquery_activityDetail_httpkomadu_d2i_indiana_eduqueryattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 212, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpkomadu_d2i_indiana_eduquery_activityDetail_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 217, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 217, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __workflowID.name() : __workflowID,
        __serviceID.name() : __serviceID,
        __timestep.name() : __timestep,
        __workflowNodeID.name() : __workflowNodeID,
        __instanceOf.name() : __instanceOf,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.activityDetail = activityDetail
Namespace.addCategoryObject('typeBinding', 'activityDetail', activityDetail)


# Complex type {http://komadu.d2i.indiana.edu/query}uniqueURIListType with content type ELEMENT_ONLY
class uniqueURIListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}uniqueURIListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uniqueURIListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 220, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}uniqueURI uses Python identifier uniqueURI
    __uniqueURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uniqueURI'), 'uniqueURI', '__httpkomadu_d2i_indiana_eduquery_uniqueURIListType_httpkomadu_d2i_indiana_eduqueryuniqueURI', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 222, 12), )

    
    uniqueURI = property(__uniqueURI.value, __uniqueURI.set, None, None)

    _ElementMap.update({
        __uniqueURI.name() : __uniqueURI
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.uniqueURIListType = uniqueURIListType
Namespace.addCategoryObject('typeBinding', 'uniqueURIListType', uniqueURIListType)


# Complex type {http://komadu.d2i.indiana.edu/query}activityIDListType with content type ELEMENT_ONLY
class activityIDListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}activityIDListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'activityIDListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 225, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}activityID uses Python identifier activityID
    __activityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityID'), 'activityID', '__httpkomadu_d2i_indiana_eduquery_activityIDListType_httpkomadu_d2i_indiana_eduqueryactivityID', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 227, 12), )

    
    activityID = property(__activityID.value, __activityID.set, None, None)

    _ElementMap.update({
        __activityID.name() : __activityID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.activityIDListType = activityIDListType
Namespace.addCategoryObject('typeBinding', 'activityIDListType', activityIDListType)


# Complex type {http://komadu.d2i.indiana.edu/query}uniqueIDListType with content type ELEMENT_ONLY
class uniqueIDListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}uniqueIDListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uniqueIDListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 230, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}uniqueID uses Python identifier uniqueID
    __uniqueID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uniqueID'), 'uniqueID', '__httpkomadu_d2i_indiana_eduquery_uniqueIDListType_httpkomadu_d2i_indiana_eduqueryuniqueID', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 232, 12), )

    
    uniqueID = property(__uniqueID.value, __uniqueID.set, None, None)

    _ElementMap.update({
        __uniqueID.name() : __uniqueID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.uniqueIDListType = uniqueIDListType
Namespace.addCategoryObject('typeBinding', 'uniqueIDListType', uniqueIDListType)


# Complex type {http://komadu.d2i.indiana.edu/query}abstractServiceDetailListType with content type ELEMENT_ONLY
class abstractServiceDetailListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}abstractServiceDetailListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractServiceDetailListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 236, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}abstractServiceDetail uses Python identifier abstractServiceDetail
    __abstractServiceDetail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'abstractServiceDetail'), 'abstractServiceDetail', '__httpkomadu_d2i_indiana_eduquery_abstractServiceDetailListType_httpkomadu_d2i_indiana_eduqueryabstractServiceDetail', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 238, 12), )

    
    abstractServiceDetail = property(__abstractServiceDetail.value, __abstractServiceDetail.set, None, None)

    _ElementMap.update({
        __abstractServiceDetail.name() : __abstractServiceDetail
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.abstractServiceDetailListType = abstractServiceDetailListType
Namespace.addCategoryObject('typeBinding', 'abstractServiceDetailListType', abstractServiceDetailListType)


# Complex type {http://komadu.d2i.indiana.edu/query}abstractServiceDetail with content type ELEMENT_ONLY
class abstractServiceDetail (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}abstractServiceDetail with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractServiceDetail')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 242, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__httpkomadu_d2i_indiana_eduquery_abstractServiceDetail_httpkomadu_d2i_indiana_eduquerytype', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 244, 12), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpkomadu_d2i_indiana_eduquery_abstractServiceDetail_httpkomadu_d2i_indiana_eduqueryname', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 246, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'version'), 'version', '__httpkomadu_d2i_indiana_eduquery_abstractServiceDetail_httpkomadu_d2i_indiana_eduqueryversion', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 247, 12), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpkomadu_d2i_indiana_eduquery_abstractServiceDetail_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 250, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 250, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __name.name() : __name,
        __version.name() : __version
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.abstractServiceDetail = abstractServiceDetail
Namespace.addCategoryObject('typeBinding', 'abstractServiceDetail', abstractServiceDetail)


# Complex type {http://komadu.d2i.indiana.edu/query}methodNameListType with content type ELEMENT_ONLY
class methodNameListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}methodNameListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'methodNameListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 252, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}methodName uses Python identifier methodName
    __methodName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'methodName'), 'methodName', '__httpkomadu_d2i_indiana_eduquery_methodNameListType_httpkomadu_d2i_indiana_eduquerymethodName', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 254, 12), )

    
    methodName = property(__methodName.value, __methodName.set, None, None)

    _ElementMap.update({
        __methodName.name() : __methodName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.methodNameListType = methodNameListType
Namespace.addCategoryObject('typeBinding', 'methodNameListType', methodNameListType)


# Complex type {http://komadu.d2i.indiana.edu/query}abstractMethodListType with content type ELEMENT_ONLY
class abstractMethodListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}abstractMethodListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractMethodListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 258, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}abstractMethod uses Python identifier abstractMethod
    __abstractMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'abstractMethod'), 'abstractMethod', '__httpkomadu_d2i_indiana_eduquery_abstractMethodListType_httpkomadu_d2i_indiana_eduqueryabstractMethod', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 260, 12), )

    
    abstractMethod = property(__abstractMethod.value, __abstractMethod.set, None, None)

    _ElementMap.update({
        __abstractMethod.name() : __abstractMethod
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.abstractMethodListType = abstractMethodListType
Namespace.addCategoryObject('typeBinding', 'abstractMethodListType', abstractMethodListType)


# Complex type {http://komadu.d2i.indiana.edu/query}entityNameListType with content type ELEMENT_ONLY
class entityNameListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}entityNameListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entityNameListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 264, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}entityName uses Python identifier entityName
    __entityName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityName'), 'entityName', '__httpkomadu_d2i_indiana_eduquery_entityNameListType_httpkomadu_d2i_indiana_eduqueryentityName', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 266, 12), )

    
    entityName = property(__entityName.value, __entityName.set, None, None)

    _ElementMap.update({
        __entityName.name() : __entityName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.entityNameListType = entityNameListType
Namespace.addCategoryObject('typeBinding', 'entityNameListType', entityNameListType)


# Complex type {http://komadu.d2i.indiana.edu/query}entityTypeListType with content type ELEMENT_ONLY
class entityTypeListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}entityTypeListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entityTypeListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 269, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}entityType uses Python identifier entityType
    __entityType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityType'), 'entityType', '__httpkomadu_d2i_indiana_eduquery_entityTypeListType_httpkomadu_d2i_indiana_eduqueryentityType', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 271, 12), )

    
    entityType = property(__entityType.value, __entityType.set, None, None)

    _ElementMap.update({
        __entityType.name() : __entityType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.entityTypeListType = entityTypeListType
Namespace.addCategoryObject('typeBinding', 'entityTypeListType', entityTypeListType)


# Complex type {http://komadu.d2i.indiana.edu/query}entityIDListType with content type ELEMENT_ONLY
class entityIDListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}entityIDListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entityIDListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 274, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}entityID uses Python identifier entityID
    __entityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityID'), 'entityID', '__httpkomadu_d2i_indiana_eduquery_entityIDListType_httpkomadu_d2i_indiana_eduqueryentityID', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 276, 12), )

    
    entityID = property(__entityID.value, __entityID.set, None, None)

    _ElementMap.update({
        __entityID.name() : __entityID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.entityIDListType = entityIDListType
Namespace.addCategoryObject('typeBinding', 'entityIDListType', entityIDListType)


# Complex type {http://komadu.d2i.indiana.edu/query}abstractEntityListType with content type ELEMENT_ONLY
class abstractEntityListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}abstractEntityListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractEntityListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 279, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}abstractEntityDetail uses Python identifier abstractEntityDetail
    __abstractEntityDetail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'abstractEntityDetail'), 'abstractEntityDetail', '__httpkomadu_d2i_indiana_eduquery_abstractEntityListType_httpkomadu_d2i_indiana_eduqueryabstractEntityDetail', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 281, 12), )

    
    abstractEntityDetail = property(__abstractEntityDetail.value, __abstractEntityDetail.set, None, None)

    _ElementMap.update({
        __abstractEntityDetail.name() : __abstractEntityDetail
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.abstractEntityListType = abstractEntityListType
Namespace.addCategoryObject('typeBinding', 'abstractEntityListType', abstractEntityListType)


# Complex type {http://komadu.d2i.indiana.edu/query}abstractEntityDetail with content type ELEMENT_ONLY
class abstractEntityDetail (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}abstractEntityDetail with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractEntityDetail')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 285, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpkomadu_d2i_indiana_eduquery_abstractEntityDetail_httpkomadu_d2i_indiana_eduqueryname', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 287, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__httpkomadu_d2i_indiana_eduquery_abstractEntityDetail_httpkomadu_d2i_indiana_eduquerytype', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 288, 12), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpkomadu_d2i_indiana_eduquery_abstractEntityDetail_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 290, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 290, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __type.name() : __type
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.abstractEntityDetail = abstractEntityDetail
Namespace.addCategoryObject('typeBinding', 'abstractEntityDetail', abstractEntityDetail)


# Complex type {http://komadu.d2i.indiana.edu/query}uniqueFileListType with content type ELEMENT_ONLY
class uniqueFileListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}uniqueFileListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'uniqueFileListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 292, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}fileURIDetailsType uses Python identifier fileURIDetailsType
    __fileURIDetailsType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileURIDetailsType'), 'fileURIDetailsType', '__httpkomadu_d2i_indiana_eduquery_uniqueFileListType_httpkomadu_d2i_indiana_eduqueryfileURIDetailsType', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 294, 12), )

    
    fileURIDetailsType = property(__fileURIDetailsType.value, __fileURIDetailsType.set, None, None)

    _ElementMap.update({
        __fileURIDetailsType.name() : __fileURIDetailsType
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.uniqueFileListType = uniqueFileListType
Namespace.addCategoryObject('typeBinding', 'uniqueFileListType', uniqueFileListType)


# Complex type {http://komadu.d2i.indiana.edu/query}fileURIDetailsType with content type ELEMENT_ONLY
class fileURIDetailsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}fileURIDetailsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fileURIDetailsType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 298, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}fileID uses Python identifier fileID
    __fileID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileID'), 'fileID', '__httpkomadu_d2i_indiana_eduquery_fileURIDetailsType_httpkomadu_d2i_indiana_eduqueryfileID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 300, 12), )

    
    fileID = property(__fileID.value, __fileID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}fileURI uses Python identifier fileURI
    __fileURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileURI'), 'fileURI', '__httpkomadu_d2i_indiana_eduquery_fileURIDetailsType_httpkomadu_d2i_indiana_eduqueryfileURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 301, 12), )

    
    fileURI = property(__fileURI.value, __fileURI.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creationDate'), 'creationDate', '__httpkomadu_d2i_indiana_eduquery_fileURIDetailsType_httpkomadu_d2i_indiana_eduquerycreationDate', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 302, 12), )

    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    _ElementMap.update({
        __fileID.name() : __fileID,
        __fileURI.name() : __fileURI,
        __creationDate.name() : __creationDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.fileURIDetailsType = fileURIDetailsType
Namespace.addCategoryObject('typeBinding', 'fileURIDetailsType', fileURIDetailsType)


# Complex type {http://komadu.d2i.indiana.edu/query}entityDetailListType with content type ELEMENT_ONLY
class entityDetailListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}entityDetailListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entityDetailListType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 305, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}entityDetail uses Python identifier entityDetail
    __entityDetail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityDetail'), 'entityDetail', '__httpkomadu_d2i_indiana_eduquery_entityDetailListType_httpkomadu_d2i_indiana_eduqueryentityDetail', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 307, 12), )

    
    entityDetail = property(__entityDetail.value, __entityDetail.set, None, None)

    _ElementMap.update({
        __entityDetail.name() : __entityDetail
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.entityDetailListType = entityDetailListType
Namespace.addCategoryObject('typeBinding', 'entityDetailListType', entityDetailListType)


# Complex type {http://komadu.d2i.indiana.edu/query}entityDetail with content type ELEMENT_ONLY
class entityDetail (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}entityDetail with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entityDetail')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 311, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}fileURI uses Python identifier fileURI
    __fileURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileURI'), 'fileURI', '__httpkomadu_d2i_indiana_eduquery_entityDetail_httpkomadu_d2i_indiana_eduqueryfileURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 314, 16), )

    
    fileURI = property(__fileURI.value, __fileURI.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}owner uses Python identifier owner
    __owner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'owner'), 'owner', '__httpkomadu_d2i_indiana_eduquery_entityDetail_httpkomadu_d2i_indiana_eduqueryowner', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 315, 16), )

    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creationDate'), 'creationDate', '__httpkomadu_d2i_indiana_eduquery_entityDetail_httpkomadu_d2i_indiana_eduquerycreationDate', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 316, 16), )

    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'size'), 'size', '__httpkomadu_d2i_indiana_eduquery_entityDetail_httpkomadu_d2i_indiana_eduquerysize', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 317, 16), )

    
    size = property(__size.value, __size.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}md5 uses Python identifier md5
    __md5 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'md5'), 'md5', '__httpkomadu_d2i_indiana_eduquery_entityDetail_httpkomadu_d2i_indiana_eduquerymd5', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 318, 16), )

    
    md5 = property(__md5.value, __md5.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}fileName uses Python identifier fileName
    __fileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileName'), 'fileName', '__httpkomadu_d2i_indiana_eduquery_entityDetail_httpkomadu_d2i_indiana_eduqueryfileName', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 319, 16), )

    
    fileName = property(__fileName.value, __fileName.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}blockContent uses Python identifier blockContent
    __blockContent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'blockContent'), 'blockContent', '__httpkomadu_d2i_indiana_eduquery_entityDetail_httpkomadu_d2i_indiana_eduqueryblockContent', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 322, 16), )

    
    blockContent = property(__blockContent.value, __blockContent.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}collectionURI uses Python identifier collectionURI
    __collectionURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collectionURI'), 'collectionURI', '__httpkomadu_d2i_indiana_eduquery_entityDetail_httpkomadu_d2i_indiana_eduquerycollectionURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 327, 16), )

    
    collectionURI = property(__collectionURI.value, __collectionURI.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu/query}membership uses Python identifier membership
    __membership = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'membership'), 'membership', '__httpkomadu_d2i_indiana_eduquery_entityDetail_httpkomadu_d2i_indiana_eduquerymembership', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 329, 20), )

    
    membership = property(__membership.value, __membership.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpkomadu_d2i_indiana_eduquery_entityDetail_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 334, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 334, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __fileURI.name() : __fileURI,
        __owner.name() : __owner,
        __creationDate.name() : __creationDate,
        __size.name() : __size,
        __md5.name() : __md5,
        __fileName.name() : __fileName,
        __blockContent.name() : __blockContent,
        __collectionURI.name() : __collectionURI,
        __membership.name() : __membership
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.entityDetail = entityDetail
Namespace.addCategoryObject('typeBinding', 'entityDetail', entityDetail)


# Complex type {http://komadu.d2i.indiana.edu/query}membershipDetail with content type ELEMENT_ONLY
class membershipDetail (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu/query}membershipDetail with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'membershipDetail')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 336, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu/query}entityType uses Python identifier entityType
    __entityType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityType'), 'entityType', '__httpkomadu_d2i_indiana_eduquery_membershipDetail_httpkomadu_d2i_indiana_eduqueryentityType', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 338, 12), )

    
    entityType = property(__entityType.value, __entityType.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpkomadu_d2i_indiana_eduquery_membershipDetail_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 341, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 341, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __entityType.name() : __entityType
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.membershipDetail = membershipDetail
Namespace.addCategoryObject('typeBinding', 'membershipDetail', membershipDetail)


findActivityRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'findActivityRequest'), findActivityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 348, 4))
Namespace.addCategoryObject('elementBinding', findActivityRequest.name().localName(), findActivityRequest)

findActivityResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'findActivityResponse'), findActivityResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 349, 4))
Namespace.addCategoryObject('elementBinding', findActivityResponse.name().localName(), findActivityResponse)

getActivityDetailRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getActivityDetailRequest'), getActivityDetailRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 351, 4))
Namespace.addCategoryObject('elementBinding', getActivityDetailRequest.name().localName(), getActivityDetailRequest)

getActivityDetailResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getActivityDetailResponse'), getActivityDetailResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 352, 4))
Namespace.addCategoryObject('elementBinding', getActivityDetailResponse.name().localName(), getActivityDetailResponse)

findEntityRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'findEntityRequest'), findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 354, 4))
Namespace.addCategoryObject('elementBinding', findEntityRequest.name().localName(), findEntityRequest)

findEntityResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'findEntityResponse'), findEntityResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 355, 4))
Namespace.addCategoryObject('elementBinding', findEntityResponse.name().localName(), findEntityResponse)

getEntityDetailRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getEntityDetailRequest'), getEntityDetailRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 357, 4))
Namespace.addCategoryObject('elementBinding', getEntityDetailRequest.name().localName(), getEntityDetailRequest)

getEntityDetailResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getEntityDetailResponse'), getEntityDetailResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 358, 4))
Namespace.addCategoryObject('elementBinding', getEntityDetailResponse.name().localName(), getEntityDetailResponse)

getContextWorkflowGraphRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getContextWorkflowGraphRequest'), getContextWorkflowGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 360, 4))
Namespace.addCategoryObject('elementBinding', getContextWorkflowGraphRequest.name().localName(), getContextWorkflowGraphRequest)

getContextWorkflowGraphResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getContextWorkflowGraphResponse'), getContextWorkflowGraphResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 361, 4))
Namespace.addCategoryObject('elementBinding', getContextWorkflowGraphResponse.name().localName(), getContextWorkflowGraphResponse)

getActivityGraphRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getActivityGraphRequest'), getActivityGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 363, 4))
Namespace.addCategoryObject('elementBinding', getActivityGraphRequest.name().localName(), getActivityGraphRequest)

getActivityGraphResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getActivityGraphResponse'), getActivityGraphResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 364, 4))
Namespace.addCategoryObject('elementBinding', getActivityGraphResponse.name().localName(), getActivityGraphResponse)

getEntityGraphRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getEntityGraphRequest'), getEntityGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 366, 4))
Namespace.addCategoryObject('elementBinding', getEntityGraphRequest.name().localName(), getEntityGraphRequest)

getEntityGraphResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getEntityGraphResponse'), getEntityGraphResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 367, 4))
Namespace.addCategoryObject('elementBinding', getEntityGraphResponse.name().localName(), getEntityGraphResponse)

getEntityForwardGraphRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getEntityForwardGraphRequest'), getEntityGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 369, 4))
Namespace.addCategoryObject('elementBinding', getEntityForwardGraphRequest.name().localName(), getEntityForwardGraphRequest)

getEntityForwardGraphResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getEntityForwardGraphResponse'), getEntityGraphResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 370, 4))
Namespace.addCategoryObject('elementBinding', getEntityForwardGraphResponse.name().localName(), getEntityForwardGraphResponse)

getEntityBackwardGraphRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getEntityBackwardGraphRequest'), getEntityGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 372, 4))
Namespace.addCategoryObject('elementBinding', getEntityBackwardGraphRequest.name().localName(), getEntityBackwardGraphRequest)

getEntityBackwardGraphResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getEntityBackwardGraphResponse'), getEntityGraphResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 373, 4))
Namespace.addCategoryObject('elementBinding', getEntityBackwardGraphResponse.name().localName(), getEntityBackwardGraphResponse)

getAgentGraphRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getAgentGraphRequest'), getAgentGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 375, 4))
Namespace.addCategoryObject('elementBinding', getAgentGraphRequest.name().localName(), getAgentGraphRequest)

getAgentGraphResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'getAgentGraphResponse'), getAgentGraphResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 376, 4))
Namespace.addCategoryObject('elementBinding', getAgentGraphResponse.name().localName(), getAgentGraphResponse)



getActivityDetailRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uniqueURIList'), uniqueURIListType, scope=getActivityDetailRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 59, 16)))

getActivityDetailRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uniqueIDList'), uniqueIDListType, scope=getActivityDetailRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 62, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getActivityDetailRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uniqueURIList')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 59, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getActivityDetailRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uniqueIDList')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 62, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getActivityDetailRequestType._Automaton = _BuildAutomaton()




getActivityDetailResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityDetailList'), activityDetailListType, scope=getActivityDetailResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 69, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getActivityDetailResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityDetailList')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 69, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getActivityDetailResponseType._Automaton = _BuildAutomaton_()




getEntityDetailRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityIDList'), entityIDListType, scope=getEntityDetailRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 75, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getEntityDetailRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityIDList')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 75, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getEntityDetailRequestType._Automaton = _BuildAutomaton_2()




getEntityDetailResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityDetailList'), entityDetailListType, scope=getEntityDetailResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 81, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getEntityDetailResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityDetailList')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 81, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getEntityDetailResponseType._Automaton = _BuildAutomaton_3()




findEntityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'blockName'), pyxb.binding.datatypes.string, scope=findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 89, 20)))

findEntityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'blockContent'), pyxb.binding.datatypes.string, scope=findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 90, 20)))

findEntityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'blockMD5Checksum'), pyxb.binding.datatypes.string, scope=findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 91, 20)))

findEntityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'blockSize'), pyxb.binding.datatypes.long, scope=findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 92, 20)))

findEntityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileName'), pyxb.binding.datatypes.string, scope=findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 95, 20)))

findEntityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileURI'), pyxb.binding.datatypes.string, scope=findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 96, 20)))

findEntityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileOwnerID'), pyxb.binding.datatypes.string, scope=findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 97, 20)))

findEntityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileCreationDate'), pyxb.binding.datatypes.dateTime, scope=findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 98, 20)))

findEntityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileMD5Checksum'), pyxb.binding.datatypes.string, scope=findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 99, 20)))

findEntityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileSize'), pyxb.binding.datatypes.long, scope=findEntityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 100, 20)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 89, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 90, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 91, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 92, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 95, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 96, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 97, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 98, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 99, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 100, 20))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(findEntityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'blockName')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 89, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(findEntityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'blockContent')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 90, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(findEntityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'blockMD5Checksum')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 91, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(findEntityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'blockSize')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 92, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(findEntityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileName')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 95, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(findEntityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 96, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(findEntityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileOwnerID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 97, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(findEntityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileCreationDate')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 98, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(findEntityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileMD5Checksum')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 99, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(findEntityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileSize')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 100, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
findEntityRequestType._Automaton = _BuildAutomaton_4()




findEntityResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uniqueBlockIDList'), uniqueIDListType, scope=findEntityResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 109, 16)))

findEntityResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uniqueFileURIList'), uniqueFileListType, scope=findEntityResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 112, 16)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(findEntityResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uniqueBlockIDList')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 109, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(findEntityResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uniqueFileURIList')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 112, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
findEntityResponseType._Automaton = _BuildAutomaton_5()




findActivityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=findActivityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 119, 12)))

findActivityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hostName'), pyxb.binding.datatypes.string, scope=findActivityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 120, 12)))

findActivityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'architecture'), pyxb.binding.datatypes.string, scope=findActivityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 121, 12)))

findActivityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'workflowID'), pyxb.binding.datatypes.string, scope=findActivityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 126, 12)))

findActivityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceID'), pyxb.binding.datatypes.string, scope=findActivityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 127, 12)))

findActivityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nextActivityID'), pyxb.binding.datatypes.string, scope=findActivityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 128, 12)))

findActivityRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributeList'), _ImportedBinding__komadu.attributesType, scope=findActivityRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 129, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 119, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(findActivityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 119, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 120, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(findActivityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hostName')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 120, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 121, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(findActivityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'architecture')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 121, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 126, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(findActivityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'workflowID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 126, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 127, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(findActivityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 127, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 128, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(findActivityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nextActivityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 128, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 129, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(findActivityRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributeList')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 129, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 119, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 120, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 121, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 126, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 127, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 128, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 129, 12))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_7())
    sub_automata.append(_BuildAutomaton_8())
    sub_automata.append(_BuildAutomaton_9())
    sub_automata.append(_BuildAutomaton_10())
    sub_automata.append(_BuildAutomaton_11())
    sub_automata.append(_BuildAutomaton_12())
    sub_automata.append(_BuildAutomaton_13())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 118, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
findActivityRequestType._Automaton = _BuildAutomaton_6()




findActivityResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uniqueURIList'), uniqueURIListType, scope=findActivityResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 136, 16)))

findActivityResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityIDList'), activityIDListType, scope=findActivityResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 139, 16)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(findActivityResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uniqueURIList')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 136, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(findActivityResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityIDList')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 139, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
findActivityResponseType._Automaton = _BuildAutomaton_14()




getContextWorkflowGraphRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contextWorkflowURI'), pyxb.binding.datatypes.string, scope=getContextWorkflowGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 146, 12)))

getContextWorkflowGraphRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel'), detailEnumType, scope=getContextWorkflowGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 147, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getContextWorkflowGraphRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contextWorkflowURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 146, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 147, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(getContextWorkflowGraphRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 147, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 147, 12))
    counters.add(cc_0)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_16())
    sub_automata.append(_BuildAutomaton_17())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 145, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getContextWorkflowGraphRequestType._Automaton = _BuildAutomaton_15()




getContextWorkflowGraphResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_prov, 'document'), _ImportedBinding__prov.Document, scope=getContextWorkflowGraphResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/prov-20130307.xsd', 648, 2)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getContextWorkflowGraphResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_prov, 'document')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 153, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getContextWorkflowGraphResponseType._Automaton = _BuildAutomaton_18()




getActivityGraphRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityURI'), pyxb.binding.datatypes.string, scope=getActivityGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 159, 12)))

getActivityGraphRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel'), detailEnumType, scope=getActivityGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 160, 12)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getActivityGraphRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 159, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 160, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(getActivityGraphRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 160, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 160, 12))
    counters.add(cc_0)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_20())
    sub_automata.append(_BuildAutomaton_21())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 158, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getActivityGraphRequestType._Automaton = _BuildAutomaton_19()




getActivityGraphResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_prov, 'document'), _ImportedBinding__prov.Document, scope=getActivityGraphResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/prov-20130307.xsd', 648, 2)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getActivityGraphResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_prov, 'document')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 166, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getActivityGraphResponseType._Automaton = _BuildAutomaton_22()




getEntityGraphRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityURI'), pyxb.binding.datatypes.string, scope=getEntityGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 172, 12)))

getEntityGraphRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityType'), entityEnumType, scope=getEntityGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 173, 12)))

getEntityGraphRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel'), detailEnumType, scope=getEntityGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 174, 12)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getEntityGraphRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 172, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getEntityGraphRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityType')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 174, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(getEntityGraphRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 174, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 174, 12))
    counters.add(cc_0)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_24())
    sub_automata.append(_BuildAutomaton_25())
    sub_automata.append(_BuildAutomaton_26())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 171, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getEntityGraphRequestType._Automaton = _BuildAutomaton_23()




getEntityGraphResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_prov, 'document'), _ImportedBinding__prov.Document, scope=getEntityGraphResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/prov-20130307.xsd', 648, 2)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getEntityGraphResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_prov, 'document')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 180, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getEntityGraphResponseType._Automaton = _BuildAutomaton_27()




getAgentGraphRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agentID'), pyxb.binding.datatypes.string, scope=getAgentGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 186, 12)))

getAgentGraphRequestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel'), detailEnumType, scope=getAgentGraphRequestType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 187, 12)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getAgentGraphRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 186, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 187, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(getAgentGraphRequestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'informationDetailLevel')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 187, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 187, 12))
    counters.add(cc_0)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_29())
    sub_automata.append(_BuildAutomaton_30())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 185, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getAgentGraphRequestType._Automaton = _BuildAutomaton_28()




getAgentGraphResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_prov, 'document'), _ImportedBinding__prov.Document, scope=getAgentGraphResponseType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/prov-20130307.xsd', 648, 2)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(getAgentGraphResponseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_prov, 'document')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 193, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
getAgentGraphResponseType._Automaton = _BuildAutomaton_31()




activityDetailListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityDetail'), activityDetail, scope=activityDetailListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 199, 12)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 199, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityDetailListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityDetail')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 199, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
activityDetailListType._Automaton = _BuildAutomaton_32()




activityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), pyxb.binding.datatypes.string, scope=activityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 206, 12)))

activityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'workflowID'), pyxb.binding.datatypes.string, scope=activityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 207, 12)))

activityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceID'), pyxb.binding.datatypes.string, scope=activityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 208, 12)))

activityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timestep'), pyxb.binding.datatypes.int, scope=activityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 209, 12)))

activityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'workflowNodeID'), pyxb.binding.datatypes.string, scope=activityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 210, 12)))

activityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'instanceOf'), pyxb.binding.datatypes.string, scope=activityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 211, 12)))

activityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), _ImportedBinding__komadu.attributesType, scope=activityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 212, 12)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 206, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 207, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'workflowID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 207, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 208, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 208, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 209, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestep')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 209, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 210, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'workflowNodeID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 210, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 211, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instanceOf')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 211, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 212, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 212, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 207, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 208, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 209, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 210, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 211, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 212, 12))
    counters.add(cc_5)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_34())
    sub_automata.append(_BuildAutomaton_35())
    sub_automata.append(_BuildAutomaton_36())
    sub_automata.append(_BuildAutomaton_37())
    sub_automata.append(_BuildAutomaton_38())
    sub_automata.append(_BuildAutomaton_39())
    sub_automata.append(_BuildAutomaton_40())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 205, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
activityDetail._Automaton = _BuildAutomaton_33()




uniqueURIListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uniqueURI'), pyxb.binding.datatypes.anyURI, scope=uniqueURIListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 222, 12)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 222, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(uniqueURIListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uniqueURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 222, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
uniqueURIListType._Automaton = _BuildAutomaton_41()




activityIDListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityID'), pyxb.binding.datatypes.string, scope=activityIDListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 227, 12)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 227, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityIDListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 227, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
activityIDListType._Automaton = _BuildAutomaton_42()




uniqueIDListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uniqueID'), pyxb.binding.datatypes.string, scope=uniqueIDListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 232, 12)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 232, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(uniqueIDListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uniqueID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 232, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
uniqueIDListType._Automaton = _BuildAutomaton_43()




abstractServiceDetailListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'abstractServiceDetail'), abstractServiceDetail, scope=abstractServiceDetailListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 238, 12)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 238, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(abstractServiceDetailListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'abstractServiceDetail')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 238, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
abstractServiceDetailListType._Automaton = _BuildAutomaton_44()




abstractServiceDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), pyxb.binding.datatypes.string, scope=abstractServiceDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 244, 12)))

abstractServiceDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=abstractServiceDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 246, 12)))

abstractServiceDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'version'), pyxb.binding.datatypes.string, scope=abstractServiceDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 247, 12)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(abstractServiceDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 244, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 246, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(abstractServiceDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 246, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 247, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(abstractServiceDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'version')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 247, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 246, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 247, 12))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_46())
    sub_automata.append(_BuildAutomaton_47())
    sub_automata.append(_BuildAutomaton_48())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 243, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
abstractServiceDetail._Automaton = _BuildAutomaton_45()




methodNameListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'methodName'), pyxb.binding.datatypes.string, scope=methodNameListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 254, 12)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 254, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(methodNameListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'methodName')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 254, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
methodNameListType._Automaton = _BuildAutomaton_49()




abstractMethodListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'abstractMethod'), pyxb.binding.datatypes.string, scope=abstractMethodListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 260, 12)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 260, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(abstractMethodListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'abstractMethod')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 260, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
abstractMethodListType._Automaton = _BuildAutomaton_50()




entityNameListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityName'), pyxb.binding.datatypes.string, scope=entityNameListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 266, 12)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityNameListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityName')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 266, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
entityNameListType._Automaton = _BuildAutomaton_51()




entityTypeListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityType'), entityEnumType, scope=entityTypeListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 271, 12)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityTypeListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityType')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 271, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
entityTypeListType._Automaton = _BuildAutomaton_52()




entityIDListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityID'), pyxb.binding.datatypes.string, scope=entityIDListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 276, 12)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityIDListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 276, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
entityIDListType._Automaton = _BuildAutomaton_53()




abstractEntityListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'abstractEntityDetail'), abstractEntityDetail, scope=abstractEntityListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 281, 12)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 281, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(abstractEntityListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'abstractEntityDetail')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 281, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
abstractEntityListType._Automaton = _BuildAutomaton_54()




abstractEntityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=abstractEntityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 287, 12)))

abstractEntityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), pyxb.binding.datatypes.string, scope=abstractEntityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 288, 12)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(abstractEntityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 287, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(abstractEntityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 288, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
abstractEntityDetail._Automaton = _BuildAutomaton_55()




uniqueFileListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileURIDetailsType'), fileURIDetailsType, scope=uniqueFileListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 294, 12)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 294, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(uniqueFileListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileURIDetailsType')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 294, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
uniqueFileListType._Automaton = _BuildAutomaton_56()




fileURIDetailsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileID'), pyxb.binding.datatypes.string, scope=fileURIDetailsType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 300, 12)))

fileURIDetailsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileURI'), pyxb.binding.datatypes.string, scope=fileURIDetailsType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 301, 12)))

fileURIDetailsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creationDate'), pyxb.binding.datatypes.dateTime, scope=fileURIDetailsType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 302, 12)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 302, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileURIDetailsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 300, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fileURIDetailsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 301, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(fileURIDetailsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creationDate')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 302, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
fileURIDetailsType._Automaton = _BuildAutomaton_57()




entityDetailListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityDetail'), entityDetail, scope=entityDetailListType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 307, 12)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 307, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(entityDetailListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityDetail')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 307, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
entityDetailListType._Automaton = _BuildAutomaton_58()




entityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileURI'), pyxb.binding.datatypes.anyURI, scope=entityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 314, 16)))

entityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'owner'), pyxb.binding.datatypes.string, scope=entityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 315, 16)))

entityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creationDate'), pyxb.binding.datatypes.dateTime, scope=entityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 316, 16)))

entityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'size'), pyxb.binding.datatypes.long, scope=entityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 317, 16)))

entityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'md5'), pyxb.binding.datatypes.string, scope=entityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 318, 16)))

entityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileName'), pyxb.binding.datatypes.string, scope=entityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 319, 16)))

entityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'blockContent'), pyxb.binding.datatypes.string, scope=entityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 322, 16)))

entityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collectionURI'), pyxb.binding.datatypes.string, scope=entityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 327, 16)))

entityDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'membership'), membershipDetail, scope=entityDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 329, 20)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 315, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 316, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 317, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 318, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 319, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 323, 16))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 324, 16))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 329, 20))
    counters.add(cc_7)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 314, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'owner')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 315, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creationDate')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 316, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'size')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 317, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'md5')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 318, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileName')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 319, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'blockContent')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 322, 16))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'size')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 323, 16))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'md5')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 324, 16))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collectionURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 327, 16))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(entityDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'membership')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 329, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
entityDetail._Automaton = _BuildAutomaton_59()




membershipDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityType'), entityEnumType, scope=membershipDetail, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 338, 12)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(membershipDetail._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityType')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_query_schema.xsd', 338, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
membershipDetail._Automaton = _BuildAutomaton_60()

