import mongomock
from bson import ObjectId

from mongo_id_marshaller import MongoId

inserted_id = "56c4b2f97c82251d12547b74"
inserted_id_two = "56c4b2f97c82251d12547b73"


class TestObjectId:

    collection = None

    def setup_class(self):
        self.collection = mongomock.MongoClient().db.collection
        self.collection.insert_one({
            "_id": ObjectId(inserted_id),
            "city": "London",
        })
        self.collection.insert_one({
            "_id": ObjectId(inserted_id_two),
            "city": "Dublin",
        })

    def teardown_class(self):
        self.collection = None

    def test_single(self):
        mongo_id = MongoId()
        mongo_data = self.collection.find_one({"city": "London"})
        result = mongo_id.single(mongo_data)
        expected = {
            "id": inserted_id,
            "city": "London",
        }
        assert result == expected

    def test_single_id_key(self):
        mongo_id = MongoId(id_key="_id")
        mongo_data = self.collection.find_one({"city": "London"})
        result = mongo_id.single(mongo_data)
        expected = {
            "_id": inserted_id,
            "city": "London",
        }
        assert result == expected

    def test_multiple(self):
        mongo_id = MongoId()
        mongo_data = self.collection.find({})
        result = mongo_id.multiple(mongo_data)
        expected = [
            {
                "id": inserted_id,
                "city": "London",
            },
            {
                "id": inserted_id_two,
                "city": "Dublin",
            }]
        assert result == expected

    def test_multiple_id_key(self):
        mongo_id = MongoId(id_key="_id")
        mongo_data = self.collection.find({})
        result = mongo_id.multiple(mongo_data)
        expected = [
            {
                "_id": inserted_id,
                "city": "London",
            },
            {
                "_id": inserted_id_two,
                "city": "Dublin",
            }]
        assert result == expected