#!/usr/bin/env python

"""
Multirunner example

Stephen Bailey
Lawrence Berkeley National Lab
March 2019
"""

import sys, os, time
import multiprocessing as mp
import argparse
import glob

parser = argparse.ArgumentParser(usage = "{prog} [options]")
parser.add_argument("-i", "--indir", type=str,  help="input directory")
parser.add_argument("-n", "--numworkers", type=int,  default=4, help="number of workers")
parser.add_argument("-w", "--waittime", type=int, default=5, help="wait time between directory checks")
args = parser.parse_args()

#- Create communication queue to pass files to workers
q = mp.Queue()

#- Function to run for each worker.
#- Listens on Queue q for filenames to process.
def run(workerid, q):
    print('Worker {} ready to go'.format(workerid))
    while True:
        filename = q.get(block=True)
        print('Worker {} processing {}'.format(workerid, filename))
        sys.stdout.flush()
        #- Do something with that filename; in this case just sleep
        time.sleep(5)
        print('Worker {} done with {}'.format(workerid, filename))
        sys.stdout.flush()

#- Start workers
for i in range(args.numworkers):
    p = mp.Process(target=run, args=(i, q))
    p.start()

#- Track what files have already been added to queue.
#- TODO: Upon startup, this could compare against files in output dir
#- and only load input files haven't already been processed.
known_files = set()

#- Periodically check for any new files that may have appeared and add them
#- to the queue for a worker to process.
glob_pattern = os.path.join(args.indir, '*')
while(True):
    for filename in glob.glob(glob_pattern):
        if filename not in known_files:
            print('Server putting {} in the queue'.format(filename))
            sys.stdout.flush()
            q.put(filename)
            known_files.add(filename)

    time.sleep(args.waittime)
