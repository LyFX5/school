
import random

from db_api import TableManager

def get_results_of_search(wanted_word):

    table_manager = TableManager()  # create table_manager object

    table_manager.create_connection()
    table_manager.create_cursor()

    results = table_manager.find_string_usage_in_subtitles(wanted_word)

    table_manager.close_connection()

    # если результатов нет, возвращаем 0 и это обрабатывается графическим интерфейсом
    if results == None:
        return 0

    # получаем 5 случайных результатов

    random.shuffle(results)

    num = min(5, len(results))

    results = results[:num]

    rows = []
    for row in results:

        link = row[1]
        startTime = str( int(row[5] / 1000) )
        endTime = str( int(startTime) + int(row[2] / 1000) )
        frase = row[3]

        rows.append([link, startTime, endTime, frase])

    return rows

from flask import Flask, request, render_template, url_for, get_template_attribute

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():

    if request.method == 'POST':
        wanted_word = request.form['wanted_word']

        rows = get_results_of_search(wanted_word)

        return render_template("show_usages.html", rows=rows)
    else:
        return render_template("find_usage_of_text.html")







