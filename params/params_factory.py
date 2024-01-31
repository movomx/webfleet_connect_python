
from .default_param import DefaultParam

class ParamsFactory():
    @classmethod
    def build_params(cls, args):  
        return [ParamsFactory._build(k, v) for k, v in args.items()]

    @classmethod
    def _build(cls, key, value):  
        return DefaultParam(key, value)
