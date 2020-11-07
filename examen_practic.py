"""
A shoe factory needs an iterable object to keep track of shoes produces by each worker each day.
Each worker has a string name and each shoe has an int serial number.
Object will have an instance variable tha will keep track of workers trying to cheat.
Iterating the object will return the serial numbers produced that day by all workers

1) Definition: 40p
    a) Class with constructor that receives the date in the format you desire. 5p
    b) Method for adding work done by worker: 25p
        - argument 1 receives worker name as string, argument 2 receives series produced as list of ints 5p
        - using this method more then once worker series can be added or retransmitted (ex name1: 100, 101; name1: 101, 102; rezulta name1: 100, 101, 102) 5p
        - method validates that series introduced do not already belong to another worker 5p
        - in case of conflict method raises ValueError with message: "Conflict series: <series>, Workers: <nume1>, <nume2>" 5p
        - conflicting series will be removed from both workers and information will be added to instance variable that tracks cheating workers 5p
    c) Iterating this object will return an instance of in iterator that will have all the series produced that day: 10p

2) Execution: 40p
    a) Create instance of class with date format you selected. 10p
    b) Add data for the following workers: 10p
     - Joe: 402, 403, 409
     - Ana: 399, 404, 405
     - Tim: 400, 401, 406
     - workerX: 406, 407, 408 - after adding workerX, workerX will have 407, 408 and Tim will have [400, 401]
    c) Print the workers that are trying to cheat
    c) Iterate the created object and save each value on a new line in a file. 10p

3) Documenting: 20p
   a) type hints for all arguments 5p
   a) module documentation 5p
   b) class documentation for all classes 5p
   c) method documentation fro all methods 5p
"""

from datetime import date


class Factory:
    """
    class to check worers and series
"""

    def __init__(self, workers={}):
        """
        :param workers: dictionary with workers
        """
        self.day = date.today().strftime('%d/%m/%Y')
        self.workers=workers

    def add_work_day(self, worker_name, produced_series):
        """
        :param worker_name: name of the worker
        :param produced_series: worker and it series
        :return:
        """
        self.workers[worker_name] = produced_series
        self.workers[worker_name] = sorted(self.workers[worker_name])
        print(self.workers[worker_name])
        lent=int(len((self.workers[worker_name])))
        print(lent)
        print(lent-1)
        for series in range(0,lent-1):
            for count in range(1,lent):
                print("series is", series)
                print("count is",count)
                print("value is", self.workers[worker_name][series])
                # if self.workers[worker_name][series] == self.workers[worker_name][count]:
                #     del self.workers[worker_name][series]
                # else:
                #     print("The same")
                 # print("count is",self.workers[worker_name][count])

        print(self.workers)

    def __iter__(self):
        return self.workers


obj=Factory()
obj.add_work_day('Joe', [402, 403, 409])
obj.add_work_day('Joe', [402, 403, 419])
# obj.add_work_day('Ana', [399, 404, 405])
# obj.add_work_day('Tim', [400, 401, 406])
# obj.add_work_day('Ana',[399, 404, 405])