# ./_komadu.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:de1c4da9fc36045550ca5feec2f59288315d6785
# Generated 2019-06-19 16:51:10.392499 by PyXB version 1.2.6 using Python 3.7.0.final.0
# Namespace http://komadu.d2i.indiana.edu [xmlns:komadu]

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

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://komadu.d2i.indiana.edu', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://komadu.d2i.indiana.edu}agentEnumType
class agentEnumType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'agentEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 73, 4)
    _Documentation = None
agentEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=agentEnumType, enum_prefix=None)
agentEnumType.PERSON = agentEnumType._CF_enumeration.addEnumeration(unicode_value='PERSON', tag='PERSON')
agentEnumType.ORGANIZATION = agentEnumType._CF_enumeration.addEnumeration(unicode_value='ORGANIZATION', tag='ORGANIZATION')
agentEnumType.SOFTWARE = agentEnumType._CF_enumeration.addEnumeration(unicode_value='SOFTWARE', tag='SOFTWARE')
agentEnumType.OTHER = agentEnumType._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
agentEnumType._InitializeFacetMap(agentEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'agentEnumType', agentEnumType)
_module_typeBindings.agentEnumType = agentEnumType

# Atomic simple type: {http://komadu.d2i.indiana.edu}entityEnumType
class entityEnumType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entityEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 84, 4)
    _Documentation = None
entityEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=entityEnumType, enum_prefix=None)
entityEnumType.FILE = entityEnumType._CF_enumeration.addEnumeration(unicode_value='FILE', tag='FILE')
entityEnumType.BLOCK = entityEnumType._CF_enumeration.addEnumeration(unicode_value='BLOCK', tag='BLOCK')
entityEnumType.COLLECTION = entityEnumType._CF_enumeration.addEnumeration(unicode_value='COLLECTION', tag='COLLECTION')
entityEnumType.GENERIC = entityEnumType._CF_enumeration.addEnumeration(unicode_value='GENERIC', tag='GENERIC')
entityEnumType._InitializeFacetMap(entityEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'entityEnumType', entityEnumType)
_module_typeBindings.entityEnumType = entityEnumType

# Atomic simple type: {http://komadu.d2i.indiana.edu}objectEnumType
class objectEnumType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'objectEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 93, 4)
    _Documentation = None
objectEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=objectEnumType, enum_prefix=None)
objectEnumType.AGENT = objectEnumType._CF_enumeration.addEnumeration(unicode_value='AGENT', tag='AGENT')
objectEnumType.ACTIVITY = objectEnumType._CF_enumeration.addEnumeration(unicode_value='ACTIVITY', tag='ACTIVITY')
objectEnumType.ENTITY = objectEnumType._CF_enumeration.addEnumeration(unicode_value='ENTITY', tag='ENTITY')
objectEnumType._InitializeFacetMap(objectEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'objectEnumType', objectEnumType)
_module_typeBindings.objectEnumType = objectEnumType

