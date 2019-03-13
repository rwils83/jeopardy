from dataclasses import dataclass


class Model:

    @classmethod
    def from_request(cls, request):
        request_json = request.get_json()
        if not request_json:
            raise ValueError('No request JSON')
        return cls(**request_json)

    @classmethod
    def from_response(cls, response):
        response_json = response.json()
        if not response_json:
            raise ValueError('No response JSON')
        return cls(**response_json)

    def to_json(self):
        return {
            key: getattr(self, key) for key in self.__dataclass_fields__.keys()
        }


@dataclass
class ClientIDResponse(Model):
    client_id: str


@dataclass
class RegisterRequest(Model):
    address: str
    client_id: str


@dataclass
class Question(Model):
    question_id: str
    text: str
    answer: str
    category: str
    value: int

    def to_json(self):
        json = super().to_json()
        json['answer'] = ''
        return json


@dataclass
class Answer(Model):
    text: str


@dataclass
class AnswerResponse(Model):
    is_correct: bool


@dataclass
class Event(Model):
    event_type: str