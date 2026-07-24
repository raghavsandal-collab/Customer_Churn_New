import streamlit as st
import pandas as pd
import plotly.express as px

def about():
        
        
        st.markdown("""
        <style>
                    .stApp{
                    # background: linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
                    background: #0e1426;
                    }

                    # /* Main Title */
                    .title{
                        background:linear-gradient(90deg,#2563EB,#60A5FA);
                        color:white;
                        padding:18px;
                        border-radius:15px;
                        text-align:center;
                        font-size:38px;
                        font-weight:bold;
                        box-shadow:0 10px 25px rgba(0,0,0,.35);
                    }
                    /* Sidebar */
                    section[data-testid="stSidebar"]{
                        background: #0e1426;
                        border-right:2px solid #3B82F6;
                    }

                    /* Objective Box */
                    .custom-text-box{
                        background: #131e36;
                        color:white;
                        border-left:6px solid #60A5FA;
                        padding:18px;
                        border-radius:12px;
                        box-shadow:0 8px 20px rgba(0,0,0,.25);
                    }

                    /* Tabs */
                    button[data-baseweb="tab"]{
                        background: #131e36;
                        color:white;
                        border-radius:10px;
                    }

                    button[data-baseweb="tab"][aria-selected="true"]{
                        background:#3B82F6;
                        color:white;
                    }

                    /* Multiselect */
                    .stMultiSelect > div > div{
                        background:#103C7A;
                        border-radius:10px;
                        color:white;
                    }
                    /* Dataframe */
                    div[data-testid="stDataFrame"]{
                        # background:#103C7A;
                        background:#131e36;
                        border-radius:12px;
                        padding:10px;
                    }

                    # <style>
                    [data-testid="column"] {
                        background-color: #f8f9fa;
                        padding: 15px;
                        border-radius: 10px;
                        border: 1px solid #ddd;
                    }
                    
                    # --------------------------------------------------------------
                                /* ===========================
                    TEXT COLOR - WHITE
                    =========================== */

                    /* Main app text */
                    .stApp{
                        color: white;
                    }

                    /* All headings */
                    h1, h2, h3, h4, h5, h6{
                        color: white !important;
                    }

                    /* Paragraphs, labels, markdown */
                    p,
                    label,
                    span,
                    div,
                    li{
                        # color: white;
                    }

                    /* Streamlit Markdown */
                    [data-testid="stMarkdownContainer"]{
                        color:white !important;
                    }

                    /* Metric Labels */
                    [data-testid="metric-container"] label{
                        color:white !important;
                        font-weight:bold;
                    }

                    /* Metric Values */
                    [data-testid="metric-container"] div{
                        color:white !important;
                    }

                    /* Tabs */
                    button[data-baseweb="tab"]{
                        color:white !important;
                    }

                    /* Selected Tab */
                    button[data-baseweb="tab"][aria-selected="true"]{
                        color:white !important;
                    }

                    # /* Sidebar text */
                    # section[data-testid="stSidebar"] *{
                    #     color:white !important;
                    # }

                    /* Selectbox */
                    .stSelectbox label{
                        color:white !important;
                    }

                    /* Multiselect */
                    .stMultiSelect label{
                        color:white !important;
                    }

                    /* Radio */
                    .stRadio label{
                        color:white !important;
                    }

                    /* Checkbox */
                    .stCheckbox label{
                        color:white !important;
                    }

                    /* DataFrame headers */
                    [data-testid="stDataFrame"]{
                        color:white !important;
                    }

                    # ---------------------------------------------------
                    /* Force all Streamlit widget text white */
                    .stTextInput label,
                    .stNumberInput label,
                    .stSelectbox label,
                    .stMultiSelect label,
                    # .stSlider label,
                    .stRadio label,
                    .stCheckbox label,
                    .stDateInput label,
                    .stFileUploader label,
                    .stMetric,
                    .css-10trblm,
                    .css-1d391kg {
                        color:white !important;
                    }
        </style>
        """,unsafe_allow_html=True)


        # st.html("style.css")
        st.markdown(
            '<h1 class = "title">📈About Project</h1>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<br>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class = "custom-text-box">PROJECT : Customer Churn Analysis</p>',
            unsafe_allow_html=True
        )
        # st.title("📈About Project")
        # st.header("Customer Churn Analysis")
        # st.write("This project analysis the telecom dataset and gives us insights about our company customer churn rate and more.")

        # st.markdown(
        #         '<h3 class = "tech"><ul>Technology Used--><li>Python</li><li>Pandas</li><li>Plotly</li><li>Streamlit</li></ul></h3>',
        #         unsafe_allow_html=True
        # )

        st.markdown(
                # '<h3 class = "tech"><ul>Technology Used--></ul></h3>',
                '<h3 class = "tech">Technology Used--></h3>',
                unsafe_allow_html=True
        )
        st.markdown(
                '<p class = "subtech"><ul><li>Python</li><li>Pandas</li><li>Plotly</li><li>Streamlit</li></ul></p>',
                unsafe_allow_html=True
        )


        # st.markdown(
        #         '<h3 class = "Techno">Technology Used</h3>',
        #         unsafe_allow_html=True
        # )

        # st.html("style.css")
        # st.header("Technology Used", key = "technology")
        # st.subheader("Technology Used")
        # st.write("-Python")
        # st.write("-Pandas")
        # st.write("-Plotly")
        # st.write("-Streamlit")