from datetime import datetime

LOG_FILE = 'performance_log.txt'

def log_performance(cycle, user_id, recommendations, score, top_n):
    with open(LOG_FILE, 'a') as log:
        log_entry = (f"{datetime.now()} - Cycle: {cycle}, User: {user_id}, "
                     f"Recommendations: {recommendations}, "
                     f"Score: {score}, Next Top_n: {top_n}\n")
        log.write(log_entry)
