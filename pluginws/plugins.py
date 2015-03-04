from importlib import import_module
import os
import logging


PLUGIN_NAMESPACE = 'apis'

log = logging.getLogger('dash')

# Define the plugin management system
_loaded = []


def load_plugins(names):
    plugins = list_available_plugins()

    for name in names:
        if name not in plugins:
            log.warn("Plugin '{0}' not found in list of available plugins".format(name))
        else:
            obj = _load_plugin(name)
            _loaded.append(obj())



def _load_plugin(name):
    modname = '{0}.{1}'.format(PLUGIN_NAMESPACE, name)
    namespace = import_module(modname)
    return getattr(namespace, name)


def reload_plugins(name=''):
    if name == '':
        reload = _loaded
    else:
        reload = [name]

    for name in reload:
        if name not in plugins:
            log.warn("Plugin '{0}' not found in list of available plugins".format(name))
        else:
            _load_plugin(name)
            _loaded.append(name)
            # TODO add in module info here
            log.info("Loaded '{0}'".format(name))



def unload_plugins():
    pass


def list_available_plugins():
    available_plugins = []

    for root, dirs, files in os.walk(PLUGIN_NAMESPACE):
        for f in files:
            if f[-3:] == '.py' and f != '__init__.py':
                available_plugins.append(f[:-3])

    return available_plugins


def list_loaded_plugins():
    return _loaded
