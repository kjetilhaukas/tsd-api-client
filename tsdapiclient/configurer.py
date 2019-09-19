
"""Module for managing tacl config."""

import os
import re

import yaml

HOME = os.path.expanduser('~')
TACL_CONFIG = HOME + '/.tacl_config'


def read_config(filename=TACL_CONFIG):
    with open(filename, 'r') as f:
        config = yaml.load(f, Loader=yaml.Loader)
    return config


def write_config(data, filename=TACL_CONFIG):
    with open(filename, 'w') as f:
        f.write(yaml.dump(data, Dumper=yaml.Dumper))


def update_config(env, key, val):
    if env not in ['test', 'prod']:
        raise Exception
    try:
        config = read_config(TACL_CONFIG)
    except IOError:
        config = {'test': {}, 'prod': {}}
    try:
        if config.has_key(env):
            curr_env = config[env]
            new_env = curr_env.copy()
        else:
            new_env = {}
        new_config = config.copy()
        if not new_env.has_key(key):
            print('updating {0}'.format(key))
            new_config[env].update({key:val})
        elif key in ['api_key', 'pass']:
            print('updating {0}'.format(key))
            new_config[env].update({key:val})
        elif key in ['client_id', 'email', 'client_name']:
            print('trying to modify {0} - not allowed'.format(key))
            print('if you want to do that, delete your current config')
            print('and register again')
            write_config(config, TACL_CONFIG)
            return
        else:
            print('updating {0}'.format(key))
            new_config[env].update({key:val})
        write_config(new_config, TACL_CONFIG)
    except IOError:
        new_config = {}
        write_config(new_config)

def print_config(filename=TACL_CONFIG):
    with open(filename, 'r') as f:
        cf = f.read()
        print(cf)

def delete_config(filename=TACL_CONFIG):
    with open(filename, 'w+') as f:
        f.write(yaml.dump({'test': {}, 'prod': {}}, Dumper=yaml.Dumper))

def print_config_tsd_2fa_key(env, pnum):
    with open(TACL_CONFIG, 'r') as f:
        cf = yaml.load(f, Loader=yaml.Loader)
        print(cf[env][pnum])
