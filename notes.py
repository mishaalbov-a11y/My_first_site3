#   ЗАПРОС К GIGACHAT
#
# from gigachat import GigaChat
#
# with GigaChat(credentials="Ключ доступа", verify_ssl_certs=False) as giga:
#     response = giga.chat("Какие факторы влияют на стоимость страховки на дом?")
#     print(response.choices[0].message.content)
#


#   СТАРЫЙ app.py


# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html', title='Главная страница')
#
# @app.route('/oge')
# def oge():
#     return render_template('oge.html', title='Подготовка к ОГЭ')
#
# # Страница выбора предметов
# @app.route('/test_selection_oge')
# def test_selection_oge():
#     return render_template('test_selection_oge.html')
#
# # Страница после выбора (например, начало теста)
# @app.route('/answer_oge')
# def answer_oge():
#     return render_template('answer_oge.html')
#
# @app.route('/ege')
# def ege():
#     return render_template('ege.html', title='Подготовка к ЕГЭ')
#
# @app.route('/about')
# def about():
#     return render_template('about.html', title='Об авторе')
#
# if __name__ == '__main__':
#     app.run(debug=True)


#   ВЫВОД ВЫБРАННЫХ ПРЕДМЕТОВ В answer_oge,html (раскоментировать здесь, а потом в answer_oge)

# <!--    &lt;!&ndash; Список выбранных предметов &ndash;&gt;-->
# <!--    <h5>Предметы, которые тебе нравятся</h5>-->
# <!--    {% if like %}-->
# <!--      <ul>-->
# <!--        {% for item in like %}-->
# <!--          <li>{{ item }}</li>-->
# <!--        {% endfor %}-->
# <!--      </ul>-->
# <!--    {% else %}-->
# <!--      <p class="text-muted">Нет выбранных предметов.</p>-->
# <!--    {% endif %}-->
#
# <!--    <h5>Предметы, которые тебе не нравятся</h5>-->
# <!--    {% if dislike %}-->
# <!--      <ul>-->
# <!--        {% for item in dislike %}-->
# <!--          <li>{{ item }}</li>-->
# <!--        {% endfor %}-->
# <!--      </ul>-->
# <!--    {% else %}-->
# <!--      <p class="text-muted">Нет выбранных предметов.</p>-->
# <!--    {% endif %}-->
#
# <!--    <h5>Предметы, которые тебе кажутся лёгкими</h5>-->
# <!--    {% if easy %}-->
# <!--      <ul>-->
# <!--        {% for item in easy %}-->
# <!--          <li>{{ item }}</li>-->
# <!--        {% endfor %}-->
# <!--      </ul>-->
# <!--    {% else %}-->
# <!--      <p class="text-muted">Нет выбранных предметов.</p>-->
# <!--    {% endif %}-->
#
# <!--    <h5>Предметы, которые тебе кажутся сложными</h5>-->
# <!--    {% if hard %}-->
# <!--      <ul>-->
# <!--        {% for item in hard %}-->
# <!--          <li>{{ item }}</li>-->
# <!--        {% endfor %}-->
# <!--      </ul>-->
# <!--    {% else %}-->
# <!--      <p class="text-muted">Нет выбранных предметов.</p>-->
# <!--    {% endif %}-->
