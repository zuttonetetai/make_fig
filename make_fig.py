import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

def plt_plot(
        data_list, 
        data_label_list, 
        color=['r', 'g', 'b', 'c'], 
        x_axis_title='Time [sec]', 
        y_axis_title='adcSteer', 
        legend=None,
        figsize=(17, 6),
        auto_adjust=False, 
        save_file=None,
        fs=None,
        ax=True,
        linewidth=1
    ):
    """
    Input:
      data_list:
      data_label_list:
      color:
      x_axis_title:
      y_axis_title:
      legend: 'inner' or 'outer' or None
      figsize:
      auto_adjust:
      save_file: file name(str)
      fs: sampling rate (convert x-axis label to Time label)
      ax: use instance plot instead of plt plot
    """
    if ax:
        fig = Figure(figsize=figsize)
        ax = fig.subplots()

        for data, name, c in zip(data_list, data_label_list, color):
            if auto_adjust:
                data += float(data_list[0].mean() - data.mean())
            if fs != None:
                ax.plot([x/fs for x in range(len(data))], data, label=name, color=c, linewidth=linewidth)
            else:
                ax.plot(range(len(data)), data, label=name, color=c, linewidth=linewidth)

        #ax.set_xlim(0, 20)
        ax.set_xlabel(x_axis_title)
        ax.set_ylabel(y_axis_title)

        if legend != None:
            if legend == 'inner':
                ax.legend(loc='best')
            elif legend == 'outer':
                ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)
        ax.grid(True)
        if save_file != None:
            fig.savefig(save_file,  bbox_inches='tight')
        return fig

    else:
        fig = plt.figure(figsize=figsize)
        for data, label ,c in zip(data_list, data_label_list, color):
            if auto_adjust:
                data += float(data_list[0].mean() - data.mean())
            if fs != None:
                plt.plot([x/fs for x in range(len(data))], data, label=label, color=c, linewidth=linewidth)
            else:
                plt.plot(range(len(data)), data, label=label, color=c, linewidth=linewidth)
            
        # ??????????????????
        #xlocs, _ = plt.xticks()
        #plt.xticks(xlocs, [str(x/2000) for x in xlocs])

        if legend != None:
            if legend == 'inner':
                plt.legend(loc='best')
            elif legend == 'outer':
                plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)


        plt.xlabel(x_axis_title)
        plt.ylabel(y_axis_title)
        
        #_min = min(data1) if min(data1) < min(data2) else min(data2)
        #_max = max(data1) if max(data1) > max(data2) else max(data2)
        #s = abs(_max - _min)/2
        #plt.ylim(_min-s/2, _max+s/10)
        plt.grid(True)

        if save_file != None:
            fig.savefig(save_file,  bbox_inches='tight')
        return fig
