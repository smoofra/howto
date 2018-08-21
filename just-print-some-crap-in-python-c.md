How to just print some crap in the python C API
=============================================

How to just print a python object from C for debug purposes.

    static const char *repr(PyObject *obj) {
        PyObject* str = PyUnicode_AsEncodedString(PyObject_Repr(obj), "utf-8", "~E~");
        return PyBytes_AS_STRING(str);
    }

    ...

    printf("foobar %s\n", repr(some_thing));
