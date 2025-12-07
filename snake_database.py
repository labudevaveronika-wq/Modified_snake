import sqlite3
import os
import datetime

class SnakeDatabase:
    def __init__(self, db_name ='snake_game.db'):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, db_name)

        self.con = sqlite3.connect(db_name)
        self.cursor = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        """Создаём таблицы если их нет"""
        # Таблица игроков
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                score_all INTEGER DEFAULT 0,
                time_all INTEGER DEFAULT 0,
                best_score INTEGER DEFAULT 0,
                games_played INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_played TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id INTEGER,
                score INTEGER,
                play_time INTEGER,
                played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (player_id) REFERENCES players(id)
            )
        ''')

    def add_player(self, username):
        self.cursor.execute("SELECT id FROM players WHERE username = ?", (username,))
        if self.cursor.fetchone() is not None:
            # значит игрок уже есть в базе
            return False
        else:
            # не нашли -> добавили нового
            self.cursor.execute("INSERT INTO players (username) VALUES (?)", (username,))

        self.con.commit()
        return True

    def save_game_result(self, username, score, play_time):
        self.cursor.execute("SELECT id FROM players WHERE username =?", (username,))
        player = self.cursor.fetchone()
        if not player:
            return False
        player_id = player[0]

        self.cursor.execute('''
            UPDATE players 
            SET score_all = score_all + ?,
                time_all = time_all + ?,
                best_score = MAX(best_score, ?)
            WHERE id = ?''', (score, play_time, score, player_id))

        self.cursor.execute('''
            INSERT INTO game_sessions (player_id, score, play_time) VALUES (?, ?, ?) ''', (player_id, score, play_time))

        self.con.commit()

        return True

    def get_player_status(self, username):
        self.cursor.execute('''
            SELECT
                username,
                best_score,
                score_all,
                time_all
            FROM players 
            WHERE username = ?
        ''', (username,))

        result = self.cursor.fetchone()

        if result:
            return {
                'username': result[0],
                'best_score': result[1],
                'total_score': result[2],
                'total_time': result[3]
            }
        return None
