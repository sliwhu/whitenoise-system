import burdock.mechanisms.random as rand
from burdock.mechanisms.base import AdditiveNoiseMechanism
from scipy.stats import laplace
from burdock.metadata.release import Result, Interval, Intervals


class Laplace(AdditiveNoiseMechanism):
    def __init__(self, eps, delta=None, sensitivity=1.0, max_contrib=1, alphas=[0.95], rows=None):
        super().__init__(eps, 0, sensitivity, max_contrib, alphas, rows)
        self.scale = (self.max_contrib * self.sensitivity) / self.eps

    def release(self, vals, compute_accuracy=False, bootstrap=False):
        noise = rand.laplace(0.0, self.scale, len(vals))
        reported_vals = noise + vals
        mechanism = "Laplace"
        statistic = "additive_noise"
        source = None
        epsilon = self.eps
        delta = self.delta
        sensitivity = self.sensitivity
        max_contrib = self.max_contrib
        accuracy = None
        intervals = None
        if compute_accuracy:
            bounds = self.bounds(bootstrap)
            accuracy = [(hi - lo) / 2.0 for lo, hi in bounds]
            intervals = Intervals([Interval(alpha, accuracy) for alpha, accuracy in zip(self.alphas, accuracy)])
            intervals.extend(reported_vals)
        return Result(mechanism, statistic, source, reported_vals, epsilon, delta, sensitivity, self.scale, max_contrib, intervals)


    def bounds(self, bootstrap=False):
        if not bootstrap:
            _bounds = []
            for a in self.alphas:
                edge = (1 - a) / 2.0
                _bounds.append( laplace.ppf([edge, 1 - edge], 0.0, self.scale))
            return _bounds
        else:
            return super().bounds(bootstrap)
