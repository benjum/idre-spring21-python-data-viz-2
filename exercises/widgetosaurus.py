def widgetosaurus(dataset='dino'):
    fig,ax = plt.subplots(2,2,figsize=(8,8))

    x = dinodf[dinodf.dataset==dataset].x
    y = dinodf[dinodf.dataset==dataset].y

    ax[1,0].scatter(x, y)

    ax[0,0].hist(x, bins=10, rwidth=0.9)
    ax[1,1].hist(y, bins=10, rwidth=0.9, orientation='horizontal')

    ax[0,1].text(0.2,0.8,'x_mean = {:.2f}'.format(x.mean()))
    ax[0,1].text(0.2,0.7,'x_stddev = {:.2f}'.format(x.std()))
    ax[0,1].text(0.2,0.6,'y_mean = {:.2f}'.format(y.mean()))
    ax[0,1].text(0.2,0.5,'y_stddev = {:.2f}'.format(y.std()))
    ax[0,1].text(0.2,0.4,'corr = {:.2f}'.format(x.corr(y)))

    fig.show()
    
ipywidgets.interact(widgetosaurus, dataset=dinodf.dataset.unique());