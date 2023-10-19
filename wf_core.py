import wf_visualization
import wf_dataprocessing

# Note: It will probably take some time to execute. Wait for all the plots to be completed before reviewing.
def core():
    wf_dataprocessing.process()
    wf_visualization.visualize()

if __name__ == '__main__':
    core()