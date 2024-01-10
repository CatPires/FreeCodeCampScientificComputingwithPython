import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self,**kwargs):
        if sum(kwargs.values()) > 0:
            self.contents = [k for k,v in kwargs.items() for i in range(v)]
        else:
            raise ValueError('ERROR: No balls in the Hat')
    
    def draw(self,balls_draw):
        if balls_draw > len(self.contents):
            return self.contents
        else:
            remov_list = []
            for i in range(balls_draw):
                #my_elements = self.contents.copy()
                random_item_from_list = random.choice(range(len(self.contents)))
                removed = self.contents.pop(random_item_from_list)
                remov_list.append(removed)
            return remov_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    results = []
    for i in range(num_experiments):
        my_hat = copy.deepcopy(hat) #.contents.copy()
        results.append(my_hat.draw(num_balls_drawn))

    fre_results = []
    for draw in results:
        freq = {}
        for ball in draw:
            if ball in freq:
                freq[ball] += 1
            else:
                freq[ball] = 1
        fre_results.append(freq)

    sucess_attemp = 0
    for dra in fre_results:
        cnt = 0
        for ball in expected_balls:    
            if ball in dra:
                if expected_balls[ball] <= dra[ball]:
                    cnt += 1
        
        if cnt == len(expected_balls):
            sucess_attemp += 1
    
    return sucess_attemp/num_experiments