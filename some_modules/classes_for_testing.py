class AnonymousSurvey():
    def __init__(self, question: str):
        self.question = question
        self.responses = []

    def show_question(self):
        print(f'Вопрос: {self.question}')

    def store_response(self, response):
        self.responses.append(response)

    def show_responses(self):
        responses_string = ''

        for response in self.responses:
            responses_string += f'; {response} ' if responses_string else response

        print(f'Ответы: {responses_string}')
