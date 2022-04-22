import numpy as np

n = 10000
s1, s2 = 0.3, 0.2
p, q, r = 0.4, 0.6, 0.8
[n1, n2, n3] = np.random.multinomial(n, [s1, s2, 1-s1-s2])
h1 = np.random.binomial(n1, p)
h2 = np.random.binomial(n2, q)
h3 = np.random.binomial(n3, r)
h = h1 + h2 + h3
t = n - h
print("h={}, t={}, f={}".format(h, t, h/n))

p_est, q_est, r_est = 0.4, 0.6, 0.8
s1_est, s2_est = 0.3, 0.2
delta, eps = 1, 1e-18
while delta > eps:
    po, qo, ro = p_est, q_est, r_est
    htmp = s1_est*p_est + s2_est*q_est + (1-s1_est-s2_est)*r_est
    ttmp = 1 - htmp
    sumh1, sumt1 = s1_est*p_est/htmp*h, s1_est*(1-p_est)/ttmp*t
    sumh2, sumt2 = s2_est*q_est/htmp*h, s2_est*(1-q_est)/ttmp*t
    summiu1, summiu2 = sumh1+sumt1, sumh2+sumt2
    s1_est, s2_est = summiu1/n, summiu2/n
    p_est, q_est, r_est = sumh1/summiu1, sumh2/summiu2, (h-sumh1-sumh2)/(n-summiu1-summiu2)
    delta = abs(p_est-po)+abs(q_est-qo)+abs(r_est-ro)
    print("p={}, q={}, r={}, s1={}, s2={}, E={}".format(p_est, q_est, r_est, s1_est, s2_est,
                                                        p_est*s1_est+q_est*s2_est+r_est*(1-s1_est-s2_est)))
