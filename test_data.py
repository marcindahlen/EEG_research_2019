from populacja import Populacja
import variables
import plotly.graph_objs

b = Populacja(0)

data = b.input_examined['P08.txt'][16]
print(data)

data = b.output_examined['P08.txt']
print(data)

x = [i for i in range(len(data))]
trace = plotly.graph_objs.Scatter(x=x, y=data)
plot_data = [trace]
figure = plotly.graph_objs.Figure(data=plot_data)
plotly.offline.plot(figure, filename=variables.out_charts_path + "badanie" + '.html', auto_open=False)
