##
# File:    InterpretDataObject.py
# Date:    15-Mar-2009
#
# Updates:
#  22-April-2010 : Incorporation into enterpise.
#  add file logging
# 01-Mar-2013  jdw change import for RcsbPath
# 26-Apr-2015  jdw remove site specific and hardcoded path details
#                  remove accession code dependency
#  4-May-2015  jdw clear value container for output items.
##

"""
Interpret data : set of methods to manage the API data based
on the data objects within the workflow.
"""

__docformat__ = "restructuredtext en"
__author__ = "Tom Oldfield"
__email__ = "oldfield@ebi.ac.uk"
__license__ = "Creative Commons Attribution 3.0 Unported"
__version__ = "V0.24"


import sys
import types
import traceback


def getObjectType(object, debug=0, prt=sys.stderr):
    value = None
    try:
        prt.write("+InterpretDataObject.getObjectType : %s\n" % object.__class__.__name__)
        if object.__class__.__name__ == "dataModule":
            value = object.type
        else:
            value = object.getValueTypeName()
    except:
        prt.write("+InterpretDataObject.getObjectCType : failed for object = %s \n" % str(type(object)))
        traceback.print_exc(file=prt)

    return value


def getObjectContainerType(object, debug=0, prt=sys.stderr):
    value = None
    try:
        prt.write("+InterpretDataObject.getObjectContainerType : %s\n" % object.__class__.__name__)
        if object.__class__.__name__ == "dataModule":
            value = object.valueContainer
        else:
            value = object.getContainerTypeName()
    except:
        prt.write("+InterpretDataObject.getObjectContainerType : failed for object = %s \n" % str(type(object)))
        traceback.print_exc(file=prt)

    return value


def getObjectValue(object, debug, prt=sys.stderr):

    value = None

    try:
        prt.write("+InterpretDataObject.getObjectValue : class name %s\n" % object.__class__.__name__)
        if object.__class__.__name__ == "dataModule":
            value = object.data
        else:
            value = __getObject(object, debug, prt)
    except:
        prt.write("+InterpretDataObject.getObjectValue : Failed for object = %s\n" % str(type(object)))
        traceback.print_exc(file=prt)
    return value


def __getObject(object, debug, prt=sys.stderr):

    if debug > 0:
        prt.write("+InterpretDataObject.__getObject : object class                  %s\n" % object.__class__.__name__)
        prt.write("+InterpretDataObject.__getObject : object.getValueTypeName()     %s\n" % object.getValueTypeName())
        prt.write("+InterpretDataObject.__getObject : object.isValueValid()         %s\n" % object.isValueValid())
        prt.write("+InterpretDataObject.__getObject : object.getContainerTypeName() %s\n" % object.getContainerTypeName())
        prt.write("+InterpretDataObject.__getObject : object.isValueSet()           %r\n" % object.isValueSet())
        prt.write("+InterpretDataObject.__getObject : object.getValue()             %r\n" % object.getValue())

    if object.getValueTypeName() is None or not object.isValueValid() or not object.isValueSet():
        prt.write("+InterpretDataObject.__getObject : unitialized or unset value\n")
        return None

    if object.getContainerTypeName() in ['list', 'dict', 'boolean']:
        return object.getValue()
    else:
        return str(object.getValue())


def __replaceVariable(allData, type, dat, debug, prt=sys.stderr):

    if dat is not None:
        if dat[:1] == "$":
            variable = dat[1:]
            if debug > 1:
                prt.write("+InterpretDataObject.__replaceVariable :  replace variable of " + str(variable) + "\n")
            for dataObject in allData:
                if variable == dataObject.name:
                    if debug > 1:
                        prt.write("+InterpretDataObject.__replaceVariable : dataObject.where " + str(dataObject.where) + "\n")
                    if dataObject.where == "constant" or dataObject.where == "variable":
                        if debug > 1:
                            prt.write("+InterpretDataObject.__replaceVariable : replaced " + str(dat) + " with value " + str(dataObject.content) + "\n")
                        return dataObject.content
                    elif dataObject.where == "workflow":
                        if debug > 1:
                            prt.write("+InterpretDataObject.__replaceVariable : replaced " + str(dat) + " with value " + str(dataObject.data) + "\n")
                        return dataObject.data
        return dat
    else:
        return None


