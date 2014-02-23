#!/usr/bin/python

# ------------------------------------------------
#- generate a list of Trade objs from a a Trx series
#-------------------------------------------------




trxstream = [1,2,-5,3,-2]

basislist = trxstream[0]

lambda same_sign

trxstream = [1,2,-5,3,-2]

def gen-trades:
    input: [trxs[trades]
"""
when u are all done you will get a list of Trades with the computed bais
then we compute pnl for each trade by offseting the offset trades with the basis trade

Trade list extractin

key is Basis assignment
start with element in the trxtream
if next trx in the stream is not of samesing add to offset list while offeset lte basis
if same sign add to basislist
split the last offeseting trx moving reminder to the next Trade
if there are no more basis on the list but we still have streamtrx the next element is the basis (can be negative)
