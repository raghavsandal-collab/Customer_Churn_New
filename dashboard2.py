import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu 

def dashboard2():
        
        
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


# with st.sidebar:
#     opt = option_menu("Menu",options = ["Overview", "Customer Demographics & Services","Churn Analysis", "Revenue & Customer Lifetime Value","About"], icons=["house","file-text","activity","bar-chart","person"],default_index=0)

    # if opt == "Customer Demographics & Services":
        # st.html("style.css")
        st.markdown(
            '<h1 class = "title">🙎‍♂️Customer Demographics & Services</h1>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<br>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class = "custom-text-box">🙎‍♂️Customer Demographics & Services</p>',
            unsafe_allow_html=True
        )

        # st.title("🙎‍♂️Customer Demographics & Services")
        # st.write("🙎‍♂️Customer Demographics & Services")

        # st.sidebar.success("Internet Type")
        # st.sidebar.success("Contract")
        # st.sidebar.success("Payment Method")
        # st.sidebar.success("Phone Service")
        df = pd.read_csv("cleaned.csv")

        st.sidebar.header("Internet Filter")

        internet = st.sidebar.multiselect(
            "Internet Type",
            options=df["Internet Type"].unique(),
            default=df["Internet Type"].unique()[:3]
        )
        st.sidebar.success("Contract")
        st.sidebar.success("Payment Method")
        st.sidebar.success("Phone Service")


        st.sidebar.header("Payment Filter")

        payment = st.sidebar.multiselect(
            "Payment Method",
            options=df["Payment Method"].unique(),
            default=df["Payment Method"].unique()[:2]
        )

        st.sidebar.header("🔍Churn Filter")

        churn = st.sidebar.multiselect(
            "Select Churn as per City",
            options=df["City"].unique(),
            default=df["City"].unique()[:3]
        )

        # df = df[(df["City"].isin(churn)) 
        
        # # (df["visuals"].isin(visuals)) &
        # # df(["insight"].isin())
        # ]
        df = df[
            (df["City"].isin(churn)) &
            (df["Payment Method"].isin(payment))
        ]
        c1 , c2 , c3 , c4 = st.columns(4)

        avg_age = df["Age"]
        with c1:
            # st.metric("Average Age", round(df["Age"].mean(), 2))
            st.metric("Average Age", round(df["Age"].mean(), 2),"Years")

        with c2:
            # st.metric("Average Tenure",round(df["Tenure in Months"].mean(),2))
            st.metric("Average Tenure",round(df["Tenure in Months"].mean(),2),"Months")
        with c3:
            # st.metric("Average Downloads",round(df["Avg Monthly GB Download"].mean(),2))
            st.metric("Average Downloads",round(df["Avg Monthly GB Download"].mean(),2),"GB")
        with c4:
            # st.metric("Average Long Distance Charges",round(df["Avg Monthly Long Distance Charges"].mean(),2))
            st.metric("Average Long Distance Charges",round(df["Avg Monthly Long Distance Charges"].mean(),2),"Dollar")

        df["Age Group"] = pd.cut(
            df["Age"],
            bins=[18, 30, 45, 60, 80],
            labels=["18-30", "31-45", "46-60", "60+"]
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

        df["Download Category"] = pd.cut(
            df["Avg Monthly GB Download"],
            bins=[0, 100, 300, 600, 900],
            labels=["Low", "Medium", "High", "Very High"]
        )

        df["Revenue Category"] = pd.cut(
            df["Total Revenue"],
            bins=5,
            labels=["Very Low", "Low", "Medium", "High", "Premium"]
        )

        c1,c2 = st.columns(2)

        with c1:
            age = df.groupby("Age Group")["Customer ID"].count().reset_index()

            fig1 = px.bar(
                age,
                x="Age Group",
                y="Customer ID",
                color="Age Group",
                title="Customers by Age Group"
            )

            fig1.update_traces(marker_line_color='black', marker_line_width=2)
            fig1.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )
            st.plotly_chart(fig1)
        with c2:
    
            contract = (
                df.groupby(["Contract", "Charge Category"])
                .size()
                .reset_index(name="Customers")
            )

            fig2 = px.bar(
                contract,
                x="Contract",
                y="Customers",
                color="Charge Category",
                barmode="group",
                title="Contract by Monthly Charge Category"
            )
            fig2.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )
            st.plotly_chart(fig2)
        
        payment_data = (
            df.groupby(["Payment Method", "Revenue Category"])
            .size()
            .reset_index(name="Customers")
        )

        fig5 = px.bar(
            payment_data,
            x="Payment Method",
            y="Customers",
            color="Revenue Category",
            barmode="group",
            title="Payment Method by Revenue Category"
        )

        fig5.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
            plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
        )
        st.plotly_chart(fig5)
        c1,c2 = st.columns(2)

        with c1:
            fig3 = px.box(
                df,
                x="Tenure Category",
                y="Monthly Charge",
                color="Tenure Category",
                title="Monthly Charge by Tenure Category"
            )

            fig3.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )
            st.plotly_chart(fig3)
        with c2:
            fig4 = px.violin(data_frame=df, x = "Contract", y = "Internet Type", color = "Contract", title = "Internet Service as per Age")

            fig4.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )
            st.plotly_chart(fig4)


        # payment = (
        #     df.groupby(["Payment Method", "Revenue Category"])
        #     .size()
        #     .reset_index(name="Customers")
        # )

        # fig5 = px.bar(
        #     payment,
        #     x="Payment Method",
        #     y="Customers",
        #     color="Revenue Category",
        #     barmode="group",
        #     title="Payment Method by Revenue Category"
        # )

        # st.plotly_chart(fig5)

        # # fig6 = px.strip(data_frame=df, x = "Streaming TV", y = "Monthly Charge", color = "Contract", title = "Charge Distribution")
        # # fig6 = px.strip(data_frame=df, x = "Streaming TV", y = "Total Revenue", color = "Streaming TV", title = "Revenue Variation")
        # fig6 = px.area(data_frame=df, x = "Streaming TV", y = "Monthly Charge", color = "Streaming TV", title = "Revenue Variation")
        # st.plotly_chart(fig6)

        stream = (
            df.groupby(["Streaming TV", "Charge Category"])
            .size()
            .reset_index(name="Customers")
        )

        fig6 = px.bar(
            stream,
            x="Streaming TV",
            y="Customers",
            color="Charge Category",
            barmode="group",
            title="Streaming TV by Monthly Charge Category"
        )

        fig6.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
            plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
        )
        st.plotly_chart(fig6)

        fig7 = px.treemap(data_frame=df, path=["Avg Monthly GB Download"], values = "Monthly Charge", title = "Download VS Cost")

        fig7.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
            plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
        )
        st.plotly_chart(fig7)

        # fig8 = px.bar(data_frame=df, x = "Phone Service", y = "Total Revenue",color = "Phone Service", title = "Revenue Patterns")
        # st.plotly_chart(fig8)

        phone = (
            df.groupby(["Phone Service", "Charge Category"])
            .size()
            .reset_index(name="Customers")
        )

        fig8 = px.bar(
            phone,
            x="Phone Service",
            y="Customers",
            color="Charge Category",
            barmode="group",
            title="Phone Service by Monthly Charge Category"
        )

        fig8.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
            plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
        )
        st.plotly_chart(fig8)