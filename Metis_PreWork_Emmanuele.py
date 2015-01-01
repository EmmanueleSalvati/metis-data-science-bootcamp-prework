"""Metis Pre-work:
Think Stats Exercise 2.4"""

from first import MakeFrames
from thinkstats2 import CohenEffectSize
import thinkstats2
import thinkplot
import sys
import probability


def ReadFrame(dct_file='2002FemResp.dct', dat_file='2002FemResp.dat.gz'):
    """Read the input DataFrame"""
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')

    return df


def Ex24():
    """Exercise 2.4"""
    (live, firsts, others) = MakeFrames()
    print 'first borns mean weight: %.2f' % firsts.totalwgt_lb.mean()
    print 'others mean weight: %.2f' % others.totalwgt_lb.mean()

    print 'Cohen\'s d: %.3f' % CohenEffectSize(firsts.totalwgt_lb,
                                               others.totalwgt_lb)


def Ex31():
    """Exercise 3.1"""
    print "Starting Ex. 3.1"
    df = ReadFrame()
    kids = df.numkdhh
    pmf = thinkstats2.Pmf(kids, label='actual')
    biased_pmf = probability.BiasPmf(pmf, label='observed')
    thinkplot.PrePlot(2)
    thinkplot.Pmfs([pmf, biased_pmf])
    thinkplot.Save(root='Ex31_Pmf', formats=['pdf'],
                   xlabel='children',
                   ylabel='PMF')
    print 'Mean of actual number of children: %.2f' % (pmf.Mean())
    print 'Mean of biased number of children: %.2f' % (biased_pmf.Mean())


if __name__ == "__main__":
    if sys.argv[1] == "24":
        Ex24()
    elif sys.argv[1] == "31":
        Ex31()
