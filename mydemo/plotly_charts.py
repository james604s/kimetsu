import datetime
import glob
import logging
import os

import numpy as np
import plotly.graph_objs as go
from plotly.graph_objs import Scatter,Bar
from plotly.offline import plot

logger = logging.getLogger(__name__)
# animals=['giraffes', 'orangutans', 'monkeys']

# fig = go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
# fig.show()
def test1():
    # x_data = [0,1,2,3]
    # y_data = [x**2 for x in x_data]
    # plot_div = plot([Scatter(x=x_data, y=y_data,
    #                         mode='lines', name='test',
    #                         opacity=0.8, marker_color='green')],
    #             output_type='div')
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Bar(x=x_data, y=y_data
                            #, mode='lines'
                            , name='test'
                            , opacity=0.8
                            , marker_color='green')],
                output_type='div')
    return plot_div

def plot1d():
    x_data = np.arange(0, 120, 0.1)
    trace1 = go.Scatter(
        x=x_data,
        y=np.sin(x_data)
    )

    data = [trace1]
    layout = go.Layout(
        # autosize=False,
        # width=900,
        # height=500,

        xaxis=dict(
            autorange=True
        ),
        yaxis=dict(
            autorange=True
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=True)
    logger.info("Plotting number of points {}.".format(len(x_data)))
    return plot_div