from flask import request, jsonify
from config import app, db, API_KEYS
from models import Log

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

@app.route('/logs', methods=['POST'])
def receive_log():
    api_key = request.headers.get("Authorization")
    if not api_key or api_key not in API_KEYS:
        return jsonify({"error": "No autorizado"}), 401

    log_data = request.json
    new_log = Log(
        timestamp=log_data['timestamp'],
        service_name=log_data['service_name'],
        log_level=log_data['log_level'],
        message=log_data['message']
    )
    db.session.add(new_log)
    db.session.commit()
    return jsonify({"message": "Log recibido"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
