class Base:
    # ...

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)
