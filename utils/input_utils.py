from reminders import reminder_json


def is_option_right(
    message: str, confirm_message: str = 'Is the selection right?: '
) -> str:
    while True:
        user_input = input(message)
        is_right = input(confirm_message).lower()[0]

        if is_right in ['y', 's', 'a', 'p', 'c']:
            return user_input


def choose_section(json_data: dict) -> int:
    valid_numbers = []
    for index in range(len(json_data['reminders'])):
        print(
            f'[{index}] {reminder_json.format_title(json_data['reminders'][index]['Title'])}'
        )
        valid_numbers.append(index)

    while True:
        chosen_section = int(is_option_right('Choose a section: '))
        if chosen_section in valid_numbers:
            return chosen_section

        print('Please choose a valid a section!')