# Complex type {http://komadu.d2i.indiana.edu}agentType with content type ELEMENT_ONLY
class agentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}agentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'agentType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 39, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}userAgent uses Python identifier userAgent
    __userAgent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'userAgent'), 'userAgent', '__httpkomadu_d2i_indiana_edu_agentType_httpkomadu_d2i_indiana_eduuserAgent', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 43, 16), )

    
    userAgent = property(__userAgent.value, __userAgent.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}genericAgent uses Python identifier genericAgent
    __genericAgent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genericAgent'), 'genericAgent', '__httpkomadu_d2i_indiana_edu_agentType_httpkomadu_d2i_indiana_edugenericAgent', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 45, 16), )

    
    genericAgent = property(__genericAgent.value, __genericAgent.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__httpkomadu_d2i_indiana_edu_agentType_httpkomadu_d2i_indiana_edutype', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 47, 12), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'role'), 'role', '__httpkomadu_d2i_indiana_edu_agentType_httpkomadu_d2i_indiana_edurole', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 49, 12), )

    
    role = property(__role.value, __role.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__httpkomadu_d2i_indiana_edu_agentType_httpkomadu_d2i_indiana_edulocation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 50, 12), )

    
    location = property(__location.value, __location.set, None, None)

    _ElementMap.update({
        __userAgent.name() : __userAgent,
        __genericAgent.name() : __genericAgent,
        __type.name() : __type,
        __role.name() : __role,
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.agentType = agentType
Namespace.addCategoryObject('typeBinding', 'agentType', agentType)


# Complex type {http://komadu.d2i.indiana.edu}genericAgentType with content type ELEMENT_ONLY
class genericAgentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}genericAgentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genericAgentType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 54, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}agentID uses Python identifier agentID
    __agentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agentID'), 'agentID', '__httpkomadu_d2i_indiana_edu_genericAgentType_httpkomadu_d2i_indiana_eduagentID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 56, 12), )

    
    agentID = property(__agentID.value, __agentID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_genericAgentType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 57, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    _ElementMap.update({
        __agentID.name() : __agentID,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.genericAgentType = genericAgentType
Namespace.addCategoryObject('typeBinding', 'genericAgentType', genericAgentType)


# Complex type {http://komadu.d2i.indiana.edu}activityType with content type ELEMENT_ONLY
class activityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}activityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'activityType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 101, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}workflowInformation uses Python identifier workflowInformation
    __workflowInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'workflowInformation'), 'workflowInformation', '__httpkomadu_d2i_indiana_edu_activityType_httpkomadu_d2i_indiana_eduworkflowInformation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 105, 16), )

    
    workflowInformation = property(__workflowInformation.value, __workflowInformation.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}serviceInformation uses Python identifier serviceInformation
    __serviceInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serviceInformation'), 'serviceInformation', '__httpkomadu_d2i_indiana_edu_activityType_httpkomadu_d2i_indiana_eduserviceInformation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 106, 16), )

    
    serviceInformation = property(__serviceInformation.value, __serviceInformation.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}methodInformation uses Python identifier methodInformation
    __methodInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'methodInformation'), 'methodInformation', '__httpkomadu_d2i_indiana_edu_activityType_httpkomadu_d2i_indiana_edumethodInformation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 107, 16), )

    
    methodInformation = property(__methodInformation.value, __methodInformation.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}activityInformation uses Python identifier activityInformation
    __activityInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityInformation'), 'activityInformation', '__httpkomadu_d2i_indiana_edu_activityType_httpkomadu_d2i_indiana_eduactivityInformation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 109, 16), )

    
    activityInformation = property(__activityInformation.value, __activityInformation.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__httpkomadu_d2i_indiana_edu_activityType_httpkomadu_d2i_indiana_edulocation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 111, 12), )

    
    location = property(__location.value, __location.set, None, None)

    _ElementMap.update({
        __workflowInformation.name() : __workflowInformation,
        __serviceInformation.name() : __serviceInformation,
        __methodInformation.name() : __methodInformation,
        __activityInformation.name() : __activityInformation,
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.activityType = activityType
Namespace.addCategoryObject('typeBinding', 'activityType', activityType)


# Complex type {http://komadu.d2i.indiana.edu}workflowInformationType with content type ELEMENT_ONLY
class workflowInformationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}workflowInformationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'workflowInformationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 115, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}workflowID uses Python identifier workflowID
    __workflowID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'workflowID'), 'workflowID', '__httpkomadu_d2i_indiana_edu_workflowInformationType_httpkomadu_d2i_indiana_eduworkflowID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 117, 12), )

    
    workflowID = property(__workflowID.value, __workflowID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}workflowNodeID uses Python identifier workflowNodeID
    __workflowNodeID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'workflowNodeID'), 'workflowNodeID', '__httpkomadu_d2i_indiana_edu_workflowInformationType_httpkomadu_d2i_indiana_eduworkflowNodeID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 118, 12), )

    
    workflowNodeID = property(__workflowNodeID.value, __workflowNodeID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}timestep uses Python identifier timestep
    __timestep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timestep'), 'timestep', '__httpkomadu_d2i_indiana_edu_workflowInformationType_httpkomadu_d2i_indiana_edutimestep', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 119, 12), )

    
    timestep = property(__timestep.value, __timestep.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_workflowInformationType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 120, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}instanceOf uses Python identifier instanceOf
    __instanceOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'instanceOf'), 'instanceOf', '__httpkomadu_d2i_indiana_edu_workflowInformationType_httpkomadu_d2i_indiana_eduinstanceOf', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 121, 12), )

    
    instanceOf = property(__instanceOf.value, __instanceOf.set, None, None)

    _ElementMap.update({
        __workflowID.name() : __workflowID,
        __workflowNodeID.name() : __workflowNodeID,
        __timestep.name() : __timestep,
        __attributes.name() : __attributes,
        __instanceOf.name() : __instanceOf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.workflowInformationType = workflowInformationType
Namespace.addCategoryObject('typeBinding', 'workflowInformationType', workflowInformationType)


# Complex type {http://komadu.d2i.indiana.edu}instanceOfType with content type ELEMENT_ONLY
class instanceOfType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}instanceOfType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'instanceOfType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 145, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}instanceOfID uses Python identifier instanceOfID
    __instanceOfID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'instanceOfID'), 'instanceOfID', '__httpkomadu_d2i_indiana_edu_instanceOfType_httpkomadu_d2i_indiana_eduinstanceOfID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 147, 12), )

    
    instanceOfID = property(__instanceOfID.value, __instanceOfID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'version'), 'version', '__httpkomadu_d2i_indiana_edu_instanceOfType_httpkomadu_d2i_indiana_eduversion', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 148, 12), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creationTime'), 'creationTime', '__httpkomadu_d2i_indiana_edu_instanceOfType_httpkomadu_d2i_indiana_educreationTime', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 149, 12), )

    
    creationTime = property(__creationTime.value, __creationTime.set, None, None)

    _ElementMap.update({
        __instanceOfID.name() : __instanceOfID,
        __version.name() : __version,
        __creationTime.name() : __creationTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.instanceOfType = instanceOfType
Namespace.addCategoryObject('typeBinding', 'instanceOfType', instanceOfType)


# Complex type {http://komadu.d2i.indiana.edu}entityType with content type ELEMENT_ONLY
class entityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}entityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entityType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 153, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'file'), 'file', '__httpkomadu_d2i_indiana_edu_entityType_httpkomadu_d2i_indiana_edufile', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 157, 16), )

    
    file = property(__file.value, __file.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}block uses Python identifier block
    __block = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'block'), 'block', '__httpkomadu_d2i_indiana_edu_entityType_httpkomadu_d2i_indiana_edublock', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 158, 16), )

    
    block = property(__block.value, __block.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}collection uses Python identifier collection
    __collection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collection'), 'collection', '__httpkomadu_d2i_indiana_edu_entityType_httpkomadu_d2i_indiana_educollection', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 159, 16), )

    
    collection = property(__collection.value, __collection.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}genericEntity uses Python identifier genericEntity
    __genericEntity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genericEntity'), 'genericEntity', '__httpkomadu_d2i_indiana_edu_entityType_httpkomadu_d2i_indiana_edugenericEntity', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 160, 16), )

    
    genericEntity = property(__genericEntity.value, __genericEntity.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_entityType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 163, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'role'), 'role', '__httpkomadu_d2i_indiana_edu_entityType_httpkomadu_d2i_indiana_edurole', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 165, 12), )

    
    role = property(__role.value, __role.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__httpkomadu_d2i_indiana_edu_entityType_httpkomadu_d2i_indiana_edulocation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 166, 12), )

    
    location = property(__location.value, __location.set, None, None)

    _ElementMap.update({
        __file.name() : __file,
        __block.name() : __block,
        __collection.name() : __collection,
        __genericEntity.name() : __genericEntity,
        __attributes.name() : __attributes,
        __role.name() : __role,
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.entityType = entityType
Namespace.addCategoryObject('typeBinding', 'entityType', entityType)


# Complex type {http://komadu.d2i.indiana.edu}fileType with content type ELEMENT_ONLY
class fileType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}fileType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fileType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 170, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}fileURI uses Python identifier fileURI
    __fileURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileURI'), 'fileURI', '__httpkomadu_d2i_indiana_edu_fileType_httpkomadu_d2i_indiana_edufileURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 172, 12), )

    
    fileURI = property(__fileURI.value, __fileURI.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}ownerDN uses Python identifier ownerDN
    __ownerDN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ownerDN'), 'ownerDN', '__httpkomadu_d2i_indiana_edu_fileType_httpkomadu_d2i_indiana_eduownerDN', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 173, 12), )

    
    ownerDN = property(__ownerDN.value, __ownerDN.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}createDate uses Python identifier createDate
    __createDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'createDate'), 'createDate', '__httpkomadu_d2i_indiana_edu_fileType_httpkomadu_d2i_indiana_educreateDate', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 174, 12), )

    
    createDate = property(__createDate.value, __createDate.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'size'), 'size', '__httpkomadu_d2i_indiana_edu_fileType_httpkomadu_d2i_indiana_edusize', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 175, 12), )

    
    size = property(__size.value, __size.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}md5sum uses Python identifier md5sum
    __md5sum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'md5sum'), 'md5sum', '__httpkomadu_d2i_indiana_edu_fileType_httpkomadu_d2i_indiana_edumd5sum', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 176, 12), )

    
    md5sum = property(__md5sum.value, __md5sum.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}fileName uses Python identifier fileName
    __fileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fileName'), 'fileName', '__httpkomadu_d2i_indiana_edu_fileType_httpkomadu_d2i_indiana_edufileName', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 177, 12), )

    
    fileName = property(__fileName.value, __fileName.set, None, None)

    _ElementMap.update({
        __fileURI.name() : __fileURI,
        __ownerDN.name() : __ownerDN,
        __createDate.name() : __createDate,
        __size.name() : __size,
        __md5sum.name() : __md5sum,
        __fileName.name() : __fileName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.fileType = fileType
Namespace.addCategoryObject('typeBinding', 'fileType', fileType)


# Complex type {http://komadu.d2i.indiana.edu}blockType with content type ELEMENT_ONLY
class blockType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}blockType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'blockType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 181, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}blockURI uses Python identifier blockURI
    __blockURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'blockURI'), 'blockURI', '__httpkomadu_d2i_indiana_edu_blockType_httpkomadu_d2i_indiana_edublockURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 183, 12), )

    
    blockURI = property(__blockURI.value, __blockURI.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}blockContent uses Python identifier blockContent
    __blockContent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'blockContent'), 'blockContent', '__httpkomadu_d2i_indiana_edu_blockType_httpkomadu_d2i_indiana_edublockContent', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 184, 12), )

    
    blockContent = property(__blockContent.value, __blockContent.set, None, None)

    _ElementMap.update({
        __blockURI.name() : __blockURI,
        __blockContent.name() : __blockContent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.blockType = blockType
Namespace.addCategoryObject('typeBinding', 'blockType', blockType)


# Complex type {http://komadu.d2i.indiana.edu}collectionType with content type ELEMENT_ONLY
class collectionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}collectionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'collectionType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 188, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}collectionURI uses Python identifier collectionURI
    __collectionURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collectionURI'), 'collectionURI', '__httpkomadu_d2i_indiana_edu_collectionType_httpkomadu_d2i_indiana_educollectionURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 190, 12), )

    
    collectionURI = property(__collectionURI.value, __collectionURI.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}members uses Python identifier members
    __members = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'members'), 'members', '__httpkomadu_d2i_indiana_edu_collectionType_httpkomadu_d2i_indiana_edumembers', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 192, 12), )

    
    members = property(__members.value, __members.set, None, None)

    _ElementMap.update({
        __collectionURI.name() : __collectionURI,
        __members.name() : __members
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.collectionType = collectionType
Namespace.addCategoryObject('typeBinding', 'collectionType', collectionType)


# Complex type {http://komadu.d2i.indiana.edu}genericEntityType with content type ELEMENT_ONLY
class genericEntityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}genericEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genericEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 196, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}entityURI uses Python identifier entityURI
    __entityURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityURI'), 'entityURI', '__httpkomadu_d2i_indiana_edu_genericEntityType_httpkomadu_d2i_indiana_eduentityURI', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 198, 12), )

    
    entityURI = property(__entityURI.value, __entityURI.set, None, None)

    _ElementMap.update({
        __entityURI.name() : __entityURI
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.genericEntityType = genericEntityType
Namespace.addCategoryObject('typeBinding', 'genericEntityType', genericEntityType)


# Complex type {http://komadu.d2i.indiana.edu}generationType with content type ELEMENT_ONLY
class generationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}generationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'generationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 202, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}activityID uses Python identifier activityID
    __activityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityID'), 'activityID', '__httpkomadu_d2i_indiana_edu_generationType_httpkomadu_d2i_indiana_eduactivityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 204, 12), )

    
    activityID = property(__activityID.value, __activityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}entityID uses Python identifier entityID
    __entityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityID'), 'entityID', '__httpkomadu_d2i_indiana_edu_generationType_httpkomadu_d2i_indiana_eduentityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 205, 12), )

    
    entityID = property(__entityID.value, __entityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), 'timestamp', '__httpkomadu_d2i_indiana_edu_generationType_httpkomadu_d2i_indiana_edutimestamp', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 206, 12), )

    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_generationType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 207, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__httpkomadu_d2i_indiana_edu_generationType_httpkomadu_d2i_indiana_edulocation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 208, 12), )

    
    location = property(__location.value, __location.set, None, None)

    _ElementMap.update({
        __activityID.name() : __activityID,
        __entityID.name() : __entityID,
        __timestamp.name() : __timestamp,
        __attributes.name() : __attributes,
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.generationType = generationType
Namespace.addCategoryObject('typeBinding', 'generationType', generationType)


# Complex type {http://komadu.d2i.indiana.edu}usageType with content type ELEMENT_ONLY
class usageType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}usageType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'usageType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 212, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}activityID uses Python identifier activityID
    __activityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityID'), 'activityID', '__httpkomadu_d2i_indiana_edu_usageType_httpkomadu_d2i_indiana_eduactivityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 214, 12), )

    
    activityID = property(__activityID.value, __activityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}entityID uses Python identifier entityID
    __entityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityID'), 'entityID', '__httpkomadu_d2i_indiana_edu_usageType_httpkomadu_d2i_indiana_eduentityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 215, 12), )

    
    entityID = property(__entityID.value, __entityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), 'timestamp', '__httpkomadu_d2i_indiana_edu_usageType_httpkomadu_d2i_indiana_edutimestamp', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 216, 12), )

    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_usageType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 217, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__httpkomadu_d2i_indiana_edu_usageType_httpkomadu_d2i_indiana_edulocation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 218, 12), )

    
    location = property(__location.value, __location.set, None, None)

    _ElementMap.update({
        __activityID.name() : __activityID,
        __entityID.name() : __entityID,
        __timestamp.name() : __timestamp,
        __attributes.name() : __attributes,
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.usageType = usageType
Namespace.addCategoryObject('typeBinding', 'usageType', usageType)


# Complex type {http://komadu.d2i.indiana.edu}startType with content type ELEMENT_ONLY
class startType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}startType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'startType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 222, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}activityID uses Python identifier activityID
    __activityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityID'), 'activityID', '__httpkomadu_d2i_indiana_edu_startType_httpkomadu_d2i_indiana_eduactivityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 224, 12), )

    
    activityID = property(__activityID.value, __activityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}triggerID uses Python identifier triggerID
    __triggerID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'triggerID'), 'triggerID', '__httpkomadu_d2i_indiana_edu_startType_httpkomadu_d2i_indiana_edutriggerID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 225, 12), )

    
    triggerID = property(__triggerID.value, __triggerID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), 'timestamp', '__httpkomadu_d2i_indiana_edu_startType_httpkomadu_d2i_indiana_edutimestamp', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 227, 12), )

    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_startType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 228, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__httpkomadu_d2i_indiana_edu_startType_httpkomadu_d2i_indiana_edulocation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 229, 12), )

    
    location = property(__location.value, __location.set, None, None)

    _ElementMap.update({
        __activityID.name() : __activityID,
        __triggerID.name() : __triggerID,
        __timestamp.name() : __timestamp,
        __attributes.name() : __attributes,
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.startType = startType
Namespace.addCategoryObject('typeBinding', 'startType', startType)


# Complex type {http://komadu.d2i.indiana.edu}endType with content type ELEMENT_ONLY
class endType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}endType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'endType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 233, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}activityID uses Python identifier activityID
    __activityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityID'), 'activityID', '__httpkomadu_d2i_indiana_edu_endType_httpkomadu_d2i_indiana_eduactivityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 235, 12), )

    
    activityID = property(__activityID.value, __activityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}triggerID uses Python identifier triggerID
    __triggerID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'triggerID'), 'triggerID', '__httpkomadu_d2i_indiana_edu_endType_httpkomadu_d2i_indiana_edutriggerID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 236, 12), )

    
    triggerID = property(__triggerID.value, __triggerID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), 'timestamp', '__httpkomadu_d2i_indiana_edu_endType_httpkomadu_d2i_indiana_edutimestamp', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 238, 12), )

    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_endType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 239, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__httpkomadu_d2i_indiana_edu_endType_httpkomadu_d2i_indiana_edulocation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 240, 12), )

    
    location = property(__location.value, __location.set, None, None)

    _ElementMap.update({
        __activityID.name() : __activityID,
        __triggerID.name() : __triggerID,
        __timestamp.name() : __timestamp,
        __attributes.name() : __attributes,
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.endType = endType
Namespace.addCategoryObject('typeBinding', 'endType', endType)


# Complex type {http://komadu.d2i.indiana.edu}invalidationType with content type ELEMENT_ONLY
class invalidationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}invalidationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'invalidationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 244, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}activityID uses Python identifier activityID
    __activityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityID'), 'activityID', '__httpkomadu_d2i_indiana_edu_invalidationType_httpkomadu_d2i_indiana_eduactivityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 246, 12), )

    
    activityID = property(__activityID.value, __activityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}entityID uses Python identifier entityID
    __entityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityID'), 'entityID', '__httpkomadu_d2i_indiana_edu_invalidationType_httpkomadu_d2i_indiana_eduentityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 247, 12), )

    
    entityID = property(__entityID.value, __entityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), 'timestamp', '__httpkomadu_d2i_indiana_edu_invalidationType_httpkomadu_d2i_indiana_edutimestamp', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 248, 12), )

    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_invalidationType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 249, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'location'), 'location', '__httpkomadu_d2i_indiana_edu_invalidationType_httpkomadu_d2i_indiana_edulocation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 250, 12), )

    
    location = property(__location.value, __location.set, None, None)

    _ElementMap.update({
        __activityID.name() : __activityID,
        __entityID.name() : __entityID,
        __timestamp.name() : __timestamp,
        __attributes.name() : __attributes,
        __location.name() : __location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.invalidationType = invalidationType
Namespace.addCategoryObject('typeBinding', 'invalidationType', invalidationType)


# Complex type {http://komadu.d2i.indiana.edu}communicationType with content type ELEMENT_ONLY
class communicationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}communicationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'communicationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 255, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}informedActivityID uses Python identifier informedActivityID
    __informedActivityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'informedActivityID'), 'informedActivityID', '__httpkomadu_d2i_indiana_edu_communicationType_httpkomadu_d2i_indiana_eduinformedActivityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 257, 12), )

    
    informedActivityID = property(__informedActivityID.value, __informedActivityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}informantActivityID uses Python identifier informantActivityID
    __informantActivityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'informantActivityID'), 'informantActivityID', '__httpkomadu_d2i_indiana_edu_communicationType_httpkomadu_d2i_indiana_eduinformantActivityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 258, 12), )

    
    informantActivityID = property(__informantActivityID.value, __informantActivityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_communicationType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 259, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    _ElementMap.update({
        __informedActivityID.name() : __informedActivityID,
        __informantActivityID.name() : __informantActivityID,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.communicationType = communicationType
Namespace.addCategoryObject('typeBinding', 'communicationType', communicationType)


# Complex type {http://komadu.d2i.indiana.edu}derivationType with content type ELEMENT_ONLY
class derivationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}derivationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'derivationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 263, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}usedEntityID uses Python identifier usedEntityID
    __usedEntityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usedEntityID'), 'usedEntityID', '__httpkomadu_d2i_indiana_edu_derivationType_httpkomadu_d2i_indiana_eduusedEntityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 265, 12), )

    
    usedEntityID = property(__usedEntityID.value, __usedEntityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}generatedEntityID uses Python identifier generatedEntityID
    __generatedEntityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'generatedEntityID'), 'generatedEntityID', '__httpkomadu_d2i_indiana_edu_derivationType_httpkomadu_d2i_indiana_edugeneratedEntityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 266, 12), )

    
    generatedEntityID = property(__generatedEntityID.value, __generatedEntityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_derivationType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 268, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    _ElementMap.update({
        __usedEntityID.name() : __usedEntityID,
        __generatedEntityID.name() : __generatedEntityID,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.derivationType = derivationType
Namespace.addCategoryObject('typeBinding', 'derivationType', derivationType)


# Complex type {http://komadu.d2i.indiana.edu}alternateType with content type ELEMENT_ONLY
class alternateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}alternateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'alternateType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 308, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}alternate1ID uses Python identifier alternate1ID
    __alternate1ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'alternate1ID'), 'alternate1ID', '__httpkomadu_d2i_indiana_edu_alternateType_httpkomadu_d2i_indiana_edualternate1ID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 310, 12), )

    
    alternate1ID = property(__alternate1ID.value, __alternate1ID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}alternate2ID uses Python identifier alternate2ID
    __alternate2ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'alternate2ID'), 'alternate2ID', '__httpkomadu_d2i_indiana_edu_alternateType_httpkomadu_d2i_indiana_edualternate2ID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 311, 12), )

    
    alternate2ID = property(__alternate2ID.value, __alternate2ID.set, None, None)

    _ElementMap.update({
        __alternate1ID.name() : __alternate1ID,
        __alternate2ID.name() : __alternate2ID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.alternateType = alternateType
Namespace.addCategoryObject('typeBinding', 'alternateType', alternateType)


# Complex type {http://komadu.d2i.indiana.edu}specializationType with content type ELEMENT_ONLY
class specializationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}specializationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'specializationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 315, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}specificEntityID uses Python identifier specificEntityID
    __specificEntityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'specificEntityID'), 'specificEntityID', '__httpkomadu_d2i_indiana_edu_specializationType_httpkomadu_d2i_indiana_eduspecificEntityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 317, 12), )

    
    specificEntityID = property(__specificEntityID.value, __specificEntityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}generalEntityID uses Python identifier generalEntityID
    __generalEntityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'generalEntityID'), 'generalEntityID', '__httpkomadu_d2i_indiana_edu_specializationType_httpkomadu_d2i_indiana_edugeneralEntityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 318, 12), )

    
    generalEntityID = property(__generalEntityID.value, __generalEntityID.set, None, None)

    _ElementMap.update({
        __specificEntityID.name() : __specificEntityID,
        __generalEntityID.name() : __generalEntityID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.specializationType = specializationType
Namespace.addCategoryObject('typeBinding', 'specializationType', specializationType)


# Complex type {http://komadu.d2i.indiana.edu}attributionType with content type ELEMENT_ONLY
class attributionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}attributionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'attributionType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 322, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}entityID uses Python identifier entityID
    __entityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityID'), 'entityID', '__httpkomadu_d2i_indiana_edu_attributionType_httpkomadu_d2i_indiana_eduentityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 324, 12), )

    
    entityID = property(__entityID.value, __entityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}agentID uses Python identifier agentID
    __agentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agentID'), 'agentID', '__httpkomadu_d2i_indiana_edu_attributionType_httpkomadu_d2i_indiana_eduagentID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 325, 12), )

    
    agentID = property(__agentID.value, __agentID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_attributionType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 326, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    _ElementMap.update({
        __entityID.name() : __entityID,
        __agentID.name() : __agentID,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.attributionType = attributionType
Namespace.addCategoryObject('typeBinding', 'attributionType', attributionType)


# Complex type {http://komadu.d2i.indiana.edu}associationType with content type ELEMENT_ONLY
class associationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}associationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'associationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 330, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}activityID uses Python identifier activityID
    __activityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityID'), 'activityID', '__httpkomadu_d2i_indiana_edu_associationType_httpkomadu_d2i_indiana_eduactivityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 332, 12), )

    
    activityID = property(__activityID.value, __activityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}agentID uses Python identifier agentID
    __agentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agentID'), 'agentID', '__httpkomadu_d2i_indiana_edu_associationType_httpkomadu_d2i_indiana_eduagentID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 333, 12), )

    
    agentID = property(__agentID.value, __agentID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}planID uses Python identifier planID
    __planID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'planID'), 'planID', '__httpkomadu_d2i_indiana_edu_associationType_httpkomadu_d2i_indiana_eduplanID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 334, 12), )

    
    planID = property(__planID.value, __planID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_associationType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 335, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    _ElementMap.update({
        __activityID.name() : __activityID,
        __agentID.name() : __agentID,
        __planID.name() : __planID,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.associationType = associationType
Namespace.addCategoryObject('typeBinding', 'associationType', associationType)


# Complex type {http://komadu.d2i.indiana.edu}delegationType with content type ELEMENT_ONLY
class delegationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}delegationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'delegationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 339, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}delegateAgentID uses Python identifier delegateAgentID
    __delegateAgentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'delegateAgentID'), 'delegateAgentID', '__httpkomadu_d2i_indiana_edu_delegationType_httpkomadu_d2i_indiana_edudelegateAgentID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 341, 12), )

    
    delegateAgentID = property(__delegateAgentID.value, __delegateAgentID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}responsibleAgentID uses Python identifier responsibleAgentID
    __responsibleAgentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responsibleAgentID'), 'responsibleAgentID', '__httpkomadu_d2i_indiana_edu_delegationType_httpkomadu_d2i_indiana_eduresponsibleAgentID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 342, 12), )

    
    responsibleAgentID = property(__responsibleAgentID.value, __responsibleAgentID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}activity uses Python identifier activity
    __activity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activity'), 'activity', '__httpkomadu_d2i_indiana_edu_delegationType_httpkomadu_d2i_indiana_eduactivity', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 343, 12), )

    
    activity = property(__activity.value, __activity.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_delegationType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 344, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    _ElementMap.update({
        __delegateAgentID.name() : __delegateAgentID,
        __responsibleAgentID.name() : __responsibleAgentID,
        __activity.name() : __activity,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.delegationType = delegationType
Namespace.addCategoryObject('typeBinding', 'delegationType', delegationType)


# Complex type {http://komadu.d2i.indiana.edu}membershipType with content type ELEMENT_ONLY
class membershipType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}membershipType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'membershipType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 348, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}collectionID uses Python identifier collectionID
    __collectionID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collectionID'), 'collectionID', '__httpkomadu_d2i_indiana_edu_membershipType_httpkomadu_d2i_indiana_educollectionID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 350, 12), )

    
    collectionID = property(__collectionID.value, __collectionID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}entityID uses Python identifier entityID
    __entityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityID'), 'entityID', '__httpkomadu_d2i_indiana_edu_membershipType_httpkomadu_d2i_indiana_eduentityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 351, 12), )

    
    entityID = property(__entityID.value, __entityID.set, None, None)

    _ElementMap.update({
        __collectionID.name() : __collectionID,
        __entityID.name() : __entityID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.membershipType = membershipType
Namespace.addCategoryObject('typeBinding', 'membershipType', membershipType)


# Complex type {http://komadu.d2i.indiana.edu}activityInformationType with content type ELEMENT_ONLY
class activityInformationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}activityInformationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'activityInformationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 355, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}activityID uses Python identifier activityID
    __activityID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityID'), 'activityID', '__httpkomadu_d2i_indiana_edu_activityInformationType_httpkomadu_d2i_indiana_eduactivityID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 357, 12), )

    
    activityID = property(__activityID.value, __activityID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_activityInformationType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 361, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    _ElementMap.update({
        __activityID.name() : __activityID,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.activityInformationType = activityInformationType
Namespace.addCategoryObject('typeBinding', 'activityInformationType', activityInformationType)


# Complex type {http://komadu.d2i.indiana.edu}attributesType with content type ELEMENT_ONLY
class attributesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}attributesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'attributesType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 365, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}attribute uses Python identifier attribute
    __attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attribute'), 'attribute', '__httpkomadu_d2i_indiana_edu_attributesType_httpkomadu_d2i_indiana_eduattribute', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 367, 12), )

    
    attribute = property(__attribute.value, __attribute.set, None, None)

    _ElementMap.update({
        __attribute.name() : __attribute
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.attributesType = attributesType
Namespace.addCategoryObject('typeBinding', 'attributesType', attributesType)


# Complex type {http://komadu.d2i.indiana.edu}membersType with content type ELEMENT_ONLY
class membersType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}membersType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'membersType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 371, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}member uses Python identifier member
    __member = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'member'), 'member', '__httpkomadu_d2i_indiana_edu_membersType_httpkomadu_d2i_indiana_edumember', True, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 373, 12), )

    
    member = property(__member.value, __member.set, None, None)

    _ElementMap.update({
        __member.name() : __member
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.membersType = membersType
Namespace.addCategoryObject('typeBinding', 'membersType', membersType)


# Complex type {http://komadu.d2i.indiana.edu}attributeType with content type ELEMENT_ONLY
class attributeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}attributeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'attributeType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 384, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'property'), 'property_', '__httpkomadu_d2i_indiana_edu_attributeType_httpkomadu_d2i_indiana_eduproperty', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 386, 12), )

    
    property_ = property(__property.value, __property.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpkomadu_d2i_indiana_edu_attributeType_httpkomadu_d2i_indiana_eduvalue', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 387, 12), )

    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __property.name() : __property,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.attributeType = attributeType
Namespace.addCategoryObject('typeBinding', 'attributeType', attributeType)


# Complex type {http://komadu.d2i.indiana.edu}agentActivityType with content type ELEMENT_ONLY
class agentActivityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}agentActivityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'agentActivityType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 391, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}agent uses Python identifier agent
    __agent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agent'), 'agent', '__httpkomadu_d2i_indiana_edu_agentActivityType_httpkomadu_d2i_indiana_eduagent', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 393, 12), )

    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}activity uses Python identifier activity
    __activity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activity'), 'activity', '__httpkomadu_d2i_indiana_edu_agentActivityType_httpkomadu_d2i_indiana_eduactivity', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 394, 12), )

    
    activity = property(__activity.value, __activity.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}association uses Python identifier association
    __association = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'association'), 'association', '__httpkomadu_d2i_indiana_edu_agentActivityType_httpkomadu_d2i_indiana_eduassociation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 395, 12), )

    
    association = property(__association.value, __association.set, None, None)

    _ElementMap.update({
        __agent.name() : __agent,
        __activity.name() : __activity,
        __association.name() : __association
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.agentActivityType = agentActivityType
Namespace.addCategoryObject('typeBinding', 'agentActivityType', agentActivityType)


# Complex type {http://komadu.d2i.indiana.edu}agentEntityType with content type ELEMENT_ONLY
class agentEntityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}agentEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'agentEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 399, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}agent uses Python identifier agent
    __agent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agent'), 'agent', '__httpkomadu_d2i_indiana_edu_agentEntityType_httpkomadu_d2i_indiana_eduagent', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 401, 12), )

    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}entity uses Python identifier entity
    __entity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entity'), 'entity', '__httpkomadu_d2i_indiana_edu_agentEntityType_httpkomadu_d2i_indiana_eduentity', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 402, 12), )

    
    entity = property(__entity.value, __entity.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attribution uses Python identifier attribution
    __attribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attribution'), 'attribution', '__httpkomadu_d2i_indiana_edu_agentEntityType_httpkomadu_d2i_indiana_eduattribution', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 403, 12), )

    
    attribution = property(__attribution.value, __attribution.set, None, None)

    _ElementMap.update({
        __agent.name() : __agent,
        __entity.name() : __entity,
        __attribution.name() : __attribution
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.agentEntityType = agentEntityType
Namespace.addCategoryObject('typeBinding', 'agentEntityType', agentEntityType)


# Complex type {http://komadu.d2i.indiana.edu}activityEntityType with content type ELEMENT_ONLY
class activityEntityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}activityEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'activityEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 407, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}activity uses Python identifier activity
    __activity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activity'), 'activity', '__httpkomadu_d2i_indiana_edu_activityEntityType_httpkomadu_d2i_indiana_eduactivity', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 409, 12), )

    
    activity = property(__activity.value, __activity.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}entity uses Python identifier entity
    __entity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entity'), 'entity', '__httpkomadu_d2i_indiana_edu_activityEntityType_httpkomadu_d2i_indiana_eduentity', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 410, 12), )

    
    entity = property(__entity.value, __entity.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage'), 'usage', '__httpkomadu_d2i_indiana_edu_activityEntityType_httpkomadu_d2i_indiana_eduusage', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 412, 16), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}generation uses Python identifier generation
    __generation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'generation'), 'generation', '__httpkomadu_d2i_indiana_edu_activityEntityType_httpkomadu_d2i_indiana_edugeneration', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 413, 16), )

    
    generation = property(__generation.value, __generation.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'start'), 'start', '__httpkomadu_d2i_indiana_edu_activityEntityType_httpkomadu_d2i_indiana_edustart', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 414, 16), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'end'), 'end', '__httpkomadu_d2i_indiana_edu_activityEntityType_httpkomadu_d2i_indiana_eduend', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 415, 16), )

    
    end = property(__end.value, __end.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}invalidation uses Python identifier invalidation
    __invalidation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'invalidation'), 'invalidation', '__httpkomadu_d2i_indiana_edu_activityEntityType_httpkomadu_d2i_indiana_eduinvalidation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 416, 16), )

    
    invalidation = property(__invalidation.value, __invalidation.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_activityEntityType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 418, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    _ElementMap.update({
        __activity.name() : __activity,
        __entity.name() : __entity,
        __usage.name() : __usage,
        __generation.name() : __generation,
        __start.name() : __start,
        __end.name() : __end,
        __invalidation.name() : __invalidation,
        __attributes.name() : __attributes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.activityEntityType = activityEntityType
Namespace.addCategoryObject('typeBinding', 'activityEntityType', activityEntityType)


# Complex type {http://komadu.d2i.indiana.edu}agentAgentType with content type ELEMENT_ONLY
class agentAgentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}agentAgentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'agentAgentType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 422, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}delegateAgent uses Python identifier delegateAgent
    __delegateAgent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'delegateAgent'), 'delegateAgent', '__httpkomadu_d2i_indiana_edu_agentAgentType_httpkomadu_d2i_indiana_edudelegateAgent', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 424, 12), )

    
    delegateAgent = property(__delegateAgent.value, __delegateAgent.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}responsibleAgent uses Python identifier responsibleAgent
    __responsibleAgent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responsibleAgent'), 'responsibleAgent', '__httpkomadu_d2i_indiana_edu_agentAgentType_httpkomadu_d2i_indiana_eduresponsibleAgent', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 425, 12), )

    
    responsibleAgent = property(__responsibleAgent.value, __responsibleAgent.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}delegation uses Python identifier delegation
    __delegation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'delegation'), 'delegation', '__httpkomadu_d2i_indiana_edu_agentAgentType_httpkomadu_d2i_indiana_edudelegation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 426, 12), )

    
    delegation = property(__delegation.value, __delegation.set, None, None)

    _ElementMap.update({
        __delegateAgent.name() : __delegateAgent,
        __responsibleAgent.name() : __responsibleAgent,
        __delegation.name() : __delegation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.agentAgentType = agentAgentType
Namespace.addCategoryObject('typeBinding', 'agentAgentType', agentAgentType)


# Complex type {http://komadu.d2i.indiana.edu}activityActivityType with content type ELEMENT_ONLY
class activityActivityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}activityActivityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'activityActivityType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 431, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}activity1 uses Python identifier activity1
    __activity1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activity1'), 'activity1', '__httpkomadu_d2i_indiana_edu_activityActivityType_httpkomadu_d2i_indiana_eduactivity1', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 433, 12), )

    
    activity1 = property(__activity1.value, __activity1.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}activity2 uses Python identifier activity2
    __activity2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activity2'), 'activity2', '__httpkomadu_d2i_indiana_edu_activityActivityType_httpkomadu_d2i_indiana_eduactivity2', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 434, 12), )

    
    activity2 = property(__activity2.value, __activity2.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}communication uses Python identifier communication
    __communication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'communication'), 'communication', '__httpkomadu_d2i_indiana_edu_activityActivityType_httpkomadu_d2i_indiana_educommunication', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 435, 12), )

    
    communication = property(__communication.value, __communication.set, None, None)

    _ElementMap.update({
        __activity1.name() : __activity1,
        __activity2.name() : __activity2,
        __communication.name() : __communication
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.activityActivityType = activityActivityType
Namespace.addCategoryObject('typeBinding', 'activityActivityType', activityActivityType)


# Complex type {http://komadu.d2i.indiana.edu}entityEntityType with content type ELEMENT_ONLY
class entityEntityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}entityEntityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'entityEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 440, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}entity1 uses Python identifier entity1
    __entity1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entity1'), 'entity1', '__httpkomadu_d2i_indiana_edu_entityEntityType_httpkomadu_d2i_indiana_eduentity1', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 442, 12), )

    
    entity1 = property(__entity1.value, __entity1.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}entity2 uses Python identifier entity2
    __entity2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entity2'), 'entity2', '__httpkomadu_d2i_indiana_edu_entityEntityType_httpkomadu_d2i_indiana_eduentity2', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 443, 12), )

    
    entity2 = property(__entity2.value, __entity2.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}derivation uses Python identifier derivation
    __derivation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'derivation'), 'derivation', '__httpkomadu_d2i_indiana_edu_entityEntityType_httpkomadu_d2i_indiana_eduderivation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 445, 16), )

    
    derivation = property(__derivation.value, __derivation.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}revision uses Python identifier revision
    __revision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'revision'), 'revision', '__httpkomadu_d2i_indiana_edu_entityEntityType_httpkomadu_d2i_indiana_edurevision', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 446, 16), )

    
    revision = property(__revision.value, __revision.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}quotation uses Python identifier quotation
    __quotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quotation'), 'quotation', '__httpkomadu_d2i_indiana_edu_entityEntityType_httpkomadu_d2i_indiana_eduquotation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 447, 16), )

    
    quotation = property(__quotation.value, __quotation.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}primarySource uses Python identifier primarySource
    __primarySource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'primarySource'), 'primarySource', '__httpkomadu_d2i_indiana_edu_entityEntityType_httpkomadu_d2i_indiana_eduprimarySource', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 448, 16), )

    
    primarySource = property(__primarySource.value, __primarySource.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}alternate uses Python identifier alternate
    __alternate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'alternate'), 'alternate', '__httpkomadu_d2i_indiana_edu_entityEntityType_httpkomadu_d2i_indiana_edualternate', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 449, 16), )

    
    alternate = property(__alternate.value, __alternate.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}specialization uses Python identifier specialization
    __specialization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'specialization'), 'specialization', '__httpkomadu_d2i_indiana_edu_entityEntityType_httpkomadu_d2i_indiana_eduspecialization', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 450, 16), )

    
    specialization = property(__specialization.value, __specialization.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}membership uses Python identifier membership
    __membership = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'membership'), 'membership', '__httpkomadu_d2i_indiana_edu_entityEntityType_httpkomadu_d2i_indiana_edumembership', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 451, 16), )

    
    membership = property(__membership.value, __membership.set, None, None)

    _ElementMap.update({
        __entity1.name() : __entity1,
        __entity2.name() : __entity2,
        __derivation.name() : __derivation,
        __revision.name() : __revision,
        __quotation.name() : __quotation,
        __primarySource.name() : __primarySource,
        __alternate.name() : __alternate,
        __specialization.name() : __specialization,
        __membership.name() : __membership
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.entityEntityType = entityEntityType
Namespace.addCategoryObject('typeBinding', 'entityEntityType', entityEntityType)


# Complex type {http://komadu.d2i.indiana.edu}addAttributesType with content type ELEMENT_ONLY
class addAttributesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://komadu.d2i.indiana.edu}addAttributesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'addAttributesType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 456, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://komadu.d2i.indiana.edu}objectType uses Python identifier objectType
    __objectType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectType'), 'objectType', '__httpkomadu_d2i_indiana_edu_addAttributesType_httpkomadu_d2i_indiana_eduobjectType', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 458, 12), )

    
    objectType = property(__objectType.value, __objectType.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}objectID uses Python identifier objectID
    __objectID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objectID'), 'objectID', '__httpkomadu_d2i_indiana_edu_addAttributesType_httpkomadu_d2i_indiana_eduobjectID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 459, 12), )

    
    objectID = property(__objectID.value, __objectID.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}entityType uses Python identifier entityType
    __entityType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entityType'), 'entityType', '__httpkomadu_d2i_indiana_edu_addAttributesType_httpkomadu_d2i_indiana_eduentityType', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 461, 12), )

    
    entityType = property(__entityType.value, __entityType.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}attributes uses Python identifier attributes
    __attributes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributes'), 'attributes', '__httpkomadu_d2i_indiana_edu_addAttributesType_httpkomadu_d2i_indiana_eduattributes', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 462, 12), )

    
    attributes = property(__attributes.value, __attributes.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}addAttributeTimestamp uses Python identifier addAttributeTimestamp
    __addAttributeTimestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'addAttributeTimestamp'), 'addAttributeTimestamp', '__httpkomadu_d2i_indiana_edu_addAttributesType_httpkomadu_d2i_indiana_eduaddAttributeTimestamp', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 463, 12), )

    
    addAttributeTimestamp = property(__addAttributeTimestamp.value, __addAttributeTimestamp.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}notificationTimestamp uses Python identifier notificationTimestamp
    __notificationTimestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notificationTimestamp'), 'notificationTimestamp', '__httpkomadu_d2i_indiana_edu_addAttributesType_httpkomadu_d2i_indiana_edunotificationTimestamp', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 464, 12), )

    
    notificationTimestamp = property(__notificationTimestamp.value, __notificationTimestamp.set, None, None)

    _ElementMap.update({
        __objectType.name() : __objectType,
        __objectID.name() : __objectID,
        __entityType.name() : __entityType,
        __attributes.name() : __attributes,
        __addAttributeTimestamp.name() : __addAttributeTimestamp,
        __notificationTimestamp.name() : __notificationTimestamp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.addAttributesType = addAttributesType
Namespace.addCategoryObject('typeBinding', 'addAttributesType', addAttributesType)


# Complex type {http://komadu.d2i.indiana.edu}userAgentType with content type ELEMENT_ONLY
class userAgentType (genericAgentType):
    """Complex type {http://komadu.d2i.indiana.edu}userAgentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'userAgentType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 61, 4)
    _ElementMap = genericAgentType._ElementMap.copy()
    _AttributeMap = genericAgentType._AttributeMap.copy()
    # Base type is genericAgentType
    
    # Element agentID ({http://komadu.d2i.indiana.edu}agentID) inherited from {http://komadu.d2i.indiana.edu}genericAgentType
    
    # Element attributes ({http://komadu.d2i.indiana.edu}attributes) inherited from {http://komadu.d2i.indiana.edu}genericAgentType
    
    # Element {http://komadu.d2i.indiana.edu}fullName uses Python identifier fullName
    __fullName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fullName'), 'fullName', '__httpkomadu_d2i_indiana_edu_userAgentType_httpkomadu_d2i_indiana_edufullName', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 65, 20), )

    
    fullName = property(__fullName.value, __fullName.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}affiliation uses Python identifier affiliation
    __affiliation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'affiliation'), 'affiliation', '__httpkomadu_d2i_indiana_edu_userAgentType_httpkomadu_d2i_indiana_eduaffiliation', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 66, 20), )

    
    affiliation = property(__affiliation.value, __affiliation.set, None, None)

    
    # Element {http://komadu.d2i.indiana.edu}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'email'), 'email', '__httpkomadu_d2i_indiana_edu_userAgentType_httpkomadu_d2i_indiana_eduemail', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 67, 20), )

    
    email = property(__email.value, __email.set, None, None)

    _ElementMap.update({
        __fullName.name() : __fullName,
        __affiliation.name() : __affiliation,
        __email.name() : __email
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.userAgentType = userAgentType
Namespace.addCategoryObject('typeBinding', 'userAgentType', userAgentType)


# Complex type {http://komadu.d2i.indiana.edu}serviceInformationType with content type ELEMENT_ONLY
class serviceInformationType (workflowInformationType):
    """Complex type {http://komadu.d2i.indiana.edu}serviceInformationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceInformationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 125, 4)
    _ElementMap = workflowInformationType._ElementMap.copy()
    _AttributeMap = workflowInformationType._AttributeMap.copy()
    # Base type is workflowInformationType
    
    # Element workflowID ({http://komadu.d2i.indiana.edu}workflowID) inherited from {http://komadu.d2i.indiana.edu}workflowInformationType
    
    # Element workflowNodeID ({http://komadu.d2i.indiana.edu}workflowNodeID) inherited from {http://komadu.d2i.indiana.edu}workflowInformationType
    
    # Element timestep ({http://komadu.d2i.indiana.edu}timestep) inherited from {http://komadu.d2i.indiana.edu}workflowInformationType
    
    # Element attributes ({http://komadu.d2i.indiana.edu}attributes) inherited from {http://komadu.d2i.indiana.edu}workflowInformationType
    
    # Element instanceOf ({http://komadu.d2i.indiana.edu}instanceOf) inherited from {http://komadu.d2i.indiana.edu}workflowInformationType
    
    # Element {http://komadu.d2i.indiana.edu}serviceID uses Python identifier serviceID
    __serviceID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serviceID'), 'serviceID', '__httpkomadu_d2i_indiana_edu_serviceInformationType_httpkomadu_d2i_indiana_eduserviceID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 129, 20), )

    
    serviceID = property(__serviceID.value, __serviceID.set, None, None)

    _ElementMap.update({
        __serviceID.name() : __serviceID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.serviceInformationType = serviceInformationType
Namespace.addCategoryObject('typeBinding', 'serviceInformationType', serviceInformationType)


# Complex type {http://komadu.d2i.indiana.edu}revisionType with content type ELEMENT_ONLY
class revisionType (derivationType):
    """Complex type {http://komadu.d2i.indiana.edu}revisionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'revisionType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 272, 4)
    _ElementMap = derivationType._ElementMap.copy()
    _AttributeMap = derivationType._AttributeMap.copy()
    # Base type is derivationType
    
    # Element usedEntityID ({http://komadu.d2i.indiana.edu}usedEntityID) inherited from {http://komadu.d2i.indiana.edu}derivationType
    
    # Element generatedEntityID ({http://komadu.d2i.indiana.edu}generatedEntityID) inherited from {http://komadu.d2i.indiana.edu}derivationType
    
    # Element attributes ({http://komadu.d2i.indiana.edu}attributes) inherited from {http://komadu.d2i.indiana.edu}derivationType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.revisionType = revisionType
Namespace.addCategoryObject('typeBinding', 'revisionType', revisionType)


# Complex type {http://komadu.d2i.indiana.edu}quotationType with content type ELEMENT_ONLY
class quotationType (derivationType):
    """Complex type {http://komadu.d2i.indiana.edu}quotationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'quotationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 279, 4)
    _ElementMap = derivationType._ElementMap.copy()
    _AttributeMap = derivationType._AttributeMap.copy()
    # Base type is derivationType
    
    # Element usedEntityID ({http://komadu.d2i.indiana.edu}usedEntityID) inherited from {http://komadu.d2i.indiana.edu}derivationType
    
    # Element generatedEntityID ({http://komadu.d2i.indiana.edu}generatedEntityID) inherited from {http://komadu.d2i.indiana.edu}derivationType
    
    # Element attributes ({http://komadu.d2i.indiana.edu}attributes) inherited from {http://komadu.d2i.indiana.edu}derivationType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.quotationType = quotationType
Namespace.addCategoryObject('typeBinding', 'quotationType', quotationType)


# Complex type {http://komadu.d2i.indiana.edu}planType with content type ELEMENT_ONLY
class planType (entityType):
    """Complex type {http://komadu.d2i.indiana.edu}planType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'planType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 286, 4)
    _ElementMap = entityType._ElementMap.copy()
    _AttributeMap = entityType._AttributeMap.copy()
    # Base type is entityType
    
    # Element file ({http://komadu.d2i.indiana.edu}file) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element block ({http://komadu.d2i.indiana.edu}block) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element collection ({http://komadu.d2i.indiana.edu}collection) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element genericEntity ({http://komadu.d2i.indiana.edu}genericEntity) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element attributes ({http://komadu.d2i.indiana.edu}attributes) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element role ({http://komadu.d2i.indiana.edu}role) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element location ({http://komadu.d2i.indiana.edu}location) inherited from {http://komadu.d2i.indiana.edu}entityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.planType = planType
Namespace.addCategoryObject('typeBinding', 'planType', planType)


# Complex type {http://komadu.d2i.indiana.edu}bundleType with content type ELEMENT_ONLY
class bundleType (entityType):
    """Complex type {http://komadu.d2i.indiana.edu}bundleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bundleType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 293, 4)
    _ElementMap = entityType._ElementMap.copy()
    _AttributeMap = entityType._AttributeMap.copy()
    # Base type is entityType
    
    # Element file ({http://komadu.d2i.indiana.edu}file) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element block ({http://komadu.d2i.indiana.edu}block) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element collection ({http://komadu.d2i.indiana.edu}collection) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element genericEntity ({http://komadu.d2i.indiana.edu}genericEntity) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element attributes ({http://komadu.d2i.indiana.edu}attributes) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element role ({http://komadu.d2i.indiana.edu}role) inherited from {http://komadu.d2i.indiana.edu}entityType
    
    # Element location ({http://komadu.d2i.indiana.edu}location) inherited from {http://komadu.d2i.indiana.edu}entityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.bundleType = bundleType
Namespace.addCategoryObject('typeBinding', 'bundleType', bundleType)


# Complex type {http://komadu.d2i.indiana.edu}primarySourceType with content type ELEMENT_ONLY
class primarySourceType (derivationType):
    """Complex type {http://komadu.d2i.indiana.edu}primarySourceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'primarySourceType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 300, 4)
    _ElementMap = derivationType._ElementMap.copy()
    _AttributeMap = derivationType._AttributeMap.copy()
    # Base type is derivationType
    
    # Element usedEntityID ({http://komadu.d2i.indiana.edu}usedEntityID) inherited from {http://komadu.d2i.indiana.edu}derivationType
    
    # Element generatedEntityID ({http://komadu.d2i.indiana.edu}generatedEntityID) inherited from {http://komadu.d2i.indiana.edu}derivationType
    
    # Element attributes ({http://komadu.d2i.indiana.edu}attributes) inherited from {http://komadu.d2i.indiana.edu}derivationType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.primarySourceType = primarySourceType
Namespace.addCategoryObject('typeBinding', 'primarySourceType', primarySourceType)


# Complex type {http://komadu.d2i.indiana.edu}methodInformationType with content type ELEMENT_ONLY
class methodInformationType (serviceInformationType):
    """Complex type {http://komadu.d2i.indiana.edu}methodInformationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'methodInformationType')
    _XSDLocation = pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 135, 4)
    _ElementMap = serviceInformationType._ElementMap.copy()
    _AttributeMap = serviceInformationType._AttributeMap.copy()
    # Base type is serviceInformationType
    
    # Element workflowID ({http://komadu.d2i.indiana.edu}workflowID) inherited from {http://komadu.d2i.indiana.edu}workflowInformationType
    
    # Element workflowNodeID ({http://komadu.d2i.indiana.edu}workflowNodeID) inherited from {http://komadu.d2i.indiana.edu}workflowInformationType
    
    # Element timestep ({http://komadu.d2i.indiana.edu}timestep) inherited from {http://komadu.d2i.indiana.edu}workflowInformationType
    
    # Element attributes ({http://komadu.d2i.indiana.edu}attributes) inherited from {http://komadu.d2i.indiana.edu}workflowInformationType
    
    # Element instanceOf ({http://komadu.d2i.indiana.edu}instanceOf) inherited from {http://komadu.d2i.indiana.edu}workflowInformationType
    
    # Element serviceID ({http://komadu.d2i.indiana.edu}serviceID) inherited from {http://komadu.d2i.indiana.edu}serviceInformationType
    
    # Element {http://komadu.d2i.indiana.edu}methodID uses Python identifier methodID
    __methodID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'methodID'), 'methodID', '__httpkomadu_d2i_indiana_edu_methodInformationType_httpkomadu_d2i_indiana_edumethodID', False, pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 139, 20), )

    
    methodID = property(__methodID.value, __methodID.set, None, None)

    _ElementMap.update({
        __methodID.name() : __methodID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.methodInformationType = methodInformationType
Namespace.addCategoryObject('typeBinding', 'methodInformationType', methodInformationType)


addAgentActivityRelationship = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addAgentActivityRelationship'), agentActivityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 472, 4))
Namespace.addCategoryObject('elementBinding', addAgentActivityRelationship.name().localName(), addAgentActivityRelationship)

addAgentEntityRelationship = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addAgentEntityRelationship'), agentEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 473, 4))
Namespace.addCategoryObject('elementBinding', addAgentEntityRelationship.name().localName(), addAgentEntityRelationship)

addActivityEntityRelationship = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addActivityEntityRelationship'), activityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 474, 4))
Namespace.addCategoryObject('elementBinding', addActivityEntityRelationship.name().localName(), addActivityEntityRelationship)

addAgentAgentRelationship = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addAgentAgentRelationship'), agentAgentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 475, 4))
Namespace.addCategoryObject('elementBinding', addAgentAgentRelationship.name().localName(), addAgentAgentRelationship)

addActivityActivityRelationship = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addActivityActivityRelationship'), activityActivityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 476, 4))
Namespace.addCategoryObject('elementBinding', addActivityActivityRelationship.name().localName(), addActivityActivityRelationship)

addEntityEntityRelationship = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addEntityEntityRelationship'), entityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 477, 4))
Namespace.addCategoryObject('elementBinding', addEntityEntityRelationship.name().localName(), addEntityEntityRelationship)

addAttributes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addAttributes'), addAttributesType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 478, 4))
Namespace.addCategoryObject('elementBinding', addAttributes.name().localName(), addAttributes)



agentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'userAgent'), userAgentType, scope=agentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 43, 16)))

agentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genericAgent'), genericAgentType, scope=agentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 45, 16)))

agentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), agentEnumType, scope=agentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 47, 12)))

agentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'role'), pyxb.binding.datatypes.string, scope=agentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 49, 12)))

agentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), pyxb.binding.datatypes.string, scope=agentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 50, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 49, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 50, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(agentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'userAgent')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 43, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(agentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genericAgent')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 45, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(agentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 47, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(agentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'role')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 49, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(agentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 50, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
agentType._Automaton = _BuildAutomaton()




genericAgentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agentID'), pyxb.binding.datatypes.anyURI, scope=genericAgentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 56, 12)))

genericAgentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=genericAgentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 57, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 57, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(genericAgentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 56, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(genericAgentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 57, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
genericAgentType._Automaton = _BuildAutomaton_()




activityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'workflowInformation'), workflowInformationType, scope=activityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 105, 16)))

activityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceInformation'), serviceInformationType, scope=activityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 106, 16)))

activityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'methodInformation'), methodInformationType, scope=activityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 107, 16)))

activityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityInformation'), activityInformationType, scope=activityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 109, 16)))

activityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), pyxb.binding.datatypes.string, scope=activityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 111, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 111, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'workflowInformation')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 105, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceInformation')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 106, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'methodInformation')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 107, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityInformation')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 109, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 111, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
activityType._Automaton = _BuildAutomaton_2()




workflowInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'workflowID'), pyxb.binding.datatypes.anyURI, scope=workflowInformationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 117, 12)))

workflowInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'workflowNodeID'), pyxb.binding.datatypes.string, scope=workflowInformationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 118, 12)))

workflowInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timestep'), pyxb.binding.datatypes.int, scope=workflowInformationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 119, 12)))

workflowInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=workflowInformationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 120, 12)))

workflowInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'instanceOf'), instanceOfType, scope=workflowInformationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 121, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 118, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 119, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 120, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 121, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(workflowInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'workflowID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 117, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(workflowInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'workflowNodeID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 118, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(workflowInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestep')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 119, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(workflowInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 120, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(workflowInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instanceOf')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 121, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
workflowInformationType._Automaton = _BuildAutomaton_3()




instanceOfType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'instanceOfID'), pyxb.binding.datatypes.string, scope=instanceOfType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 147, 12)))

instanceOfType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'version'), pyxb.binding.datatypes.string, scope=instanceOfType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 148, 12)))

instanceOfType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creationTime'), pyxb.binding.datatypes.dateTime, scope=instanceOfType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 149, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 148, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 149, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(instanceOfType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instanceOfID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 147, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(instanceOfType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'version')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 148, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(instanceOfType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creationTime')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 149, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
instanceOfType._Automaton = _BuildAutomaton_4()




entityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'file'), fileType, scope=entityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 157, 16)))

entityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'block'), blockType, scope=entityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 158, 16)))

entityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collection'), collectionType, scope=entityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 159, 16)))

entityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genericEntity'), genericEntityType, scope=entityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 160, 16)))

entityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=entityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 163, 12)))

entityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'role'), pyxb.binding.datatypes.string, scope=entityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 165, 12)))

entityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), pyxb.binding.datatypes.string, scope=entityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 166, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 157, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 158, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 159, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 160, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 163, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 165, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 166, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(entityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'file')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 157, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(entityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'block')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 158, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(entityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collection')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 159, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(entityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genericEntity')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 160, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(entityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 163, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(entityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'role')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 165, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(entityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 166, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
entityType._Automaton = _BuildAutomaton_5()




fileType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileURI'), pyxb.binding.datatypes.anyURI, scope=fileType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 172, 12)))

fileType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ownerDN'), pyxb.binding.datatypes.string, scope=fileType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 173, 12)))

fileType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'createDate'), pyxb.binding.datatypes.dateTime, scope=fileType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 174, 12)))

fileType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'size'), pyxb.binding.datatypes.long, scope=fileType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 175, 12)))

fileType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'md5sum'), pyxb.binding.datatypes.string, scope=fileType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 176, 12)))

