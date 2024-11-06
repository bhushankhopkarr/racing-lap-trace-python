import os
import plotly.graph_objects as go
import json
from plotly.subplots import make_subplots

def load_data(filename):
    file_path = os.path.join('data', filename)
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data.")
        return None

def create_chart(distance, steering, gears, throttle, braking, speed):
    fig = make_subplots(
        rows=5, cols=1, shared_xaxes=True, vertical_spacing=0.02,
        row_heights=[1, 3, 1, 1, 1]
    )

    data = {
        'Steering': steering,
        'Speed (mph)': speed,
        'Gears': gears,
        'Throttle (%)': throttle,
        'Braking (%)': braking
    }

    for i, (name, y_data) in enumerate(data.items(), start=1):
        fig.add_trace(go.Scatter(x=distance, y=y_data, mode='lines', name=name), row=i, col=1)

    fig.update_layout(
        height=1000,
        title_text="Lap Trace Data",
        paper_bgcolor='black',
        plot_bgcolor='#171717',
        font=dict(color='white'),
    )

    fig.update_xaxes(showgrid=False, title_text='Distance (m)', row=5, col=1)
    fig.update_yaxes(showgrid=False, zeroline=False, zerolinewidth=2)

    fig.show()

def main():
    data = load_data('lap.json')
    if data is None:
        return

    lap_distance = [entry['lap_distance'] for entry in data]
    steering = [entry['steering'] for entry in data]
    gears = [entry['gear'] for entry in data]
    throttle = [entry['throttle'] * 100 for entry in data]
    braking = [entry['brake'] * 100 for entry in data]
    speed = [entry['speed'] for entry in data]

    create_chart(lap_distance, steering, gears, throttle, braking, speed)

if __name__ == '__main__':
    main()