from badanie import Badanie
from datastorage import Datastorage
import variables
import plotly.graph_objs


data = Datastorage()

data.prepare_input()

#data.show_summary()

b = Badanie(1, data)

print("Assumed iterations: " + str(data.assume_networkIterationsNo()))

wyniki = b.forward_pass_all_networks(data.assume_networkIterationsNo())

print(wyniki)