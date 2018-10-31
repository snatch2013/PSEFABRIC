'''
Adminstrator has to describe the equipment of psefabric.
The mult_cfg.py script uses these dicts in the deciding of how to process the data.
'''

def host_to_type():
    host = {}
    host['panorama'] = 'pa_panorama'
    host['aci_dc1_oss'] = 'cisco_aci'
    host['aci_dc1_corpo'] = 'cisco_aci'
    host['aci_dc2_oss'] = 'cisco_aci'
    host['aci_dc2_corpo'] = 'cisco_aci'
    host['aci_dc1_a1'] = 'cisco_aci'
    host['aci_dc1_a2'] = 'cisco_aci'
    host['aci_dc2_a1'] = 'cisco_aci'
    host['aci_dc2_a2'] = 'cisco_aci'
    return host

def area_to_eq_aci():
    
    map_aci = {}

    map_aci['dc1'] = {}
    map_aci['dc2'] = {}
    map_aci['dc1']['oss_aa'] = 'aci_dc1_oss'
    map_aci['dc1']['int_aa'] = 'aci_dc1_corpo'
    map_aci['dc1']['ext_aa'] = 'aci_dc1_corpo'
    map_aci['dc1']['corpo_internet'] = 'aci_dc1_corpo'
    map_aci['dc1']['oss_internet'] = 'aci_dc1_oss'
    map_aci['dc2']['oss_aa'] = 'aci_dc2_oss'
    map_aci['dc2']['int_aa'] = 'aci_dc2_corpo'
    map_aci['dc2']['ext_aa'] = 'aci_dc2_corpo'
    map_aci['dc2']['corpo_internet'] = 'aci_dc2_corpo'
    map_aci['dc2']['oss_internet'] = 'aci_dc2_oss'

    map_aci['dc1']['a1'] = 'aci_dc1_a1'
    map_aci['dc1']['a2'] = 'aci_dc1_a2'
    map_aci['dc2']['a1'] = 'aci_dc2_a1'
    map_aci['dc2']['a2'] = 'aci_dc2_a2'
    return map_aci

def area_to_eq_pa():

    '''
    Maps areas to panorama device-groups
    '''
    
    map_pa = {}
    map_pa['dc1'] = {}
    map_pa['dc2'] = {}
    map_pa['dc1']['a1'] = 'pa_dc1_a1'
    map_pa['dc1']['a2'] = 'pa_dc1_a2'
    map_pa['dc2']['a1'] = 'pa_dc2_a1'
    map_pa['dc2']['a2'] = 'pa_dc2_a2'
    return map_pa
