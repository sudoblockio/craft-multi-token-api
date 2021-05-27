from app.db.session import MongoClient

class CRUDcraftmultitoken:

    def get_craft_multi_token_transactions(self, limit=1, skip=0):
        transactions_cursor = (
            MongoClient["icon"]["craft_multi_token_contract"]
            .find(
            {
                "type": "transaction"
            },
            {
                "_id": 0
            })
            .sort("block_number", -1)
            .limit(limit)
            .skip(skip)
        )

        transactions = []
        for t in transactions_cursor:
            transactions.append(t)

        return transactions


    def get_craft_multi_token_transactions_by_method(self, method, limit=1, skip=0):
        transactions_cursor = (
            MongoClient["icon"]["craft_multi_token_contract"]
            .find(
            {
                "method": method,
                "type": "transaction"
            },
            {
                "_id": 0
            })
            .sort("block_number", -1)
            .limit(limit)
            .skip(skip)
        )

        transactions = []
        for t in transactions_cursor:
            transactions.append(t)

        return transactions


    def get_craft_multi_token_logs(self, limit=1, skip=0):
        logs_cursor = (
            MongoClient["icon"]["craft_multi_token_contract"]
            .find(
            {
                "type": "log"
            },
            {
                "_id": 0
            })
            .sort("block_number", -1)
            .limit(limit)
            .skip(skip)
        )

        logs = []
        for l in logs_cursor:
            logs.append(l)

        return logs


    def get_craft_multi_token_logs_by_method(self, method, limit=1, skip=0):
        logs_cursor = (
            MongoClient["icon"]["craft_multi_token_contract"]
            .find(
            {
                "method": method,
                "type": "log"
            },
            {
                "_id": 0
            })
            .sort("block_number", -1)
            .limit(limit)
            .skip(skip)
        )

        logs = []
        for l in logs_cursor:
            logs.append(l)

        return logs

craft_multi_token = CRUDcraftmultitoken()