def __fillInputOutput(allData, wfData, depID, mode, debug, prt=sys.stderr):
    if debug > 1:
        prt.write("+InterpretDataObject.__fillInputOutput :  name " + str(wfData.name) + "\n")

    if wfData.referenceType is not None:
        if len(wfData.referenceType) > 0:
            wfData.ApiData.setReferenceType(wfData.referenceType)
            if debug > 1:
                prt.write("+InterpretDataObject.__fillInputOutput :  referenceType " + str(wfData.referenceType) + "\n")

    if wfData.partitionNumber is not None:
        if len(wfData.partitionNumber) > 0:
            partitionNumber = __replaceVariable(allData, wfData.type, wfData.partitionNumber, debug, prt)
            wfData.ApiData.setPartitionNumber(partitionNumber)
            if debug > 1:
                prt.write("+InterpretDataObject.__fillInputOutput : partitionNumber " + str(partitionNumber) + "\n")

    if wfData.where is not None:
        #  path(rcsb:cif)
        if wfData.where[:4] == "path":
            absolutePath = wfData.where[5:-1] + depID + ".cif"
            wfData.ApiData.setExternalFilePath(absolutePath)
            if debug > 1:
                prt.write("+InterpretDataObject.__fillInputOutput :  where " + str(absolutePath) + "\n")
        else:
            wfData.ApiData.setStorageType(wfData.where)
            if debug > 1:
                prt.write("+InterpretDataObject.__fillInputOutput :  where " + str(wfData.where) + "\n")
    else:
        prt.write("+InterpretDataObject.__fillInputOutput :  WARNING - no storage type defined for data " + str(wfData.nameHumanReadable) + "\n")

    if wfData.content is not None:
        if wfData.format is not None:
            format = __replaceVariable(allData, wfData.type, wfData.format, debug, prt)
            content = __replaceVariable(allData, wfData.type, wfData.content, debug, prt)
            wfData.ApiData.setContentTypeAndFormat(content, format)
            if debug > 1:
                prt.write("+InterpretDataObject.__fillInputOutput : content  " + str(content) + ", format " + str(format) + "\n")
        else:
            prt.write("+InterpretDataObject.__fillInputOutput :  WARNING - no format defined for data " + str(wfData.nameHumanReadable) + "\n")
    else:
        if wfData.where not in ['inline', 'constant']:
            prt.write("+InterpretDataObject.__fillInputOutput : WARNING - no content defined for data " + str(wfData.nameHumanReadable))

    if wfData.version is not None:
        try:
            version = __replaceVariable(allData, wfData.type, wfData.version, debug, prt)
            if version is not None:
                num = int(version)
            else:
                num = 0
            if not wfData.ApiData.setVersionId(num):
                prt.write("+InterpretDataObject.__fillInputOutput : Bad version number in data object " + str(version) + "\n")
                return None
            else:
                if debug > 1:
                    prt.write("+InterpretDataObject.__fillInputOutput :  versionID : " + str(num) + "\n")
        except ValueError:
            if not wfData.ApiData.setVersionId(version):
                prt.write("+InterpretDataObject.__fillInputOutput :  Bad version number in data object " + str(version) + "\n")
                return None
            else:
                if debug > 1:
                    prt.write("+InterpretDataObject.__fillInputOutput : versionID : " + str(version) + "\n")
    else:
        if wfData.where not in ['inline', 'constant']:
            prt.write("+InterpretDataObject.__fillInputOutput :  WARNING - no version defined for data " + str(wfData.nameHumanReadable) + "\n")
            if debug > 1:
                prt.write("+InterpretDataObject.__fillInputOutput :  versionID : latest\n")
        wfData.ApiData.setVersionId("latest")

    if wfData.valueType is not None:
        wfData.ApiData.setValueTypeName(wfData.valueType)
        if debug > 1:
            prt.write("+InterpretDataObject.__fillInputOutput : valueTypeName  %s\n" % wfData.valueType)
        vType = wfData.valueType
        if vType in ['int', 'integer']:
            defVal = 0
        elif vType in ['float', 'double']:
            defVal = 0.0
        elif vType in ['boolean']:
            defVal = False
        elif vType in ['string', 'date', 'datetime']:
            defVal = ''
        else:
            defVal = None
            prt.write("+InterpretDataObject.__fillInputOutput : unsupported value type %s\n" % vType)

        if ((mode == 'output') and (defVal is not None)):
            wfData.ApiData.setValue(defVal)

    if wfData.valueContainer is not None:
        wfData.ApiData.setContainerTypeName(wfData.valueContainer)
        if debug > 1:
            prt.write("+InterpretDataObject.__fillInputOutput : containerTypeName  " + str(wfData.valueContainer) + "\n")
        vContainer = wfData.valueContainer
        if vContainer == 'dict':
            defVal = {}
        elif vContainer == 'list':
            defVal = []
        elif vContainer == 'value':
            defVal = None
        else:
            defVal = None
            prt.write("+InterpretDataObject.__fillInputOutput : unsupported value container %s\n" % vContainer)
        if ((mode == 'output') and (defVal is not None)):
            wfData.ApiData.setValue(defVal)


