# Copyright (C) 2015, marazt. All rights reserved.
from mapper.object_mapper_exception import ObjectMapperException
from casedict import CaseDict
from helpers.entity_helper import extract_property

class ObjectMapper:
    """
    Base class for mapping class attributes from one class to another one
    Supports mapping conversions too
    """

    def __init__(self):
        """Constructor

        Args:
          mappings: dictionary of the attribute conversions

        Examples:

            1. Mapping of the properties without mapping definition
            In this case are mapped only these properties of the target class which
            are in target and source classes. Other properties are not mapped.
            Suppose we have class 'A' with attributes 'name' and 'last_name'
            and class 'B' with attribute 'name'.
            Initialization of the ObjectMapper will be:
            mapper = ObjectMapper()
            mapper.create_map(A, B)
            instance_b = mapper.map(A(), B)

            In this case, value of A.name will be copied into B.name.

            2. Mapping with defined mapping functions
            Suppose we have class 'A' with attributes 'first_name' and 'last_name'
            , class 'B' with attribute 'full_name' and class 'C' with attribute reverse_name.
            And want to map it in a way 'B.full_name' = 'A.first_name' + 'A.last_name' and
            'C.reverse_name' = 'A.last_name' + 'A.first_name'
            Initialization of the ObjectMapper will be:
            mapper = ObjectMapper()
            mapper.create_map(A, B, {'name': lambda a : a.first_name + " " + a.last_name})
            mapper.create_map(A, C, {'name': lambda a : a.last_name + " " + a.first_name})

            instance_b = mapper.map(A(), B)
            instance_c = mapper.map(A(), C)

            In this case, to the B.name will be mapped A.first_name + " " + A.last_name
            In this case, to the C.name will be mapped A.last_name + " " + A.first_name

            3. Mapping suppression
            For some purposes, it can be needed to suppress some mapping.
            Suppose we have class 'A' with attributes 'name' and 'last_name'
            and class 'B' with attributes 'name' and 'last_name'.
            And we want to map only the A.name into B.name, but not A.last_name to
            b.last_name
            Initialization of the ObjectMapper will be:
            mapper = ObjectMapper()
            mapper.create_map(A, B, {'last_name': None})

            instance_b = mapper.map(A(), B)

            In this case, value of A.name will be copied into B.name automatically by the attribute name 'name'.
            Attribute A.last_name will be not mapped thanks the suppression (lambda function is None).

            4. Case insensitive mapping
            Suppose we have class 'A' with attributes 'Name' and 'Age' and
            class 'B' with attributes 'name' and 'age' and we want to map 'A' to 'B' in a way
            'A.Name' = 'B.name' and 'A.Age' = 'B.age'
            Initialization of the ObjectMapper will be:
            mapper = ObjectMapper()
            mapper.create_map(A, B)
            instance_b = mapper.map(A(), B, ignore_case=True)

            In this case, the value of A.Name will be copied into B.name and
            the value of A.Age will be copied into B.age.

        Returns:
            Instance of the ObjectMapper
        """
        # self.to_type = to_type
        self.mappings = {}
        pass

    def create_map(self, type_from, type_to, alias, mapping=None):
        """Method for adding mapping definitions

        Args:
            type_from: source type object
            type_to: target type object
            alias: map alias
            mapping: dictionary of mapping definitions in a form {'target_property_name',
            lambda function from rhe source}

        Returns:

        """

        key_from = type_from.__name__
        key_to = type_to.__name__

        if not hasattr(self, 'mappings'):
            self.mappings = {}

        if mapping is None:
            mapping = {}

        if key_from in self.mappings:
            inner_map = self.mappings[key_from]
            if alias in inner_map:
                raise ObjectMapperException("Mapping for {0} -> {1} with alias {2} already exists".format(key_from, key_to, alias))
            else:
                self.mappings[key_from][alias] = {}
                self.mappings[key_from][alias]["mapping"] = mapping
                self.mappings[key_from][alias]["type_to"] = type_to
        else:
            self.mappings[key_from] = {}
            self.mappings[key_from][alias] = {}
            self.mappings[key_from][alias]["mapping"] = mapping
            self.mappings[key_from][alias]["type_to"] = type_to

    def map(self, from_obj, alias, ignore_case=False, allow_none=False):
        """
        Note: Changed by Sofyan, to so Map method can use alias
        Method for creating target object instance

        Args:
          from_obj: source object to be mapped from
          alias: map alias
          ignore_case: if set to true, ignores attribute case when performing the mapping
          allow_none: if set to true, returns None if the source object is None; otherwise throws an exception

        Returns:
          Instance of the target class with mapped attributes
        """
        if (from_obj is None) and allow_none:
            return None

        key_from = from_obj.__class__.__name__

        if self.mappings is not None \
            and key_from in self.mappings \
            and alias in self.mappings[key_from]:

            _map = self.mappings[key_from][alias]

            inst = _map["type_to"]()
            
                
            if ignore_case:
                from_props = CaseDict(extract_property(from_obj))
                to_props = CaseDict(extract_property(inst))
            else:
                from_props = extract_property(from_obj)
                to_props = extract_property(inst)

            for prop in to_props:
                if prop in _map["mapping"]:
                    # take mapping function
                    try:
                        fnc = _map["mapping"][prop]
                        if fnc is not None:
                            setattr(inst, prop, fnc(from_obj))
                            # none suppress mapping
                    except Exception:
                        raise ObjectMapperException("Invalid mapping function while setting property {0}.{1}".
                                                    format(inst.__class__.__name__, prop))

                else:
                    # try find property with the same name in the source
                    if prop in from_props:                        
                        setattr(inst, prop, from_props[prop])
                        # case when target attribute is not mapped (can be extended)

            return inst
        else:
            raise ObjectMapperException("No mapping defined for {0} with alias {1}".format(key_from, alias))