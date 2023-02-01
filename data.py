import os
import json
import dataclasses

@dataclasses.dataclass(slots=True)
class File:
    read = 'r'
    write = 'w'
    append = 'a'
    create = 'x'


class DataFiles:
    """ used for finding files in the current directory and loading their """
    
    extension           = '.json'
    current_directory   = os.getcwd()
    
    def __init__(self) -> None:
        self.files = [x for x in os.listdir(self.current_directory) if x.endswith(self.extension)]
        self.names = [x.split('.')[0] for x in self.files]
        self.paths = [f'{self.current_directory}\\{x}' for x in self.files]
    
    def get_data(self, filename):
        data = Data()
        data.load_file(filename)
        return data.get()
    
    
        
class Data:
    """  Initializes an empty dataclass for skills, durations and binds """
    
    def __init__(self) -> None:
        self.data = {}
        self.loaded = False
    
    def set(self, datadict: dict) -> None:
        """ set the data to the param dict """
        
        self.data = datadict
        self.loaded = True
    
    def get(self) -> dict[str:dict]:
        """ return the data dict """
        
        if self.loaded:
            return self.data

    def ListOf(self, item: str):
        """ return a list of <item> """
        
        if self.loaded:
            match item:
                case 'names' | 'name' | 'n':
                    return list(self.data.keys())
                case 'durations' | 'duration' | 'd':
                    return [x['duration'] for x in list(self.data.values())]
                case 'binds' | 'bind' | 'b':
                    return [x['bind'] for x in list(self.data.values())]
                case other:
                    return None
    
    def set_filename(self, filename: str):
        """ sets the filename to the param """
        
        if not filename.endswith('.json'):
            filename = filename + '.json'
        self.filename = filename
        path = f'{os.getcwd()}\\{filename}'
        self.path = path
    
    def load_file(self, filename: str):
        """ loads a filename to data """
        
        self.set_filename(filename)
        try:
            with open(self.path, File.read) as rfile:
                data = json.load(fp=rfile)
            self.set(data)
        except FileNotFoundError | FileNotFoundError:
            print('file not found')
            exit()
    
    def save_file(self, filename: str):
        """ save the data to file """
        
        if self.loaded:
            self.set_filename(filename)
            with open(self.path, File.write) as rfile:
                json.dump(obj=self.data, fp=rfile)
    
    
    def make(self, filename: str, names: list[str], durations:list[str], binds:list[str]):     
        """ make the data and datafile with given filename, names, durations, binds """
           
        data = {}
        enames = enumerate(names)
        edurations = enumerate(durations)
        ebinds = enumerate(binds)
        
        array_names = [None for x in names]
        array_durations = [None for x in names]
        array_binds = [None for x in names]
        
        for index, name in enames:
            array_names[index] = name
            array_durations[index] = edurations[index][1]
            array_binds[index] = ebinds[index][1]
            
        for index, x in enames:
            y = data[array_names[index]] = {}
            y['name'] = array_names[index]
            y['duration'] = array_durations[index]
            y['bind'] = array_binds[index]
        
        self.set(data)
        self.save_file(filename)