fileType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fileName'), pyxb.binding.datatypes.string, scope=fileType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 177, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 173, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 174, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 175, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 176, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 177, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 172, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ownerDN')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 173, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'createDate')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 174, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'size')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 175, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'md5sum')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 176, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fileName')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 177, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    return fac.Automaton(states, counters, False, containing_state=None)
fileType._Automaton = _BuildAutomaton_6()




blockType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'blockURI'), pyxb.binding.datatypes.anyURI, scope=blockType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 183, 12)))

blockType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'blockContent'), pyxb.binding.datatypes.string, scope=blockType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 184, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(blockType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'blockURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 183, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(blockType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'blockContent')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 184, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
blockType._Automaton = _BuildAutomaton_7()




collectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collectionURI'), pyxb.binding.datatypes.anyURI, scope=collectionType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 190, 12)))

collectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'members'), membersType, scope=collectionType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 192, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 192, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(collectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collectionURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 190, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(collectionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'members')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 192, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
collectionType._Automaton = _BuildAutomaton_8()




genericEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityURI'), pyxb.binding.datatypes.anyURI, scope=genericEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 198, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(genericEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityURI')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
genericEntityType._Automaton = _BuildAutomaton_9()




generationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityID'), pyxb.binding.datatypes.anyURI, scope=generationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 204, 12)))

generationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityID'), pyxb.binding.datatypes.anyURI, scope=generationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 205, 12)))

generationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), pyxb.binding.datatypes.dateTime, scope=generationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 206, 12)))

generationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=generationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 207, 12)))

generationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), pyxb.binding.datatypes.string, scope=generationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 208, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 206, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 207, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 208, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(generationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 204, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(generationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 205, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(generationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestamp')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 206, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(generationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 207, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(generationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 208, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
generationType._Automaton = _BuildAutomaton_10()




usageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityID'), pyxb.binding.datatypes.anyURI, scope=usageType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 214, 12)))

usageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityID'), pyxb.binding.datatypes.anyURI, scope=usageType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 215, 12)))

usageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), pyxb.binding.datatypes.dateTime, scope=usageType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 216, 12)))

usageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=usageType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 217, 12)))

usageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), pyxb.binding.datatypes.string, scope=usageType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 218, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 216, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 217, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 218, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(usageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 214, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(usageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 215, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(usageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestamp')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 216, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(usageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 217, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(usageType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 218, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
usageType._Automaton = _BuildAutomaton_11()




startType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityID'), pyxb.binding.datatypes.anyURI, scope=startType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 224, 12)))

startType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'triggerID'), pyxb.binding.datatypes.anyURI, scope=startType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 225, 12)))

startType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), pyxb.binding.datatypes.dateTime, scope=startType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 227, 12)))

startType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=startType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 228, 12)))

startType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), pyxb.binding.datatypes.string, scope=startType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 229, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 227, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 228, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 229, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(startType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 224, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(startType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'triggerID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 225, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(startType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestamp')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 227, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(startType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 228, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(startType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 229, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
startType._Automaton = _BuildAutomaton_12()




endType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityID'), pyxb.binding.datatypes.anyURI, scope=endType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 235, 12)))

endType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'triggerID'), pyxb.binding.datatypes.anyURI, scope=endType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 236, 12)))

endType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), pyxb.binding.datatypes.dateTime, scope=endType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 238, 12)))

endType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=endType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 239, 12)))

endType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), pyxb.binding.datatypes.string, scope=endType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 240, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 236, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 238, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 239, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 240, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(endType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 235, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(endType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'triggerID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 236, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(endType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestamp')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 238, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(endType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 239, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(endType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 240, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
endType._Automaton = _BuildAutomaton_13()




invalidationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityID'), pyxb.binding.datatypes.anyURI, scope=invalidationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 246, 12)))

invalidationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityID'), pyxb.binding.datatypes.anyURI, scope=invalidationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 247, 12)))

invalidationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'timestamp'), pyxb.binding.datatypes.dateTime, scope=invalidationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 248, 12)))

invalidationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=invalidationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 249, 12)))

invalidationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'location'), pyxb.binding.datatypes.string, scope=invalidationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 250, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 246, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 248, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 249, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 250, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(invalidationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 246, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(invalidationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 247, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(invalidationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestamp')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 248, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(invalidationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 249, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(invalidationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 250, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
invalidationType._Automaton = _BuildAutomaton_14()




communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'informedActivityID'), pyxb.binding.datatypes.anyURI, scope=communicationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 257, 12)))

communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'informantActivityID'), pyxb.binding.datatypes.anyURI, scope=communicationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 258, 12)))

communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=communicationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 259, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 259, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'informedActivityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 257, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'informantActivityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 258, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 259, 12))
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
communicationType._Automaton = _BuildAutomaton_15()




derivationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usedEntityID'), pyxb.binding.datatypes.anyURI, scope=derivationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 265, 12)))

derivationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generatedEntityID'), pyxb.binding.datatypes.anyURI, scope=derivationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 266, 12)))

derivationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=derivationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 268, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 268, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(derivationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usedEntityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 265, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(derivationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generatedEntityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 266, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(derivationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 268, 12))
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
derivationType._Automaton = _BuildAutomaton_16()




alternateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'alternate1ID'), pyxb.binding.datatypes.anyURI, scope=alternateType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 310, 12)))

alternateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'alternate2ID'), pyxb.binding.datatypes.anyURI, scope=alternateType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 311, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(alternateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alternate1ID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 310, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(alternateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alternate2ID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 311, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
alternateType._Automaton = _BuildAutomaton_17()




specializationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'specificEntityID'), pyxb.binding.datatypes.anyURI, scope=specializationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 317, 12)))

specializationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generalEntityID'), pyxb.binding.datatypes.anyURI, scope=specializationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 318, 12)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(specializationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'specificEntityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 317, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(specializationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generalEntityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 318, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
specializationType._Automaton = _BuildAutomaton_18()




attributionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityID'), pyxb.binding.datatypes.anyURI, scope=attributionType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 324, 12)))

attributionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agentID'), pyxb.binding.datatypes.anyURI, scope=attributionType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 325, 12)))

attributionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=attributionType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 326, 12)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 326, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(attributionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 324, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(attributionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 325, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(attributionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 326, 12))
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
attributionType._Automaton = _BuildAutomaton_19()




associationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityID'), pyxb.binding.datatypes.anyURI, scope=associationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 332, 12)))

associationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agentID'), pyxb.binding.datatypes.anyURI, scope=associationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 333, 12)))

associationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'planID'), pyxb.binding.datatypes.anyURI, scope=associationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 334, 12)))

associationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=associationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 335, 12)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 334, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 335, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(associationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 332, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(associationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 333, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(associationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'planID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 334, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(associationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 335, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
associationType._Automaton = _BuildAutomaton_20()




delegationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'delegateAgentID'), pyxb.binding.datatypes.anyURI, scope=delegationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 341, 12)))

delegationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responsibleAgentID'), pyxb.binding.datatypes.anyURI, scope=delegationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 342, 12)))

delegationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity'), activityType, scope=delegationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 343, 12)))

delegationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=delegationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 344, 12)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 343, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 344, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(delegationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'delegateAgentID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 341, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(delegationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responsibleAgentID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 342, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(delegationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activity')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 343, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(delegationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 344, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
delegationType._Automaton = _BuildAutomaton_21()




membershipType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collectionID'), pyxb.binding.datatypes.anyURI, scope=membershipType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 350, 12)))

membershipType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityID'), pyxb.binding.datatypes.anyURI, scope=membershipType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 351, 12)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(membershipType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collectionID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 350, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(membershipType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 351, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
membershipType._Automaton = _BuildAutomaton_22()




activityInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityID'), pyxb.binding.datatypes.anyURI, scope=activityInformationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 357, 12)))

activityInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=activityInformationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 361, 12)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 361, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 357, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 361, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
activityInformationType._Automaton = _BuildAutomaton_23()




attributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attribute'), attributeType, scope=attributesType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 367, 12)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 367, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(attributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attribute')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 367, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
attributesType._Automaton = _BuildAutomaton_24()




membersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'member'), entityType, scope=membersType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 373, 12)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(membersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'member')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 373, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
membersType._Automaton = _BuildAutomaton_25()




attributeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'property'), pyxb.binding.datatypes.anyURI, scope=attributeType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 386, 12)))

attributeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.string, scope=attributeType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 387, 12)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(attributeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'property')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 386, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(attributeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 387, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
attributeType._Automaton = _BuildAutomaton_26()




agentActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agent'), agentType, scope=agentActivityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 393, 12)))

agentActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity'), activityType, scope=agentActivityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 394, 12)))

agentActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'association'), associationType, scope=agentActivityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 395, 12)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(agentActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agent')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 393, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(agentActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activity')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 394, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(agentActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'association')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 395, 12))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
agentActivityType._Automaton = _BuildAutomaton_27()




agentEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agent'), agentType, scope=agentEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 401, 12)))

agentEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entity'), entityType, scope=agentEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 402, 12)))

agentEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attribution'), attributionType, scope=agentEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 403, 12)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(agentEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agent')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 401, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(agentEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entity')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 402, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(agentEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attribution')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 403, 12))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
agentEntityType._Automaton = _BuildAutomaton_28()




activityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity'), activityType, scope=activityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 409, 12)))

activityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entity'), entityType, scope=activityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 410, 12)))

activityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage'), usageType, scope=activityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 412, 16)))

activityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generation'), generationType, scope=activityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 413, 16)))

activityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'start'), startType, scope=activityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 414, 16)))

activityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'end'), endType, scope=activityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 415, 16)))

activityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'invalidation'), invalidationType, scope=activityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 416, 16)))

activityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=activityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 418, 12)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 418, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(activityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activity')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 409, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(activityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entity')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 410, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 412, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generation')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 413, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'start')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 414, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'end')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 415, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'invalidation')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 416, 16))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(activityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 418, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
activityEntityType._Automaton = _BuildAutomaton_29()




agentAgentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'delegateAgent'), agentType, scope=agentAgentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 424, 12)))

agentAgentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responsibleAgent'), agentType, scope=agentAgentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 425, 12)))

agentAgentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'delegation'), delegationType, scope=agentAgentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 426, 12)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(agentAgentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'delegateAgent')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 424, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(agentAgentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responsibleAgent')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 425, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(agentAgentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'delegation')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 426, 12))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
agentAgentType._Automaton = _BuildAutomaton_30()




activityActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity1'), activityType, scope=activityActivityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 433, 12)))

activityActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity2'), activityType, scope=activityActivityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 434, 12)))

activityActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'communication'), communicationType, scope=activityActivityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 435, 12)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(activityActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activity1')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 433, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(activityActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activity2')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 434, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(activityActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'communication')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 435, 12))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
activityActivityType._Automaton = _BuildAutomaton_31()




entityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entity1'), entityType, scope=entityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 442, 12)))

entityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entity2'), entityType, scope=entityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 443, 12)))

entityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'derivation'), derivationType, scope=entityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 445, 16)))

entityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'revision'), revisionType, scope=entityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 446, 16)))

entityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quotation'), quotationType, scope=entityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 447, 16)))

entityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'primarySource'), primarySourceType, scope=entityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 448, 16)))

entityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'alternate'), alternateType, scope=entityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 449, 16)))

entityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'specialization'), specializationType, scope=entityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 450, 16)))

entityEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'membership'), membershipType, scope=entityEntityType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 451, 16)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(entityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entity1')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 442, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(entityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entity2')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 443, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'derivation')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 445, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'revision')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 446, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quotation')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 447, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'primarySource')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 448, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alternate')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 449, 16))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'specialization')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 450, 16))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(entityEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'membership')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 451, 16))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
entityEntityType._Automaton = _BuildAutomaton_32()




addAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectType'), objectEnumType, scope=addAttributesType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 458, 12)))

addAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objectID'), pyxb.binding.datatypes.anyURI, scope=addAttributesType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 459, 12)))

addAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entityType'), entityEnumType, scope=addAttributesType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 461, 12)))

addAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributes'), attributesType, scope=addAttributesType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 462, 12)))

addAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addAttributeTimestamp'), pyxb.binding.datatypes.dateTime, scope=addAttributesType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 463, 12)))

addAttributesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notificationTimestamp'), pyxb.binding.datatypes.dateTime, scope=addAttributesType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 464, 12)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 461, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 463, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectType')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 458, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objectID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 459, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entityType')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 461, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 462, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'addAttributeTimestamp')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 463, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(addAttributesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notificationTimestamp')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 464, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
addAttributesType._Automaton = _BuildAutomaton_33()




userAgentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fullName'), pyxb.binding.datatypes.string, scope=userAgentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 65, 20)))

userAgentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'affiliation'), pyxb.binding.datatypes.string, scope=userAgentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 66, 20)))

userAgentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), pyxb.binding.datatypes.string, scope=userAgentType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 67, 20)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 57, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 65, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 66, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 67, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(userAgentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agentID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 56, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(userAgentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 57, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(userAgentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fullName')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 65, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(userAgentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'affiliation')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 66, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(userAgentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 67, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
userAgentType._Automaton = _BuildAutomaton_34()




serviceInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceID'), pyxb.binding.datatypes.anyURI, scope=serviceInformationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 129, 20)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 118, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 119, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 120, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 121, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(serviceInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'workflowID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 117, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(serviceInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'workflowNodeID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 118, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(serviceInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestep')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 119, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(serviceInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 120, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(serviceInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instanceOf')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 121, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(serviceInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 129, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
serviceInformationType._Automaton = _BuildAutomaton_35()




def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 268, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(revisionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usedEntityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 265, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(revisionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generatedEntityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 266, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(revisionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 268, 12))
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
revisionType._Automaton = _BuildAutomaton_36()




def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 268, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(quotationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usedEntityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 265, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(quotationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generatedEntityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 266, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(quotationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 268, 12))
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
quotationType._Automaton = _BuildAutomaton_37()




def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 157, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 158, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 159, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 160, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 163, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 165, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 166, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(planType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'file')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 157, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(planType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'block')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 158, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(planType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collection')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 159, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(planType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genericEntity')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 160, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(planType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 163, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(planType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'role')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 165, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(planType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 166, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
planType._Automaton = _BuildAutomaton_38()




def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 157, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 158, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 159, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 160, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 163, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 165, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 166, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(bundleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'file')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 157, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(bundleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'block')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 158, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(bundleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collection')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 159, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(bundleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genericEntity')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 160, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(bundleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 163, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(bundleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'role')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 165, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(bundleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'location')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 166, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
bundleType._Automaton = _BuildAutomaton_39()




def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 268, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(primarySourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usedEntityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 265, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(primarySourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generatedEntityID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 266, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(primarySourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 268, 12))
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
primarySourceType._Automaton = _BuildAutomaton_40()




methodInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'methodID'), pyxb.binding.datatypes.anyURI, scope=methodInformationType, location=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 139, 20)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 118, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 119, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 120, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 121, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(methodInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'workflowID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 117, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(methodInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'workflowNodeID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 118, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(methodInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'timestep')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 119, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(methodInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributes')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 120, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(methodInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'instanceOf')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 121, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(methodInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serviceID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 129, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(methodInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'methodID')), pyxb.utils.utility.Location('/private/tmp/xsdpython/PyXB-1.2.6/komadu_ingest_schema.xsd', 139, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
methodInformationType._Automaton = _BuildAutomaton_41()

