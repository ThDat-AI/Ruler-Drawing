import streamlit as st
import matplotlib.pyplot as plt
import time

st.set_page_config(layout="wide") 

# Thuật toán
def draw_ruler(ax, chart, A, B, H):
    if H == 0 or B <= A:
        return

    mid = (A + B) / 2
    ax.vlines(mid, 0, H, colors='blue')
    chart.pyplot(fig, dpi = 200)
    time.sleep(0.3)

    draw_ruler(ax, chart, A, mid, H - 1)
    draw_ruler(ax, chart, mid, B, H - 1)

# Giao diện
st.title("📏 Ruler Drawing")

col1, col2 = st.columns([1, 3]) 

with col1:
    A = st.number_input("Điểm A (bắt đầu)", min_value = 0.0, value = 0.0, format = "%.2f")
    B = st.number_input("Điểm B (kết thúc)", min_value = A + 5, max_value = A + 200.00, value = 10.0, format = "%.2f")
    H = st.number_input("Chiều cao H (độ sâu vạch)", min_value = 0, max_value = 10, value = 5, step = 1)

    draw = st.button("🎨 Vẽ thước")

with col2:
    chart = st.empty()
    if draw:
        if A >= B:
            st.error("⚠️ A phải nhỏ hơn B")
        else:
            fig, ax = plt.subplots(figsize = (12, 3), dpi = 200) 

            ax.set_ylim(0, H + 1)
            ax.set_xlim(A - 1, B + 1)
            ax.hlines(0, A, B, colors='black', linewidth = 2)

            if B - A <= 100:
                ticks = [round(x, 2) for x in 
                         [A + i * (B - A) / 20 for i in range(21)]]
                ax.set_xticks(ticks)
                ax.set_xticklabels([f"{x:.2f}" for x in ticks], fontsize=8)

            draw_ruler(ax, chart, A, B, H)
