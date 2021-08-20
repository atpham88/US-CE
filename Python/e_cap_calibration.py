from sympy import Symbol, solve, nsolve

year_begin = 2020
year_end = 2050
year_mid = 2040
cap_begin = 130594820
cap_end = 0

m = Symbol('m')
c = Symbol('c')

results = nsolve([(m/2)*year_begin**2 + c*year_begin - cap_begin, (m/2)*year_end**2 + c*year_end - cap_end], [m, c], [1, 1])

m_star = results[0]
c_star = results[1]
#print(equations((m, c)))

# Check:
(m_star/2)*year_begin**2 + c_star*year_begin == cap_begin
(m_star/2)*year_end**2 + c_star*year_end == cap_end
(m_star/2)*year_mid**2 + c_star*year_mid
