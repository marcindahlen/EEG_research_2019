"""
Main node of the experiment.

I assume following files hierarchy:
    root/
        in_raw/
            P01.txt
            .
            .
            .
            P32.txt
        in_raw_channels/
            P01CH01
            P01CH02
            .
            .
            .
            P32Ch14
        out_raw/
            main_alpha-index_base.xls
            out_absData.xls
        out_wykresy/

        python/
            dataIO/
            networks/
            tests/
            utils/
            badanie_Main.py
            main.py
        net_memory/

"""

"""
    x = [i for i in range(len(output_scores))]
            trace = graph_objs.Scatter(x=x, y=output_scores)
            plotly.offline.plot(trace, filename=variables.out_charts_path + 'name.html', auto_open=False) # @TODO filenaming needs parametrisation
"""

"""
    → https://superuser.com/questions/679679/how-to-increase-pythons-cpu-usage
    → https://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python
"""

"""
    → https://en.wikipedia.org/wiki/Data_stream_management_system#Synopses  !!!
    It is possible to use another method for data reading, other than windows,
    and given the nature of eeg it might be highly desirable to use it.
    
    The idea behind compression techniques is to maintain only a synopsis of the data, 
    but not all (raw) data points of the data stream. The algorithms range from selecting 
    random data points called sampling to summarisation using histograms, wavelets 
    or sketching. One simple example of a compression is the continuous calculation 
    of an average. Instead of memorizing each data point, the synopsis only holds 
    the sum and the number of items. The average can be calculated by dividing 
    the sum by the number. However, it should be mentioned that synopses cannot reflect 
    the data accurately. Thus, a processing that is based on synopses may produce inaccurate results.
"""

"""
    I can use two types of neuron: classic and LSTM.
    But LSTMs are pointless in one-time-look on data, they don't have occasion to remember anything.
    Should I implement GRUs?
    
    What about LSTM gives final output after looking at all channels?
    
    There are some cases:
    neurons: classic vs LSTM (vs GRU)
    viewpoint:  single whole channel → verdict; few whole channels → verdict; scanning channel in parts → verdict;
                scanning channels in parallel → verdict;
        A nice table of comparison emerges from the above.
        
    Outputs could be evaluated in many different ways.
    There could be 10 output neurons, each one responsible for its own 'range of correctness:
    for real output 14, neuron no. 2 should fire, rest should be silent.
    But there could be also a single output neuron giving answers in its range <0, 1> where
    real output 14 would be a 0.14 answer. 
    Second approach could be more "trainable".
    This adds new depth to "a nice table of comparison".
"""

"""
Decide to use 3-fold cross validation vs 6-fold cross validation.
Citation about estimating network performance on larger dataset most welcome.
"""