def getTaskParameterDict(allData, data, debug, prt=sys.stderr):

    if debug > 1:
        prt.write("+InterpretDataObject.getTaskParameterDict :  input parameter " + str(data) + "\n")
    if data is not None and len(data) > 0:
        d = {}
        keyValues = data.split(',')
        for keyValue in keyValues:
            pair = keyValue.split(':')
            ky = pair[0]
            v = __replaceVariable(allData, "string", pair[1], debug, prt)
            d[ky] = v
            if debug > 1:
                prt.write("+InterpretDataObject.getTaskParameterDict : keyValue %s   ky=%r v=%r\n" % (keyValue, ky, d[ky]))
        if d is not None:
            return d
        else:
            return None
    else:
        return None


def fillAPIinputObject(allData, wfData, id, debug=0, prt=sys.stderr):

    __fillInputOutput(allData, wfData, id, 'input', debug, prt)

    if wfData.selectConditionAttribute is not None:
        if debug > 1:
            prt.write("+InterpretDataObject.fillApiInputObject : selectConditionAttribute" + wfData.selectConditionAttribute + "\n")
        dd = getTaskParameterDict(allData, wfData.selectConditionAttribute, debug, prt)
        if dd is not None:
            for key, value in dd.items():
                prt.write("+InterpretDataObject.fillApiInputObject : add select condition key %r  value %r\n" % (key, value))
                wfData.ApiData.addSelectCondition(key, value)

    if wfData.selectCategory is not None:
        if debug > 1:
            prt.write("+InterpretDataObject.fillApiInputObject : setSelectCategoryName " + str(wfData.selectCategory) + "\n")
        if len(wfData.selectCategory) > 0:
            selectCategory = __replaceVariable(allData, wfData.type, wfData.selectCategory, debug, prt)
            wfData.ApiData.setSelectCategoryName(selectCategory)
            if debug > 1:
                prt.write("+InterpretDataObject.fillApiInputObject : setSelectCategoryName " + str(selectCategory) + "\n")

    if wfData.selectAttribute is not None:
        if debug > 1:
            prt.write("+InterpretDataObject.fillApiInputObject : addSelectionAttributeName " + str(wfData.selectAttribute) + "\n")
        if len(wfData.selectAttribute) > 0:
            selectAttribute = __replaceVariable(allData, wfData.type, wfData.selectAttribute, debug, prt)
            listData = selectAttribute.split(',')
            for l in listData:
                wfData.ApiData.addSelectAttributeName(l)
                if debug > 1:
                    prt.write("+InterpretDataObject.fillApiInputObject :  addSelectionAttributeName " + str(l) + "\n")


def fillAPIoutputObject(allData, wfData, id, debug=0, prt=sys.stderr):
    __fillInputOutput(allData, wfData, id, 'output', debug, prt)


def setRuntimeVariable(allData, value, debug=0, prt=sys.stderr):
    '''
      THIS IS NOT CALLED - MUST DO VARIABLE REPLACEMENT NOT TO REFERENCE - or permament
    '''
# method to reset WfDataObjects based on runtime variables

# version ID
    if debug > 1:
        prt.write("+InterpretDataObject.setRuntimeVariable :   setRuntimeVariable " + str(value.version) + "\n")
    value.version = __replaceVariable(allData, value.type, value.version, debug, prt)
    value.content = __replaceVariable(allData, value.type, value.content, debug, prt)
    value.format = __replaceVariable(allData, value.type, value.format, debug, prt)
    value.selectAttribute = __replaceVariable(allData, value.type, value.selectAttribute, debug, prt)
    value.selectCategory = __replaceVariable(allData, value.type, value.selectCategory, debug, prt)
    value.partitionNumber = __replaceVariable(allData, value.type, value.partitionNumber, debug, prt)
