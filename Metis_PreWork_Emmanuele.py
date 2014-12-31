"""Metis Pre-work:
Think Stats Exercise 2.4"""

from first import MakeFrames
from thinkstats2 import CohenEffectSize


if __name__ == "__main__":

    (live, firsts, others) = MakeFrames()
    print 'first borns mean weight: %.2f' % firsts.totalwgt_lb.mean()
    print 'others mean weight: %.2f' % others.totalwgt_lb.mean()

    print 'Cohen\'s d: %.3f' % CohenEffectSize(firsts.totalwgt_lb,
                                               others.totalwgt_lb)
