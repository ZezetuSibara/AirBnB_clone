#!/usr/bin/python3

"""
Unittest module for FileStorage
"""

from datetime import datetime
import io
from models import storage
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State

import unittest
from os import path, remove


class Test_all(unittest.TestCase):
    """ The all method is tested """

    def setUp(self):
        """ The all methods are set up """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ The all methods Tear down """
        try:
            remove("file.json")
        except:
            pass

    def test_all_empty(self):
        """ Empty Dictionary  is tested """
        self.assertEqual(storage.all(), {})

    def test_basemodel(self):
        """ Basemodel object is tested """
        b = BaseModel()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_user(self):
        """ Basemodel object is tested """
        b = User()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_city(self):
        """ Basemodel object is tested """
        b = City()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_amenity(self):
        """ Test the basemodel object """
        b = Amenity()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_place(self):
        """ Test the basemodel object """
        b = Place()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_review(self):
        """ Test the basemodel object """
        b = Review()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_state(self):
        """ Test the basemodel """
        b = State()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_all_class(self):
        """ Test with all classes """
        b = BaseModel()
        u = User()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        s = State()

        alldic = storage.all()

        self.assertEqual(b, alldic["BaseModel" + '.' + b.id])
        self.assertEqual(u, alldic["User" + '.' + u.id])
        self.assertEqual(c, alldic["City" + '.' + c.id])
        self.assertEqual(a, alldic["Amenity" + '.' + a.id])
        self.assertEqual(p, alldic["Place" + '.' + p.id])
        self.assertEqual(r, alldic["Review" + '.' + r.id])
        self.assertEqual(s, alldic["State" + '.' + s.id])


class Test_new(unittest.TestCase):
    """ Test for the new method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_no_arg(self):
        """ Test no passing argument """
        with self.assertRaises(TypeError):
            storage.new()

    def test_extra_arg(self):
        """ Test no passing argument """
        b = BaseModel()
        with self.assertRaises(TypeError):
            storage.new(b, b)

    def test_basenew(self):
        """ Tests new method with basemodel """
        dic = {"id": "123"}
        b = BaseModel(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_usernew(self):
        """ Tests new method with user """
        dic = {"id": "123"}
        b = User(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_city(self):
        """ Tests new method with city """
        dic = {"id": "123"}
        b = City(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_amenity(self):
        """ Tests new method with amenity """
        dic = {"id": "123"}
        b = Amenity(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_place(self):
        """ Tests new method with amenity """
        dic = {"id": "123"}
        b = Place(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_review(self):
        """ Tests new method with review """
        dic = {"id": "123"}
        b = Review(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_state(self):
        """ Tests new method with state """
        dic = {"id": "123"}
        b = State(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])


class Test_save(unittest.TestCase):
    """ Test for the new method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_save_base(self):
        """ A method with base model is saved """
        dic = {"id": "123"}
        b = BaseModel(**dic)
        key = b.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

    def test_save_base_no_dic(self):
        """ A method with base model is saved """
        b = BaseModel()
        key = b.__class__.__name__ + '.' + b.id
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

    def test_save_base_no_dicX2(self):
        """ A method with base model is saved """
        b = BaseModel()
        b2 = BaseModel()
        key = b.__class__.__name__ + '.' + b.id
        key2 = b2.__class__.__name__ + '.' + b2.id
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])
            self.assertEqual(b2.id, pobj[key2]["id"])
            self.assertEqual(b2.__class__.__name__, pobj[key2]["__class__"])

    def test_save_user(self):
        """ A method to save the user """
        dic = {"id": "123"}
        b = User(**dic)
        key = b.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

    def test_save_user(self):
        """ A method to save the user """
        dic = {"id": "123"}
        b = User(**dic)
        key = b.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

    def test_save_city(self):
        """ A method to save the city """
        dic = {"id": "123"}
        b = City(**dic)
        key = b.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

    def test_save_amenity(self):
        """ A method to save the amenity """
        dic = {"id": "123"}
        b = Amenity(**dic)
        key = b.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

    def test_save_place(self):
        """ A method to save the place """
        dic = {"id": "123"}
        b = Place(**dic)
        key = b.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

    def test_save_review(self):
        """ A method to save the review """
        dic = {"id": "123"}
        b = Review(**dic)
        key = b.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

    def test_save_state(self):
        """ A method to save with state """
        dic = {"id": "123"}
        b = State(**dic)
        key = b.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

    def test_save_all_class(self):
        """ A method to save all_classes """
        dic = {"id": "123"}
        b = BaseModel(**dic)
        u = User(**dic)
        c = City(**dic)
        a = Amenity(**dic)
        p = Place(**dic)
        r = Review(**dic)
        s = State(**dic)
        keyb = b.__class__.__name__ + '.' + "123"
        keyu = u.__class__.__name__ + '.' + "123"
        keyc = c.__class__.__name__ + '.' + "123"
        keya = a.__class__.__name__ + '.' + "123"
        keyp = p.__class__.__name__ + '.' + "123"
        keyr = r.__class__.__name__ + '.' + "123"
        keys = s.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.new(u)
        storage.new(c)
        storage.new(a)
        storage.new(p)
        storage.new(r)
        storage.new(s)
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[keyb]["id"])
            self.assertEqual(b.__class__.__name__, pobj[keyb]["__class__"])
            self.assertEqual(u.id, pobj[keyu]["id"])
            self.assertEqual(u.__class__.__name__, pobj[keyu]["__class__"])
            self.assertEqual(c.id, pobj[keyc]["id"])
            self.assertEqual(c.__class__.__name__, pobj[keyc]["__class__"])
            self.assertEqual(a.id, pobj[keya]["id"])
            self.assertEqual(a.__class__.__name__, pobj[keya]["__class__"])
            self.assertEqual(p.id, pobj[keyp]["id"])
            self.assertEqual(p.__class__.__name__, pobj[keyp]["__class__"])
            self.assertEqual(r.id, pobj[keyr]["id"])
            self.assertEqual(r.__class__.__name__, pobj[keyr]["__class__"])
            self.assertEqual(s.id, pobj[keys]["id"])
            self.assertEqual(s.__class__.__name__, pobj[keys]["__class__"])

    def test_save_all_class_no_kwarg(self):
        """ A method to save for all_classes no kwarg"""
        b = BaseModel()
        u = User()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        s = State()
        keyb = b.__class__.__name__ + '.' + b.id
        keyu = u.__class__.__name__ + '.' + u.id
        keyc = c.__class__.__name__ + '.' + c.id
        keya = a.__class__.__name__ + '.' + a.id
        keyp = p.__class__.__name__ + '.' + p.id
        keyr = r.__class__.__name__ + '.' + r.id
        keys = s.__class__.__name__ + '.' + s.id
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[keyb]["id"])
            self.assertEqual(b.__class__.__name__, pobj[keyb]["__class__"])
            self.assertEqual(u.id, pobj[keyu]["id"])
            self.assertEqual(u.__class__.__name__, pobj[keyu]["__class__"])
            self.assertEqual(c.id, pobj[keyc]["id"])
            self.assertEqual(c.__class__.__name__, pobj[keyc]["__class__"])
            self.assertEqual(a.id, pobj[keya]["id"])
            self.assertEqual(a.__class__.__name__, pobj[keya]["__class__"])
            self.assertEqual(p.id, pobj[keyp]["id"])
            self.assertEqual(p.__class__.__name__, pobj[keyp]["__class__"])
            self.assertEqual(r.id, pobj[keyr]["id"])
            self.assertEqual(r.__class__.__name__, pobj[keyr]["__class__"])
            self.assertEqual(s.id, pobj[keys]["id"])
            self.assertEqual(s.__class__.__name__, pobj[keys]["__class__"])


class Test_reload(unittest.TestCase):
    """ Test a new method """

    def setUp(self):
        """ Fix all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ A Tear down for all """
        try:
            remove("file.json")
        except:
            pass

    def test_no_file(self):
        """ When the file is present, test if there is an error """
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.reload()

    def test_reload_base(self):
        """ Test the reload method for basemodel """
        fname = "file.json"
        b = BaseModel()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_user(self):
        """ Test the reload method for user """
        fname = "file.json"
        b = User()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_city(self):
        """ Test the reload method for city """
        fname = "file.json"
        b = City()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_amenity(self):
        """ Test the reload method for amenity """
        fname = "file.json"
        b = Amenity()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_place(self):
        """ Test the reload method for place """
        fname = "file.json"
        b = Place()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_review(self):
        """ Test the reload method for review """
        fname = "file.json"
        b = Review()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_state(self):
        """ Test the reload method for state """
        fname = "file.json"
        b = State()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_all_clases(self):
        """ Test the reload method for all """
        fname = "file.json"
        b = BaseModel()
        u = User()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        s = State()
        keyb = b.__class__.__name__ + '.' + b.id
        keyu = u.__class__.__name__ + '.' + u.id
        keyc = c.__class__.__name__ + '.' + c.id
        keya = a.__class__.__name__ + '.' + a.id
        keyp = p.__class__.__name__ + '.' + p.id
        keyr = r.__class__.__name__ + '.' + r.id
        keys = s.__class__.__name__ + '.' + s.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        cl = [b, u, c, a, p, r, s]
        cln = ['b', 'u', 'c', 'a', 'p', 'r', 's']
        for i, j in zip(cl, cln):
            key = "key" + j
            self.assertFalse(i == alldic[eval(key)])
            self.assertEqual(i.id, alldic[eval(key)].id)
            self.assertEqual(i.__class__, alldic[eval(key)].__class__)
