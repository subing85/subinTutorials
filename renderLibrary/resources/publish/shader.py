NAME = 'Extract Shader'
ORDER = 2
ENABLE = False
TYPE = 'publish'
OWNER = 'Subin Gopi'
COMMENTS = 'extract shader from the geometries'
VERSION = '0.0.0'
MODIFIED = '2021:March:24:Wednesday-10:34:28:AM'
ACTION = 'renderLibrary.resources.publish.shader'


def execute(context, **kwargs):
    import os
    
    from maya import OpenMaya
        
    from renderLibrary.core import export
    from renderLibrary.utils import studioMaya    
    
    nodes = [context.get('node')] or studioMaya.getSelectedNodes()
        
    if not nodes:
        message = 'not found any selection'
        return False, message        
    
    layer = context.get('layer')    
    root_node = studioMaya.getRootNode(nodes[-1])
    
    # get geometries hierarchy    
    _shaders, _nodes = studioMaya.getShaders(layer, root_node)
    # get override data
    _overrides = studioMaya.getOverrides(layer, _nodes)    
    
    # get render memeber
    _members = studioMaya.getRenderMembers(layer, _nodes)
    
    output_path = context.get('path')
   
    output_data = {
        'shader': _shaders,
        'nodes': _nodes,
        'overrides': _overrides,
        'members': _members
        }
    
       
    kwrags = {
        'name': context.get('name'),
        'type': context.get('type'),
        'order': context.get('order'),
        'action': context.get('action'),
        'comments': context.get('comments'),
        'enable': context.get('enable'),
        'time_stamp': context.get('time_stamp')
        }

    
    result, results = export.studio_shader(
        output_path, output_data, format='mayaAscii', preserved=False, **kwrags)
    

    return True, 'success!...', result, results
     
