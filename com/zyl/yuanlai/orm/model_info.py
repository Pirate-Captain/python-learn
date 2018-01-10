#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename: model_info
# @Date    : 2018-01-10 11:23
# @Author  : zhuyl

"""
orm model
"""


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.column_type)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar2(100)")


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        print("Found model %s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mappings: %s==>%s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs["__mappings__"] = mappings
        attrs["__table__"] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = "insert into %s (%s) VALUES(%s)" % (self.__table__, ','.join(fields), ','.join(params))
        print("SQL:%s" % sql)
        print("ARGS:%s" % str(args))


class User(Model):
    id = IntegerField("id")
    name = StringField("name")
    email = StringField("email")
    password = StringField("password")


u = User(id=1234, name="mike", email="a@google.com", password="123456")
u.save()
