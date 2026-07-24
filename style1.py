import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    /* Entire Dashboard */
    .stApp{
        background: linear-gradient(180deg,#0A7AB3,#153A81);
        color:white;
    }

    /* Sidebar */
    [data-testid="stSidebar"]{
        background: linear-gradient(180deg,#06152E,#123C73);
        border-right:2px solid #4FC3F7;
    }

    /* Sidebar Text */
    [data-testid="stSidebar"] *{
        color:white !important;
    }

    /* Headings */
    h1,h2,h3,h4,h5,h6{
        color:#FFFFFF !important;
    }
                
    h2{
            color:#FFFFFF !important;    
                }

    /* Paragraph */
    p{
        color:#E3F2FD !important;
    }

    /* Markdown */
    .stMarkdown{
        color:white !important;
    }

    /* Metric Cards */
    [data-testid="stMetric"]{
        background:#103E74;
        padding:18px;
        border-radius:15px;
        border:1px solid #4FC3F7;
        box-shadow:0px 0px 20px rgba(79,195,247,.35);
    }

    [data-testid="stMetricLabel"]{
        color:white !important;
    }

    [data-testid="stMetricValue"]{
        color:#4FC3F7 !important;
    }

    </style>
    """, unsafe_allow_html=True)


def chart_theme(fig):

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            family="Arial",
            size=13
        ),

        title_font=dict(
            color="#ECEFF2",
            size=22
        ),

        title_x=0.5,

        hoverlabel=dict(
            bgcolor="#B1CCF0",
            font_color="white",
            bordercolor="#87C4E0"
        ),

        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        ),

        margin=dict(l=20, r=20, t=60, b=20)
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#ECEFF2",

        # X axis values
        tickfont=dict(
            color="white",
            size=12
        ),

        # X axis title
        title_font=dict(
            color="white",
            size=15
        ),

        zeroline=False
    )


    fig.update_yaxes(
        showgrid=True,
        gridcolor="#ECEFF2",

        # Y axis values
        tickfont=dict(
            color="white",
            size=12
        ),

        # Y axis title
        title_font=dict(
            color="white",
            size=15
        ),

        zeroline=False
    )

   

    return fig