import ipywidgets
dinodf = pd.read_csv('data/DatasaurusDozen.tsv',sep='\t')

def chartosaurus(dataset='dino'):
    localdf = dinodf[dinodf.dataset==dataset]
    points = alt.Chart(localdf).mark_point().encode(
        x='x',
        y='y'
    ).add_selection(
        my_si
    )

    barsX = alt.Chart(localdf).mark_bar().encode(
        alt.X('x',bin=True, scale=alt.Scale(domain=[0, 100])),
        y='count()'
    ).transform_filter(
        my_si
    )

    barsY = alt.Chart(localdf).mark_bar().encode(
        alt.Y('y',bin=True, scale=alt.Scale(domain=[0, 100])),
        x='count()'
    ).transform_filter(
        my_si
    )

    chart = alt.vconcat(barsX,
                alt.hconcat(points,barsY))
    
    return chart
    
ipywidgets.interact(chartosaurus,dataset=dinodf.dataset.unique());