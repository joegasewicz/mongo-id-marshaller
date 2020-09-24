# Mongo ID Marshaller
A small library that marshals Mongo ObjectIds

## Install
```bash
pip install mongo_id_marshaller
```

## Api

### `single()`
By default, the object id key is always set to `id`. you can set your own key using the `id_key` kwarg.

```python
from mongo_id_marshaller import MongoId

"""
mongo_data:
{
    {
    "_id": {$oid: "56c4b2f97c82251d12547b74"},
    "longitude" : 0.81315,
    "latitude" : 52.1642,
    "country" : "England",
    "county" : "London",
    "town" : "London",
}
"""


mongo_data = db.getCollection('towns').findOne({"town": "London"})

mongo_id = MongoId()
mongo_data = mongo_id.single(mongo_data)
"""
mongo_data:
{
    "id" : "56c4b2f97c82251d12547b74",
    "longitude" : 0.81315,
    "latitude" : 52.1642,
    "country" : "England",
    "county" : "London",
    "town" : "London",
}
"""

### `multiple()`

Here we are setting the `id_key` to `_id`

```python
from mongo_id_marshaller import MongoId

"""
mongo_data:
[
    {_id: {$oid: "56c4b2f97c82251d12547b74"}},
    {_id: {$oid: "56c4b2f97c82251d12547b73"}}
]
"""


mongo_data = db.getCollection('towns').findOne({"town": "London"})

mongo_id = MongoId(id_key="_id")
mongo_data = mongo_id.multiple(mongo_data)
"""
mongo_data:
[
    {_id: "56c4b2f97c82251d12547b74"},
    {_id: "56c4b2f9s7c82251d12547b73"}
]
"""