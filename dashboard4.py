import streamlit as st
import pandas as pd
import plotly.express as px

def dashboard4():
        
        
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
            '<h1 class = "title">💵Revenue & Customer Lifetime Value</h1>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<br>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class = "custom-text-box">Objective: Analyze revenue and customer lifetime value.</p>',
            unsafe_allow_html=True
        )

        # st.title("💵Revenue & Customer Lifetime Value")
        # st.write("Objective: Analyze revenue and customer lifetime value.")

        st.set_page_config(
            page_title="Customer Churn",
            page_icon="🙎‍♂️",
            layout= "wide"
        )

        df = pd.read_csv("cleaned.csv")

        # st.sidebar.success("Contract")
        # st.sidebar.success("Internet Type")
        # st.sidebar.success("Payment Method")

        # st.sidebar.success("Customer Status")

        st.sidebar.header("📝Contract")

        Contract = st.sidebar.multiselect(
            "Contract filter",
            options=df["Contract"].unique(),
            default=df["Contract"].unique()[:3]
        )

        st.sidebar.header("🌐Internet Type")

        Internet_Type = st.sidebar.multiselect(
             "Internet Type Filter",
             options = df["Internet Type"].unique(),
             default = df["Internet Type"].unique()[:3]
        )

        st.sidebar.header("💵Payment Method")

        Payment_Method = st.sidebar.multiselect(
             "Payment Method Filter",
             options = df["Payment Method"].unique(),
             default = df["Payment Method"].unique()[:3]
        )

        st.sidebar.header("📱Phone Service")

        Customer_Service = st.sidebar.multiselect(
             "Select Customer Service",
             options = df["Phone Service"].unique(),
             default = df["Phone Service"].unique()[:3]
        )
        df = df[(df["Contract"].isin(Contract)) &
        (df["Internet Type"].isin(Internet_Type)) &
        (df["Payment Method"].isin(Payment_Method)) &
        (df["Phone Service"].isin(Customer_Service))
        ]

        c1,c2,c3,c4,c5 = st.columns(5)

        with c1:
            st.metric("Total Revenue", round(df["Total Revenue"].sum(),2))

        with c2:
            st.metric("Average Revenue", round(df["Total Revenue"].mean(),2))
            
        with c3:
            st.metric("Average CLTV", round(df["CLTV"].mean(),2))
            
        with c4:
            st.metric("Average Monthly Charge", round(df["Monthly Charge"].mean(),2))

        with c5:
            st.metric("Average Total Charges", round(df["Total Charges"].mean(),2))

        st.subheader("📊Visulization")

        c1,c2 = st.columns(2)
        with c1:
            df["CLTV Category"] = pd.cut(
                df["CLTV"],
                bins=5,
                labels=["Very Low","Low","Medium","High","Premium"]
            )

            cltv = df.groupby("CLTV Category")["Customer ID"].count().reset_index()

            fig1 = px.bar(
                cltv,
                x="CLTV Category",
                y="Customer ID",
                color="CLTV Category",
                title="Customer Distribution by CLTV"
            )
            fig1.update_traces(marker_line_color='black', marker_line_width=2)

            fig1.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )

            st.plotly_chart(fig1)

        # fig1 = px.histogram(data_frame=df, x = "CLTV",title = "CLTV Distribution")
        # fig1.update_traces(marker_line_color='black', marker_line_width=2)
        # st.plotly_chart(fig1)

        # fig2 = px.bar(data_frame=df, x = "Contract", y = "CLTV", color = "Contract",title = "Revenue Comparison", barmode="group")
        # st.plotly_chart(fig2)

        contract = (
            df.groupby("Contract")["CLTV"]
            .mean()
            .reset_index()
        )

        fig2 = px.funnel(
            contract,
            x="CLTV",
            y="Contract",
            # color = "Contract",
            title="Average CLTV by Contract"
        )

        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
            plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
        )
        
        st.plotly_chart(fig2)

        # fig3 = px.scatter(data_frame=df, x = "Monthly Charge", y = "CLTV", color = "Monthly Charge",title = "Pricing VS Value")
        # st.plotly_chart(fig3)
        with c2:
            df["Charge Category"] = pd.cut(
                df["Monthly Charge"],
                bins=[0,30,60,90,120],
                labels=["Low","Medium","High","Premium"]
            )

            fig3 = px.box(
                df,
                x="Charge Category",
                y="CLTV",
                color="Charge Category",
                title = "Monthly Charge Category"
            )

            fig3.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
                plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
            )

            st.plotly_chart(fig3)

        # fig4 = px.scatter(data_frame=df, x = "Total Charges", y = "CLTV", color = "Monthly Charge",title = "Lifetime Relationship")
        # st.plotly_chart(fig4)

        df["Total Charge Category"] = pd.cut(
            df["Total Charges"],
            bins=5,
            labels=["Very Low","Low","Medium","High","Premium"]
        )

        fig4 = px.violin(
            df,
            x="Total Charge Category",
            y="CLTV",
            color="Total Charge Category",
            box=True,
            title="CLTV by Total Charges"
        )

        fig4.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
            plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
        )
        
        st.plotly_chart(fig4)

        # fig5 = px.box(data_frame=df, x = "Internet Type", y = "Total Revenue", color = "Internet Type",title = "Revenue By Internet Type")
        # st.plotly_chart(fig5)

        internet = (
            df.groupby("Internet Type")["Total Revenue"]
            .sum()
            .reset_index()
        )

        fig5 = px.sunburst(
            internet,
            path=["Internet Type"],
            values="Total Revenue",
            title="Revenue by Internet Type"
        )

        fig5.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
            plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
        )

        st.plotly_chart(fig5)

        # fig6 = px.violin(data_frame=df, x = "Payment Method", y = "Total Revenue", color = "Payment Method", box = True, title = "Revenue Distribution")
        # st.plotly_chart(fig6)

        payment = (
            df.groupby("Payment Method")["Total Revenue"]
            .sum()
            .reset_index()
        )

        fig6 = px.pie(
            payment,
            names="Payment Method",
            values="Total Revenue",
            hole=0.5,
            title="Revenue Share by Payment Method"
        )

        fig6.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
            plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
        )
        
        st.plotly_chart(fig6)

        # fig7 = px.treemap()

        # fig8 = px.imshow(df.corr(numeric_only=True), color_continuous_scale= "matter",title = "Financial Correlations")
        # fig8.update_layout(width = 500, height = 700)
        # st.plotly_chart(fig8)

        corr_df = df[[
            "Monthly Charge",
            "Total Charges",
            "Total Revenue",
            "CLTV"
        ]]

        fig8 = px.imshow(
            corr_df.corr(),
            text_auto=True,
            color_continuous_scale="matter",
            title="Revenue & CLTV Correlation"
        )

        fig8.update_layout(width = 400, height = 600)

        fig8.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",   # Outside the plot
            plot_bgcolor="rgba(0,0,0,0)"     # Inside the plot
        )
        
        st.plotly_chart(fig8, use_container_width=True)