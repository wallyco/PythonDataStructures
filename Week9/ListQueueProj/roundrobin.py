from listqueue import ListQueue


def round_robin(job_queue):
    """ Each job in the job queue has a time slice of
    10 time units. An unfinished job will be returned
    to the rear of the queue. """
    time = 10
    if job_queue.isEmpty():
        return
    else:
        process = job_queue.peek()
        print("Job queue:" + str(job_queue))
        print("Current job: %d" % process)
        if process < time:
            time = process
        while time > 0:
            process -= 1
            time -= 1
            if process == 0:
                print("Job finished \n")
                job_queue.pop()
            elif time == 0:
                print("Job unfinished \n")
                job_queue.pop()
                job_queue.add(process)
        round_robin(job_queue)


def test_round_robin():
    job_list = [17, 5, 32, 8, 24]
    job_queue = ListQueue(job_list)
    print("Initial job queue:", job_queue)
    round_robin(job_queue)


test_round_robin()
