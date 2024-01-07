from pathlib import Path
import sqlite3


def init_db():
    global db, cursor
    db_path = Path(__file__).parent / 'shop.db'
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

def create_categories_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT)''')
    db.commit()


def create_products_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    description TEXT,
    id_categories INTEGER,
    FOREIGN KEY (id_categories) REFERENCES categories(id))''')
    db.commit()


def fill_categories():
    cursor.execute('''INSERT INTO categories (name) VALUES 
    ('books'), 
    ('comics'), 
    ('manga')''')
    db.commit()


def fill_products():
    cursor.execute('''INSERT INTO products (name, price, description, id_categories) VALUES
     ('Война и Мир', 600, 'роман-эпопея Льва Николаевича Толстого, описывающий русское общество в эпоху войн против Наполеона.', 1),
      ('Дружелюбный соседушка: Человек-Паук', 850, 'В городе появляется новый злодей по имени Трассёр. И он не так-то прост, как кажется Человеку-Пауку на первый взгляд. С этого и начинается новый этап приключений Дружелюбного Человека-Паука.', 2),
      ('Приключения покемонов', 600, '11-летний Ред из города Паллет-таун уже достаточно опытный тренер, но однажды встреча с загадочным покемоном изменила ему жизнь. Ред начал своё путешествие снова уже с помощью Профессора Оука деда Грина - самого большого своего соперника. На своём пути Ред встречает множество покемонов и тренеров которые так или иначе влияли на его жизнь и на его цель стать Чемпионом мира покемонов!', 3)''')
    db.commit()


def show_data_categories():
    cursor.execute('SELECT name FROM categories')
    return cursor.fetchall()[0]


if __name__ == '__main__':
    init_db()
    create_categories_table()
    create_products_table()
    fill_categories()
    fill_products()