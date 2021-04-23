import ipywidgets

def plotlysaurus(dataset='dino'):
    fig = go.Figure()

    localdf = dinodf[dinodf.dataset==dataset]

    fig.add_trace(go.Scatter(
        x=localdf.x,
        y=localdf.y,
        mode='markers',
        marker=dict(
            size=16,
            color=np.random.randn(500), #set color equal to a variable
            colorscale='rainbow', # one of plotly colorscales
            showscale=True
        )
    ))
    
    return fig
    
ipywidgets.interact(plotlysaurus,dataset=dinodf.dataset.unique());