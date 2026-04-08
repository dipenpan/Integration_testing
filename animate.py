import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Plotly Animation Demo", layout="wide")

st.title("Plotly Animations in Streamlit")
st.write(
    "This app demonstrates several Plotly animations built with frames. "
    "I kept the original animations and added a new custom animation."
)

animation_choice = st.selectbox(
    "Choose an animation",
    [
        "Rotating 3D Helix",
        "Moving Sine Wave",
        "Bouncing Ball",
        "Multiple Bouncing Balls",
    ],
)

num_frames = 80


def rotating_3d_helix():
    t = np.linspace(0, 8 * np.pi, 300)
    x = np.cos(t)
    y = np.sin(t)
    z = np.linspace(-2, 2, 300)

    frames = []
    for i in range(num_frames):
        angle = 2 * np.pi * i / num_frames
        x_rot = x * np.cos(angle) - y * np.sin(angle)
        y_rot = x * np.sin(angle) + y * np.cos(angle)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter3d(
                        x=x_rot,
                        y=y_rot,
                        z=z,
                        mode="lines",
                        line=dict(width=8, color=z, colorscale="Turbo"),
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=x,
                y=y,
                z=z,
                mode="lines",
                line=dict(width=8, color=z, colorscale="Turbo"),
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Rotating 3D Helix",
        scene=dict(
            xaxis=dict(range=[-1.5, 1.5], title="X"),
            yaxis=dict(range=[-1.5, 1.5], title="Y"),
            zaxis=dict(range=[-2.5, 2.5], title="Z"),
            aspectmode="cube",
            camera=dict(eye=dict(x=1.6, y=1.6, z=1.1)),
        ),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 45, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def moving_sine_wave():
    x = np.linspace(0, 4 * np.pi, 400)

    frames = []
    for i in range(num_frames):
        phase = 2 * np.pi * i / num_frames
        y = np.sin(x + phase)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=x,
                        y=y,
                        mode="lines",
                        line=dict(width=4),
                        fill="tozeroy",
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=np.sin(x),
                mode="lines",
                line=dict(width=4),
                fill="tozeroy",
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Moving Sine Wave",
        xaxis=dict(range=[0, 4 * np.pi], title="x"),
        yaxis=dict(range=[-1.5, 1.5], title="sin(x)"),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 45, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def bouncing_ball():
    x_positions = np.linspace(0, 10, num_frames)
    y_positions = np.abs(np.sin(np.linspace(0, 3 * np.pi, num_frames))) * 5

    frames = []
    for i in range(num_frames):
        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=[x_positions[i]],
                        y=[y_positions[i]],
                        mode="markers",
                        marker=dict(size=24, color=[y_positions[i]], colorscale="Plasma"),
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=[x_positions[0]],
                y=[y_positions[0]],
                mode="markers",
                marker=dict(size=24, color=[y_positions[0]], colorscale="Plasma"),
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Bouncing Ball",
        xaxis=dict(range=[0, 10], title="X Position"),
        yaxis=dict(range=[0, 6], title="Height"),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 55, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def multiple_bouncing_balls():
    num_balls = 6
    x_base = np.linspace(1, 9, num_balls)
    phases = np.linspace(0, np.pi, num_balls)

    frames = []
    for i in range(num_frames):
        t = i / num_frames * 3 * np.pi
        y = np.abs(np.sin(t + phases)) * 5

        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=x_base,
                        y=y,
                        mode="markers",
                        marker=dict(
                            size=22,
                            color=y,
                            colorscale="Rainbow",
                        ),
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=x_base,
                y=np.abs(np.sin(phases)) * 5,
                mode="markers",
                marker=dict(
                    size=22,
                    color=np.abs(np.sin(phases)) * 5,
                    colorscale="Rainbow",
                ),
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Multiple Bouncing Balls",
        xaxis=dict(range=[0, 10], title="X Position"),
        yaxis=dict(range=[0, 6], title="Height"),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


if animation_choice == "Rotating 3D Helix":
    fig = rotating_3d_helix()
elif animation_choice == "Moving Sine Wave":
    fig = moving_sine_wave()
elif animation_choice == "Bouncing Ball":
    fig = bouncing_ball()
else:
    fig = multiple_bouncing_balls()

st.plotly_chart(fig, use_container_width=True)