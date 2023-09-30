from service.token_bucket_impl import TokenBucketImpl
from service.sliding_window_counter_impl import SlidingWindowCounterImpl
from service.fixed_window_counter_impl import FixedWindowCounterImpl

class AlgoFactory:
    def getAlgo(self, algo_type):
        if algo_type == 'fixedWindow':
            print("fixed window")
            return FixedWindowCounterImpl()
        elif algo_type == 'tokenBucket':
            print('token bucket')
            return TokenBucketImpl()
        else:
            raise ValueError("Invalid algorithm type")