/****************************************************************************
** Meta object code from reading C++ file 'CppObject.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../../QmlCallCpp2020/CppObject.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'CppObject.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_CppObject_t {
    QByteArrayData data[13];
    char stringdata0[106];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_CppObject_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_CppObject_t qt_meta_stringdata_CppObject = {
    {
QT_MOC_LITERAL(0, 0, 9), // "CppObject"
QT_MOC_LITERAL(1, 10, 10), // "cppSignalA"
QT_MOC_LITERAL(2, 21, 0), // ""
QT_MOC_LITERAL(3, 22, 10), // "cppSignalB"
QT_MOC_LITERAL(4, 33, 3), // "str"
QT_MOC_LITERAL(5, 37, 5), // "value"
QT_MOC_LITERAL(6, 43, 11), // "nameChanged"
QT_MOC_LITERAL(7, 55, 4), // "name"
QT_MOC_LITERAL(8, 60, 11), // "yearChanged"
QT_MOC_LITERAL(9, 72, 4), // "year"
QT_MOC_LITERAL(10, 77, 8), // "cppSlotA"
QT_MOC_LITERAL(11, 86, 8), // "cppSlotB"
QT_MOC_LITERAL(12, 95, 10) // "sendSignal"

    },
    "CppObject\0cppSignalA\0\0cppSignalB\0str\0"
    "value\0nameChanged\0name\0yearChanged\0"
    "year\0cppSlotA\0cppSlotB\0sendSignal"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_CppObject[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       7,   14, // methods
       2,   68, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       4,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   49,    2, 0x06 /* Public */,
       3,    2,   50,    2, 0x06 /* Public */,
       6,    1,   55,    2, 0x06 /* Public */,
       8,    1,   58,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
      10,    0,   61,    2, 0x0a /* Public */,
      11,    2,   62,    2, 0x0a /* Public */,

 // methods: name, argc, parameters, tag, flags
      12,    0,   67,    2, 0x02 /* Public */,

 // signals: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString, QMetaType::Int,    4,    5,
    QMetaType::Void, QMetaType::QString,    7,
    QMetaType::Void, QMetaType::Int,    9,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString, QMetaType::Int,    4,    5,

 // methods: parameters
    QMetaType::Void,

 // properties: name, type, flags
       7, QMetaType::QString, 0x00495103,
       9, QMetaType::Int, 0x00495103,

 // properties: notify_signal_id
       2,
       3,

       0        // eod
};

void CppObject::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<CppObject *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->cppSignalA(); break;
        case 1: _t->cppSignalB((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 2: _t->nameChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 3: _t->yearChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->cppSlotA(); break;
        case 5: _t->cppSlotB((*reinterpret_cast< const QString(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 6: _t->sendSignal(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (CppObject::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CppObject::cppSignalA)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (CppObject::*)(const QString & , int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CppObject::cppSignalB)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (CppObject::*)(const QString );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CppObject::nameChanged)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (CppObject::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CppObject::yearChanged)) {
                *result = 3;
                return;
            }
        }
    }
#ifndef QT_NO_PROPERTIES
    else if (_c == QMetaObject::ReadProperty) {
        auto *_t = static_cast<CppObject *>(_o);
        Q_UNUSED(_t)
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< QString*>(_v) = _t->getName(); break;
        case 1: *reinterpret_cast< int*>(_v) = _t->getYear(); break;
        default: break;
        }
    } else if (_c == QMetaObject::WriteProperty) {
        auto *_t = static_cast<CppObject *>(_o);
        Q_UNUSED(_t)
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setName(*reinterpret_cast< QString*>(_v)); break;
        case 1: _t->setYear(*reinterpret_cast< int*>(_v)); break;
        default: break;
        }
    } else if (_c == QMetaObject::ResetProperty) {
    }
#endif // QT_NO_PROPERTIES
}

QT_INIT_METAOBJECT const QMetaObject CppObject::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_meta_stringdata_CppObject.data,
    qt_meta_data_CppObject,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *CppObject::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *CppObject::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_CppObject.stringdata0))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int CppObject::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 7)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 7;
    }
#ifndef QT_NO_PROPERTIES
    else if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 2;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 2;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}

// SIGNAL 0
void CppObject::cppSignalA()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void CppObject::cppSignalB(const QString & _t1, int _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))), const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t2))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}

// SIGNAL 2
void CppObject::nameChanged(const QString _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 2, _a);
}

// SIGNAL 3
void CppObject::yearChanged(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 3, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
