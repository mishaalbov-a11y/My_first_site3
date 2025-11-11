from flask import Flask, render_template, request
from gigachat import GigaChat
from dotenv import load_dotenv
import os
from flask_caching import Cache

# Загружаем переменные окружения из .env
load_dotenv()
GIGACHAT_KEY = os.getenv("GIGACHAT_KEY")

app = Flask(__name__)

#Кэширование
app.config['CACHE_TYPE'] = 'SimpleCache'  # Простое кэширование в памяти
app.config['CACHE_DEFAULT_TIMEOUT'] = 900  # 900 секунд = 15 минут

cache = Cache(app)

@app.route('/')
@cache.cached(query_string=True)
def index():
    return render_template('index.html', title='Главная страница')

@app.route('/oge')
@cache.cached(query_string=True)
def oge():
    return render_template('oge.html', title='Профориентация к ОГЭ')

@app.route('/test_selection_oge')
@cache.cached(query_string=True)
def test_selection_oge():
    return render_template('test_selection_oge.html')

@app.route('/answer_oge')
@cache.cached(query_string=True)
def answer_oge():
    # 1️⃣ Получаем данные из URL
    like = request.args.getlist('like')
    dislike = request.args.getlist('dislike')
    easy = request.args.getlist('easy')
    hard = request.args.getlist('hard')

    # 2️⃣ Формируем текст запроса к GigaChat
    prompt_text = f"""
    Ты — эксперт по профориентации, который помогает ученику подобрать будущую профессию.
    
    Составь короткий, связный, логичный и понятный текст (не более 10 предложений). 
    Строго запрещено использовать знаки Markdown, такие как *, #, ##, ###, **, ***, -
    Соблюдай знаки пунктуации и не нарушай грамматику русского языка.
    Меньше используй тире
    Раздели ответ на абзацы!

    Ответ должен включать части (Каждая часть должна быть в отдельном абзаце):
    
    1. Первое предложение должо быть таким: "Привет! Представлю твою профориентацию по выбранным интересам в школе"
    2. Подбор нескольких актуальных профессий на ближайшие годы, которые подойдут ученику по его интересам. 
    3. Рекомендация экзаменов для сдачи ОГЭ (Запрещено советовать Русский язык и Математику)
    4. Советы, на какие предметы стоит обратить особое внимание, чтобы достичь успеха в выбранных направлениях.  
    5. Завершение с мотивирующим и ободряющим посланием, которое внушает уверенность и желание продолжать учиться.

    Информация о предпочтениях ученика:  
    Любимые предметы: {', '.join(like) if like else '—'}  
    Нелюбимые предметы: {', '.join(dislike) if dislike else '—'}  
    Лёгкие предметы: {', '.join(easy) if easy else '—'}  
    Сложные предметы: {', '.join(hard) if hard else '—'}

    Пиши живым, естественным языком, будто обращаешься лично к ученику.
    """

    # 3️⃣ Обращаемся к GigaChat
    try:
        with GigaChat(credentials=GIGACHAT_KEY, verify_ssl_certs=False) as giga:
            response = giga.chat(prompt_text)
            giga_response = response.choices[0].message.content
    except Exception as e:
        giga_response = f"Ошибка при обращении к GigaChat: {e}"

    # 4️⃣ Передаём всё в шаблон
    return render_template(
        'answer_oge.html',
        title='Результаты теста',
        like=like,
        dislike=dislike,
        easy=easy,
        hard=hard,
        giga_response=giga_response
    )

@app.route('/ege')
@cache.cached(query_string=True)
def ege():
    return render_template('ege.html', title='Профориентация к ЕГЭ')

@app.route('/test_selection_ege')
@cache.cached(query_string=True)
def test_selection_ege():
    return render_template('test_selection_ege.html')

@app.route('/answer_ege')
@cache.cached(query_string=True)
def answer_ege():
    # 1️⃣ Получаем все ответы пользователя
    like = request.args.getlist('like')
    career_path = request.args.get('career_path', '')
    job_type = request.args.get('job_type', '')
    learning_style = request.args.get('learning_style', '')
    work_rhythm = request.args.get('work_rhythm', '')
    games = request.args.get('games', '')
    childhood = request.args.get('childhood', '')

    # 2️⃣ Формируем текст запроса к GigaChat
    prompt_text = f"""
Ты — эксперт по профориентации, который помогает ученику подобрать будущую профессию.

Составь короткий, логичный и понятный текст (до 13 предложений),
без использования Markdown символов (#, *, **, -, ## и т.п.).
Пиши грамотно, без лишних восклицаний, и избегай разговорных слов.
Раздели ответ на абзацы! 

Ответ должен включать части:

1. Начни с фразы: "Привет! Представлю твою профориентацию по выбранным интересам"
2. Подбери несколько актуальных профессий ближайших лет, которые подойдут ученику, исходя из его интересов и ответов.  
3. Укажи, какие экзамены ЕГЭ подойдут для подготовки к этим направлениям (Запрещено советовать Русский язык и Математику).
4. Дай советы, на какие школьные предметы стоит сделать упор, чтобы развить подходящие навыки.
5. Заверши коротким, мотивирующим и вдохновляющим посланием — чтобы ученик почувствовал уверенность и желание развиваться.

Информация об ученике:
Любимые предметы: {', '.join(like) if like else '—'}
Предпочтительная карьерная траектория: {career_path or '—'}
Тип работы, который выбрал ученик: {job_type or '—'}
Как ученик предпочитает получать информацию: {learning_style or '—'}
Предпочтительный ритм работы: {work_rhythm or '—'}
Какой тип игр ближе по духу: {games or '—'}
Что особенно нравилось в детстве: {childhood or '—'}

Пиши естественно, доброжелательно и в позитивном тоне, как будто общаешься лично с учеником.
"""

    # 3️⃣ Отправляем запрос к GigaChat
    try:
        with GigaChat(credentials=GIGACHAT_KEY, verify_ssl_certs=False) as giga:
            response = giga.chat(prompt_text)
            giga_response = response.choices[0].message.content
    except Exception as e:
        giga_response = f"Ошибка при обращении к GigaChat: {e}"

    # 4️⃣ Отправляем данные в шаблон
    return render_template(
        'answer_ege.html',
        title='Результаты профориентации',
        like=like,
        career_path=career_path,
        job_type=job_type,
        learning_style=learning_style,
        work_rhythm=work_rhythm,
        games=games,
        childhood=childhood,
        giga_response=giga_response
    )

@app.route('/about')
@cache.cached(query_string=True)
def about():
    return render_template('about.html', title='Об авторе')

if __name__ == '__main__':
    app.run(debug=True)