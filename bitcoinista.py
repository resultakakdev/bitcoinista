import sys
import bitcoinista

mode = 'demo'
if __name__ == '__main__':
    # Pythonista resets recursion 
    # limit to 256 in the interpreter
    # so we need to force it here
    reclimit = sys.getrecursionlimit()
    if reclimit > 1000:
        sys.setrecursionlimit(1000)
    ctrl = bitcoinista.TextController(mode)
    try:
        ctrl.run()
    except Exception as e:
        print 'An error occurred: {0}'.format(e)
