import streamlit as st
from sympy import Symbol
from sympy.solvers import solve
from sympy.core import sympify


def solver(exp: str) -> dict:
    cvt_exp = ""
    exp_list = exp.splitlines()
    for e in exp_list:
        e_list = e.split("=")
        cvt_exp += f"Eq({e_list[0]},{e_list[1]}),"

    return solve(sympify(cvt_exp))


exp = st.text_area("請輸入聯立方程式：", "x + y = 16\n10 * x + 50 * y = 560")

if st.button("求解"):
    ans = solver(exp)

    st.write('結果：')
    for k, v in ans.items():
        st.write(Symbol(f'{k} = {v}'))
