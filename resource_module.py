import time
import psutil

def track_resources():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    return cpu_usage, memory_usage

def resource_report():
    cpu, memory = track_resources()
    return f"CPU Usage: {cpu}%, Memory Usage: {memory}%"
