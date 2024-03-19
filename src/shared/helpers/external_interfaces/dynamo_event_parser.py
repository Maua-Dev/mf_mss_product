from typing import Dict, List


class DynamoEventParser:
    records: List[Dict[str, str]]
    data: Dict

    def __init__(self, event: dict = None) -> None:
        self.records = []
        if not event:
            return
        if event.get("Records") is None:
            return

        for record in event.get("Records"):

            record_to_add = {
                "event_id": record.get("eventID"),
                "event_name": record.get("eventName"),
                "new_image": self.parse_dynamo(record.get("dynamodb", {}).get("NewImage", {})),
                "old_image": self.parse_dynamo(record.get("dynamodb", {}).get("OldImage", {})),
            }

            self.records.append(record_to_add)
        self.data = {
            "all_records": self.records
        }


    def parse_dynamo(self, image: dict):
        resp = {}
        for key in image:
            value = list(image[key].values())[0]
            if type(value) == list and len(value) > 0 and list(value[0].keys())[0] == "M":
                value = [self.parse_dynamo(item['M']) for item in value]
            resp[key] = value

        return resp
