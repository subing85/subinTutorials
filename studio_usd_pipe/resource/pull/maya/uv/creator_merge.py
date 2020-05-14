NAME = 'merge'
ORDER = 1
VALID = True
TYPE = 'creator'
KEY = 'studio_uv'
OWNER = 'Subin Gopi'
COMMENTS = 'To merge the studio uv'
VERSION = '0.0.0'
MODIFIED = 'May 03, 2020'
ICON = 'merge_studio_uv.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    studio_model = kwargs[KEY][0].encode()
    valid, value, message = maya_scene.merge_studio_uv(studio_model)
    return valid, [value], message
    
    
    

    
