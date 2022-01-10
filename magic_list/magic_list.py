
from typing import List


class MagicList(List):
    
    def __init__(self, cls_type=None):
        self.cls_type = cls_type
        super().__init__()
    
    def __setitem__(self, key, value):
        
        # instantiate cls_type object if provided
        if self.cls_type:
            value = self.cls_type(value)

        # append if the key is the next unassigned index
        if self.__len__() == key:            
            self.append(value)
        else:
            super().__setitem__(key, value)
        return self

    def __getitem__(self, key):
        if self.__len__() == key:
            # append default value 
            self.append(self.cls_type() if self.cls_type else 0)
        return super().__getitem__(key)