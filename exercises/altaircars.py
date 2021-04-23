from vega_datasets import data
cars = data.cars()

my_si = alt.selection_interval()

points = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
).add_selection(
    my_si
)

bars = alt.Chart(cars).mark_bar().encode(
    x='count(Origin)',
    y='Origin',
    color='Origin'
).transform_filter(
    my_si
)

points & bars