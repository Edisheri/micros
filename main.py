from flask import Flask, jsonify, abort

app = Flask(__name__)

# Данные работников
workers = [
    {"ID": 1, "ФИО": "Иванов", "Номер бригады": 1, "ЗП": 10000, "Специализация": "Черновая отделка"},
    {"ID": 2, "ФИО": "Петров", "Номер бригады": 2, "ЗП": 12000, "Специализация": "Чистовая отделка"},
    {"ID": 3, "ФИО": "Сидоров", "Номер бригады": 1, "ЗП": 16000, "Специализация": "Бригадир"},
    {"ID": 4, "ФИО": "Сергеев", "Номер бригады": 1, "ЗП": 20000, "Специализация": "Прораб"},
    {"ID": 5, "ФИО": "Сергеев", "Номер бригады": 2, "ЗП": 20000, "Специализация": "Прораб"},
]

# Метод для получения списка работников бригады
@app.route('/api/v1/team/<int:team_id>/WorkerList', methods=['GET'])
def get_team_workers(team_id):
    team_workers = [worker for worker in workers if worker["Номер бригады"] == team_id]
    if not team_workers:
        abort(404, description=f"No workers found in team {team_id}")
    return jsonify(team_workers)

# Метод для получения данных о конкретном работнике
@app.route('/api/v1/worker/<int:worker_id>', methods=['GET'])
def get_worker(worker_id):
    worker = next((worker for worker in workers if worker["ID"] == worker_id), None)
    if not worker:
        abort(404, description=f"Worker with ID {worker_id} not found")
    return jsonify(worker)

if __name__ == '__main__':
    app.run(debug=True)
