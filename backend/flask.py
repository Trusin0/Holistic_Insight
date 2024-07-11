from flask import Flask, send_file, jsonify
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
import pymysql

app = Flask(__name__)

def get_db_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="105306663",
        database="software"
    )
    return conn

def get_reaction_times():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT reaction_time FROM reaction_times WHERE user_id = 'alica'")
    user_reaction_times = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT reaction_time FROM reaction_times")
    average_user_reaction_times = [row[0] for row in cursor.fetchall()]
    conn.close()
    return user_reaction_times, average_user_reaction_times

def create_plot(user_reaction_times, average_user_reaction_times):
    plt.figure(figsize=(14, 6))
    sns.kdeplot(average_user_reaction_times, bw_adjust=0.5, color='lightblue', fill=True, label='Average users', linewidth=1)
    sns.kdeplot(user_reaction_times, bw_adjust=0.5, color='blue', fill=True, label='alica', linewidth=2)
    plt.legend(loc='upper right')
    plt.title('Reaction Time Statistics', fontsize=16)
    plt.xlabel('Time (ms)', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.xticks(np.arange(0, 1001, 25), rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    sns.despine(left=True)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

@app.route('/plot/<test_name>')
def plot(test_name):
    if test_name == 'reaction-time':
        user_reaction_times, average_user_reaction_times = get_reaction_times()
        create_plot(user_reaction_times, average_user_reaction_times)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

@app.route('/api/<test_name>')
def get_data(test_name):
    if test_name == 'reaction-time':
        user_reaction_times, _ = get_reaction_times()
        data = {
            'points': np.mean(user_reaction_times),
            'percentile': np.percentile(user_reaction_times, 50)
        }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
