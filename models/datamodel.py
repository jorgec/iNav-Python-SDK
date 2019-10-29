import json


class DataModel:
    class Meta:
        fields = {}

    def as_dict(self):
        return {key: str(getattr(self, value)) for key, value in self.Meta.fields.items()}

    def serialize(self):
        return json.dumps(self.as_dict())
