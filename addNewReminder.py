from Reminders import genericReminderFunctions
from Reminders import showReminder
from Reminders import createReminder
import json

config_data = genericReminderFunctions.readJsonFile('config.json')
JSON_FILE = config_data['remindersJsonFilePath']
json_data = genericReminderFunctions.readJsonFile(JSON_FILE)


def main():
    chosen_section = genericReminderFunctions.chooseSection(json_data)
    showReminder.showSection(chosen_section, json_data)

    start_date = genericReminderFunctions.isOptionRight('Qual a primeira data?: ', 'A escolha está correta?: ')
    end_date = genericReminderFunctions.isOptionRight('Qual a última data?: ',  'A escolha está correta?: ')
    new_message = genericReminderFunctions.isOptionRight('Qual a nova messagem?: ',  'A escolha está correta?: ')
    date_interval = createReminder.getDateInterval(start_date, end_date)
    json_data[chosen_section]["Messages"].append(
        {
            "dates": date_interval, 
            "message": new_message.replace('\\n', '\n').replace('\\t', '\t')
        }
    )

    with open(JSON_FILE, 'w', encoding='utf-8') as j_file:
        json.dump(json_data, fp=j_file, ensure_ascii=False)


if __name__ == '__main__':
    main()
