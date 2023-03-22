class Course:
    def __init__(self, title='', schedule='', description='') -> None:
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self) -> str:
        output = ''
        output += f'Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n'
        output += '------------------'
        return output