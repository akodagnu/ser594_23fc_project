import wf_visualization
import wf_dataprocessing

def core():
    wf_dataprocessing.process()
    wf_visualization.visualize()

core()