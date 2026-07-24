import streamlit as st
import pandas as pd
import plotly.express as px

def dashboard3():


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
            '<h1 class = "title">🔍Churn Analysis</h1>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<br>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class = "custom-text-box">Objective: Identify factors contributing to churn.</p>',
            unsafe_allow_html=True
        )

        # st.title("🔍Churn Analysis")
        # st.write("Objective: Identify factors contributing to churn.")

        df = pd.read_csv("cleaned.csv")

        # # st.sidebar.button("Churn Label")
        # st.sidebar.success("Churn Label")
        # st.sidebar.success("Churn Category")
        # st.sidebar.success("Contract")
        # st.sidebar.success("Internet Type")

        st.sidebar.header("🔍Churn Filter")

        churn = st.sidebar.multiselect(
            "Select Churn as per City",
            options=df["City"].unique(),
            default=df["City"].unique()[:3]
        )

        df = df[(df["City"].isin(churn)) 
        # (df["visuals"].isin(visuals)) &
        # df(["insight"].isin())
        ]

        st.sidebar.header("🙎‍♂️Churn Status")

        churn1 = st.sidebar.multiselect(
            "Select Churn status",
            options=df["Churn Category"].unique(),
            default=df["Churn Category"].unique()
        )

        df = df[(df["Churn Category"].isin(churn1)) 
        # (df["visuals"].isin(visuals)) &
        # df(["insight"].isin())
        ]
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            total_count = df["Customer Status"].count()
            df1 = df[df["Customer Status"] == "Churned"]

            churn_count = len(df[df["Customer Status"] == "Churned"])
            div_churn = (churn_count / total_count) * 100
            # st.metric("Churn Rate",round(div_churn,2))
            st.metric("Churn Rate",round(div_churn,2),"%")

        with c2:
            st.metric("Average Churn Score",df["Churn Score"].median())
        with c3:
            st.metric("Average CLTV", round(df["CLTV"].mean(),2))
        with c4:
            st.metric("Average Customer Tenure", round(df["Tenure in Months"].mean(),2))

        st.subheader("📊Visulization")

        df["Churn Score Category"] = pd.cut(
            df["Churn Score"],
            bins=[0, 25, 50, 75, 100],
            labels=["Very Low", "Low", "High", "Very High"]
        )

        df["CLTV Category"] = pd.cut(
            df["CLTV"],
            bins=4,
            labels=["Low", "Medium", "High", "Premium"]
        )

        df["Charge Category"] = pd.cut(
            df["Monthly Charge"],
            bins=[0, 30, 60, 90, 120],
            labels=["Low", "Medium", "High", "Premium"]
        )

        df["Tenure Category"] = pd.cut(
            df["Tenure in Months"],
            bins=[0, 12, 24, 48, 72],
            labels=["0-12", "13-24", "25-48", "49-72"]
        )

        df["Satisfaction Category"] = pd.cut(
            df["Satisfaction Score"],
            bins=[0, 2, 4, 5],
            labels=["Low", "Medium", "High"]
        )
        c1,c2 = st.columns(2)
        with c1:
            fig1 = px.sunburst(
                df,
                path=["Contract", "Churn Label"],
                title="Contract Wise Churn"
            )

            fig1.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )
            st.plotly_chart(fig1)

            score = (
                df.groupby("Churn Score Category")["Customer ID"]
                .count()
                .reset_index()
            )

            fig2 = px.bar(
                score,
                x="Churn Score Category",
                y="Customer ID",
                color="Churn Score Category",
                title="Customer Count by Churn Score Category"
            )

            fig2.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )

            st.plotly_chart(fig2, use_container_width=True)

        # fig3 = px.box(data_frame=df, x = "Churn Label", y = "Tenure in Months", color = "Churn Label",title = "Tenure Comparison")
        # st.plotly_chart(fig3)
        with c2:
            fig3 = px.violin(
                df,
                x="Tenure Category",
                y="Monthly Charge",
                color="Tenure Category",
                box=True,
                title="Monthly Charge by Tenure Category"
            )

            fig3.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )

            st.plotly_chart(fig3)

            cltv = (
                df.groupby("CLTV Category")["Customer ID"]
                .count()
                .reset_index()
            )

            fig5 = px.pie(
                cltv,
                names="CLTV Category",
                values="Customer ID",
                hole=0.5,
                title="Customer Distribution by CLTV Category"
            )

            fig5.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )

            st.plotly_chart(fig5)

        # # fig6 = px.line(data_frame=df, x = "Satisfaction Score", y = "Churn Score" , color="Churn Score", title = "Satisfaction Effect")
        # # fig6 = px.bar(data_frame=df, x = "Satisfaction Score", y = "Churn Score", color = "Satisfaction Score", color_continuous_scale=,title = "Satisfaction Effect")
        # fig6 = px.bar(data_frame=df, x = "Satisfaction Score", y = "Churn Score", color = "Satisfaction Score", color_continuous_scale= "Oranges",title = "Satisfaction Effect")
        # st.plotly_chart(fig6)
        c3,c4 = st.columns(2)
        with c3:
            sat = (
                df.groupby("Satisfaction Category")["Customer ID"]
                .count()
                .reset_index()
            )

            fig6 = px.treemap(
                sat,
                path=["Satisfaction Category"],
                values="Customer ID",
                title="Customer Satisfaction Categories"
            )

            fig6.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )

            st.plotly_chart(fig6)

            # fig7 = px.area(data_frame=df, x = "Churn Category", color = "Churn Category",title = "Top Churn Categories")
            fig7 = px.pie(data_frame=df, names = "Churn Category", values = "CLTV",title = "Top Churn Categories")

            fig7.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )

            st.plotly_chart(fig7)
        with c4:
            fig8 = px.treemap(data_frame=df, path = ["Churn Reason"], values = "CLTV",color = "Churn Reason",title = "Top Churn Reasons")
            # fig8.update_layout(width = 900 , height = 700)

            fig8.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )

            st.plotly_chart(fig8)

        # contract as per cltv in bar or column instead of c put value in y