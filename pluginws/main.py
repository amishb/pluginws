from Dashboard import plugins
from flask import Flask, jsonify

version = 0.1

# Start Flask App
app = Flask(__name__)

# Add module information
modules = {}
modules.update({'/': {'Name': 'Information',
                      'Version': str(version),
                      'Description': 'Prints version number of system'}})

modules.update({'/modules': {'Name': 'List of Modules',
                             'Version': str(version),
                             'Description': 'Shows information about modules'}})


def add_module_info(route, name, author, ver, desc):
    modules.update({route: {'Name': name,
                           'Author': author,
                           'Version': str(ver),
                           'Description': desc}})


# Add basic routes
@app.route('/')
def show_version():
    return str(version)


@app.route('/modules')
def list_modules():
    return jsonify(modules)


# Start the main app server
if __name__ == '__main__':
    plugins.load_plugins(plugins.list_available_plugins())
    for j, i in enumerate(plugins.list_loaded_plugins()):
        i.register(app, route_base=i._base_route)
        add_module_info(i._base_route, '1', i.author, i.version, i.description)

    # Start server
    app.run(host='0.0.0.0', port=4000, debug=True)