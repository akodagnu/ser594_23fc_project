import wf_visualization
import wf_dataprocessing

def core():
    wf_dataprocessing.process()
    wf_visualization.visualize()

if __name__ == '__main__':
    core()