import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Hello World LinoGi mit Matplotlib & Streamlit")

diagramm = st.selectbox(
    "Wähle ein Diagramm aus:",
    ("Linienplot", "Scatterplot", "Histogramm", "Interaktiver Plot")
)

x = np.linspace(0, 10, 100)

if diagramm == "Linienplot":
    st.write("## 1. Einfacher Linienplot")
    fig1, ax1 = plt.subplots()
    y = np.sin(x)
    ax1.plot(x, y, label="sin(x)")
    ax1.set_title("Sinuskurve")
    ax1.set_xlabel("x")
    ax1.set_ylabel("sin(x)")
    ax1.legend()
    st.pyplot(fig1)

elif diagramm == "Scatterplot":
    st.write("## 2. Scatterplot mit zufälligen Daten")
    fig2, ax2 = plt.subplots()
    np.random.seed(42)
    x2 = np.random.rand(100)
    y2 = np.random.rand(100)
    colors = np.random.rand(100)
    sizes = 1000 * np.random.rand(100)
    scatter = ax2.scatter(x2, y2, c=colors, s=sizes, alpha=0.5, cmap='viridis')
    ax2.set_title("Scatterplot")
    fig2.colorbar(scatter, ax=ax2)
    st.pyplot(fig2)

elif diagramm == "Histogramm":
    st.write("## 3. Histogramm")
    fig3, ax3 = plt.subplots()
    data = np.random.randn(1000)
    ax3.hist(data, bins=30, color='skyblue', edgecolor='black')
    ax3.set_title("Histogramm einer Normalverteilung")
    st.pyplot(fig3)

elif diagramm == "Interaktiver Plot":
    st.write("## 4. Interaktiver Plot")
    freq = st.slider("Frequenz", 1, 10, 3)
    fig4, ax4 = plt.subplots()
    ax4.plot(x, np.sin(freq * x), label=f"sin({freq}x)", color='red')
    ax4.set_title("Interaktiver Sinusplot")
    ax4.legend()
    st.pyplot(fig4)

st.write("### Matplotlib bietet viele Möglichkeiten zur Anpassung von Plots, Farben, Achsen, Legenden und mehr!")
