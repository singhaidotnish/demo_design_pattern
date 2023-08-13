import os
import json
import yaml
from abc import ABCMeta, abstractmethod
from json.decoder import JSONDecodeError


class FileFactory:
    ALL_TYPES = ['Json', 'Yaml']

    def file_referencer(self, name):
        if name in self.ALL_TYPES:
            return eval('{}()'.format(name))
        else:
            raise NotImplementedError


class IFile(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def write(self, data):
        raise NotImplementedError


class Json(IFile):
    DEMO_JSON = 'demo.json'

    def __init__(self):
        super().__init__()
        self.name = 'Json'
        self.file = os.path.join(os.path.dirname(__file__), Json.DEMO_JSON)

    def read(self, read_from=None):
        _data = None
        try:
            if read_from:
                _data = json.dumps(read_from, indent=4)
                _data = json.loads(_data)
            else:
                with open(self.file, 'r') as jsonFile:
                    _data = json.load(jsonFile)
        except JSONDecodeError as e:
            _data = None
            raise Exception('Error Reading Json ')
        return _data

    def write(self, data):
        try:
            _data = self.read()
            # append new item to data lit
            _data['data'].append(data)
            # serializing json
            json_object = json.dumps(_data, indent=4)
            # writing to demo json
            with open(self.file, 'w+') as outfile:
                outfile.write(json_object)
        except (FileNotFoundError, TypeError, IOError) as e:
            print('Unable to serialize the object')
            return False
        return _data


class Yaml(IFile):
    DEMO_YAML = 'demo.yaml'

    def __init__(self):
        super().__init__()
        self.name = 'Yaml'
        self.file = os.path.join(os.path.dirname(__file__), Yaml.DEMO_YAML)

    def read(self, read_from=None):
        _data = None
        try:
            if read_from:
                _data = yaml.safe_dump(read_from, indent=4)
                _data = yaml.safe_load(_data)
            else:
                with open(self.file, 'r') as yamlFile:
                    _data = yaml.safe_load(yamlFile) or []
        except yaml.YAMLError as e:
            raise Exception('Error Reading Yaml {e}')
        return _data

    def write(self, data):
        try:
            _tmp_data = self.read()
            _tmp_data['data'].append(data)
            with open(self.file, 'w') as stream:
                yaml.safe_dump(_tmp_data, stream, default_flow_style=False)
        except (IOError, ) as e:
            return False
        return _tmp_data
