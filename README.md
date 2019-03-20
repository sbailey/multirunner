# multirunner


This repo demos a design pattern for using a multi-core machine to process incoming data in parallel using multiprocessing.  A single server process monitors a directory for new data and puts filenames into a queue as they arrive.  Multiple worker processes pull filenames from that queue, with the multiprocessing library guaranteeing that each filename is only given to a single worker.

This is not intended to be a generic library to be used as an external dependency, nor is it intended to be super fault-toleratant, scalable, etc.  But it is intended to be lightweight, simple, and serverless, and it may suit your needs.  Copy-and-paste it and modify it to match the details of your particular problem.

## Demo

In one window:
```
mkdir test
python multirunner.py --indir test/ --numworkers 4 --waittime 2
```

In a different window, add files to the directory, waiting in between:
```
cd test
touch a b c d e f
touch g h
touch j k
```

You should see something like this in the first window:
```
Worker 0 ready to go
Worker 2 ready to go
Worker 1 ready to go
Worker 3 ready to go
Server putting test/a in the queue
Server putting test/f in the queue
Server putting test/c in the queue
Server putting test/d in the queue
Worker 0 processing test/a
Server putting test/e in the queue
Server putting test/b in the queue
Worker 1 processing test/f
Worker 2 processing test/c
Worker 3 processing test/d
Worker 2 done with test/c
Worker 1 done with test/f
Worker 0 done with test/a
Worker 3 done with test/d
Worker 2 processing test/e
Worker 1 processing test/b
Server putting test/g in the queue
Server putting test/h in the queue
Worker 0 processing test/g
Worker 3 processing test/h
Worker 2 done with test/e
Worker 1 done with test/b
Server putting test/j in the queue
Server putting test/k in the queue
Worker 2 processing test/j
Worker 1 processing test/k
Worker 0 done with test/g
Worker 3 done with test/h
Worker 2 done with test/j
Worker 1 done with test/k
```

<hr/>
Stephen Bailey<br/>
Lawrence Berkeley National Lab<br/>
March 2019<br/>

