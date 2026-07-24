import streamlit as st
import pandas as pd
import plotly.express as px
import dashboard2 as d2
import dashboard3 as d3
import dashboard4 as d4
import about as ab
# import apply_theme as af
import style1 as s1
from streamlit_option_menu import option_menu 
# import pathlib
st.set_page_config(
    page_title="Customer Churn",
    page_icon="🙎‍♂️",
    layout= "wide"
)

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
#     st.markdown(
#         "<h2 style='color:black;'>Menu</h2>",
#         unsafe_allow_html=True
#     )

#     opt = option_menu(
#         menu_title=None,
#         options=[
#             "Overview",
#             "Customer Demographics & Services",
#             "Churn Analysis",
#             "Revenue & Customer Lifetime Value",
#             "About"
#         ],
#         icons=["house", "file-text", "activity", "bar-chart", "person"],
#         default_index=0,
#         styles={
#             "container": {"background-color": "#F0F8FF"},
#             "icon": {"color": "black"},
#             "nav-link": {"color": "black"},
#             "nav-link-selected": {
#                 "background": "linear-gradient(90deg,#1565C0,#42A5F5)",
#                 "color": "black",
#             },
#         },
#     )

with st.sidebar:

    st.markdown("""
    <div style="
        background-color:#F0F8FF;
        color:black !important;
        text-align:center;
        font-size:24px;
        font-weight:bold;
        padding:12px;
        border-radius:10px;
        margin-bottom:10px;
        border:1px solid #1565C0;
    ">
        📋 Menu
    </div>
    """, unsafe_allow_html=True)

    opt = option_menu(
        menu_title=None,
        options=[
            "Overview",
            "Customer Demographics & Services",
            "Churn Analysis",
            "Revenue & Customer Lifetime Value",
            "About"
        ],
        icons=["house", "file-text", "activity", "bar-chart", "person"],
        default_index=0,
        styles={
            "container": {
                "background-color": "#F0F8FF",
                "padding": "5px",
                "border-radius": "10px",
            },
            "icon": {
                "color": "black",
                "font-size": "18px",
            },
            "nav-link": {
                "font-size": "16px",
                "color": "black",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#64B5F6",
                "border-radius": "10px",
            },
            "nav-link-selected": {
                "background": "linear-gradient(90deg,#1565C0,#42A5F5)",
                "color": "white",
                "font-weight": "bold",
            },
        },
    )
# st.markdown("""
            
# <style>

# /* ============================
#    DARK ROYAL BLUE DASHBOARD
# ============================= */

# .stApp{
#     background: #081C3A;
# }

# /* Sidebar */
# section[data-testid="stSidebar"]{
#     background: linear-gradient(180deg,#04142D,#0B2E63,#154A99);
#     border-right:2px solid #3B82F6;
# }

# section[data-testid="stSidebar"] *{
#     color:white !important;
# }

# /* Main Title */
# .title{
#     background:linear-gradient(90deg,#2563EB,#60A5FA);
#     color:white;
#     padding:18px;
#     border-radius:15px;
#     text-align:center;
#     font-size:38px;
#     font-weight:bold;
#     box-shadow:0 10px 25px rgba(0,0,0,.35);
# }

# /* Objective Box */
# .custom-text-box{
#     background:#0F2F66;
#     color:white;
#     border-left:6px solid #60A5FA;
#     padding:18px;
#     border-radius:12px;
#     box-shadow:0 8px 20px rgba(0,0,0,.25);
# }

# /* Metric Cards */
# div[data-testid="metric-container"]{
#     background:#103C7A;
#     border:1px solid #3B82F6;
#     border-radius:15px;
#     padding:15px;
#     box-shadow:0 8px 20px rgba(0,0,0,.25);
# }

# div[data-testid="metric-container"]:hover{
#     transform:translateY(-5px);
#     transition:0.3s;
#     box-shadow:0 12px 28px rgba(59,130,246,.45);
# }

# div[data-testid="metric-container"] label{
#     color:#93C5FD !important;
#     font-weight:bold;
# }

# div[data-testid="metric-container"] div{
#     color:white !important;
#     font-weight:bold;
# }

# /* Buttons */
# .stButton>button{
#     background:linear-gradient(90deg,#2563EB,#3B82F6);
#     color:white;
#     border:none;
#     border-radius:10px;
#     font-weight:bold;
# }

# .stButton>button:hover{
#     background:linear-gradient(90deg,#1D4ED8,#2563EB);
# }

# /* Tabs */
# button[data-baseweb="tab"]{
#     background:#123E7A;
#     color:white;
#     border-radius:10px;
# }

# button[data-baseweb="tab"][aria-selected="true"]{
#     background:#3B82F6;
#     color:white;
# }

# /* Charts */
# div[data-testid="stPlotlyChart"]{
#     background:#0F2F66;
#     border-radius:15px;
#     padding:10px;
#     box-shadow:0 8px 18px rgba(0,0,0,.30);
# }

# /* Dataframe */
# div[data-testid="stDataFrame"]{
#     background:#103C7A;
#     border-radius:12px;
#     padding:10px;
# }

# /* Selectbox */
# .stSelectbox > div > div{
#     background:#103C7A;
#     color:white;
#     border-radius:10px;
# }

# /* Multiselect */
# .stMultiSelect > div > div{
#     background:#103C7A;
#     color:white;
# }

# /* Expanders */
# .streamlit-expanderHeader{
#     background:#2563EB;
#     color:white;
#     border-radius:10px;
# }

# /* Headings */
# h1,h2,h3,h4{
#     color:#E0F2FE;
# }

# /* Scrollbar */
# ::-webkit-scrollbar{
#     width:10px;
# }

# ::-webkit-scrollbar-track{
#     background:#0F2F66;
# }

# ::-webkit-scrollbar-thumb{
#     background:#3B82F6;
#     border-radius:20px;
# }

# ::-webkit-scrollbar-thumb:hover{
#     background:#60A5FA;
# }

# .block-container{
#     padding-top:2rem;
# }

# </style>

# </style>
# """, unsafe_allow_html=True)    

# with st.sidebar:
#     opt = option_menu("Menu",options = ["Overview", "Customer Demographics & Services","Churn Analysis", "Revenue & Customer Lifetime Value","About"], icons=["house","file-text","activity","bar-chart","person"],default_index=0, key = "menu")

# with st.sidebar:
#     opt = option_menu(
#         "Menu",
#         ["Overview",
#          "Customer Demographics & Services",
#          "Churn Analysis",
#          "Revenue & Customer Lifetime Value",
#          "About"],
#         icons=["house","file-text","activity","bar-chart","person"],
#         default_index=0,
#         styles={
#             "container": {
#                 # "background-color": "#D9E1E8",
#                 "background-color": "#F0F8FF",
#                 "padding": "5px"
#                 # "border-radius": "10px";

#             },
#             "icon": {
#                 # "color": "white",
#                 "color": "black",
#                 "font-size": "18px"
#             },
#             "nav-link": {
#                 "font-size": "16px",
#                 # "color": "white",
#                 "color": "black",
#                 "text-align": "left",
#                 "margin": "5px",
#                 "--hover-color": "#64B5F6",
#                 "border-radius": "10px",
#             },
#             "nav-link-selected": {
#                 "background": "linear-gradient(90deg,#1565C0,#42A5F5)",
#                 # "color": "white",
#                 "color": "black",
#                 "font-weight": "bold",

#             #     # -------------------------------------------------------
#             # "icon": {
#             #     "color": "white",
#             #     "font-size": "18px",
#             # },
#             # "nav-link": {
#             #     "font-size": "16px",
#             #     "color": "white",
#             #     "text-align": "left",
#             #     "margin": "5px",
#             #     "--hover-color": "#64B5F6",
#             #     "border-radius": "10px",
#             # },
#             # "nav-link-selected": {
#             #     "background": "linear-gradient(90deg,#1565C0,#42A5F5)",
#             #     "color": "white",
#             #     "font-weight": "bold",
#             # },
#             },
#         },
#     )


if opt == "Overview":

    df = pd.read_csv("cleaned.csv")

    st.sidebar.header("🔍Churn Filter")

    # st.html("style.css")

    st.markdown(
        '<h1 class = "title">📊Executive Overview</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<br>',
        unsafe_allow_html=True
    )

    st.sidebar.header("📊Visuals")

    visuals = st.sidebar.multiselect(
        "Select Visual",
        options=["Bar Graph", "Line Graph", "Pie Chart", "Scatter"],
        default=["Bar Graph"][:3]
    )

    st.markdown(
        # '<div class="custom-text-box">This text has a blue background and border.</div>', 
        '<div class="custom-text-box"><b>🎯Objective:</b> Provide an overall snapshot of the customer base, churn, and revenue.</div>', 
        unsafe_allow_html=True
    )

    st.markdown(
        # '<div class="custom-text-box">This text has a blue background and border.</div>', 
        '<br>', 
        unsafe_allow_html=True
    )

    # # 2. Target your custom class with CSS
    # st.html("""
    # <style>
    #     .custom-text-box {
    #         background-color: #E8F0FE;
    #         border: 2px solid #1A73E8;
    #         padding: 10px;
    #         border-radius: 5px;
    #     }
    # </style>
    # """)

    st.sidebar.header("📊Insights")

    insight = st.sidebar.multiselect(
        "Select Insight to know",
        options=["Total No. of Customers", "Number of Offers","Churned Customers", "CLTV"],
        default=["CLTV"][:3]
    )

    tab1,tab2,tab3 =st.tabs(["Overview", "Dataset", "Visuals"])

    with tab1:
        style = {
            tab1
        }

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("💵Total Revenue", round(df["Total Revenue"].sum(),2))

        with c2:
            st.metric("🙎‍♂️No of customers", df["Customer ID"].nunique())
        with c3:
            st.metric("🏙️no. of Cities", df["City"].nunique())

        with c4:
            st.metric("🎯No. of Offers", df["Offer"].nunique())

        churn = st.multiselect(
            "Select Churn as per City",
            options=df["City"].unique(),
            # sorted(df["City"].unique())
            default=df["City"].unique()[:3]
        )

        df = df[(df["City"].isin(churn)) 
        # (df["visuals"].isin(visuals)) &
        # df(["insight"].isin())
        ]

        c1, c2 = st.columns(2)

        with c1:
            figure = px.histogram(data_frame=df, x = "Total Revenue", nbins = 25, title = "Total Revenue")
            st.plotly_chart(figure)
            contract_wise_customer = df.groupby("Contract")["Customer ID"].count().reset_index()
            figure1 = px.pie(data_frame=contract_wise_customer, names = "Contract", values= "Customer ID"  , hole= 0.5)
            st.plotly_chart(figure1)

        total_Customer = df.groupby("Gender")["Customer ID"].count().reset_index()
        figure2 = px.pie(data_frame= total_Customer , names = "Gender" , values = "Customer ID" , color= "Gender", hole = 0.5, title = "Customer ID as per Gender")
        st.plotly_chart(figure2)

        with c2:
            total_cities = df.groupby("City")["Total Revenue"].sum().reset_index().nlargest(10,["Total Revenue"])
            # figure3 = px.treemap(data_frame = df, path = ["City"], values = "Total Revenue")
            figure3 = px.treemap(data_frame = total_cities, path = ["City"], values = "Total Revenue", title = "Top 10 Cities as per Total Revenue")
            st.plotly_chart(figure3)

            figure4 = px.pie(data_frame=df, names = "Offer", title = "Types of Offers")
            # figure4.update_layout(width = 400, height = 600)
            st.plotly_chart(figure4, use_container_width=True)

    with tab2:
        c1,c2 = st.columns(2)
        with c1:
            st.metric("📝Total Rows",df.shape[0])
        with c2:
            st.metric("🗒️Total Columns",df.shape[1])  
        c3,c4 = st.columns(2)
        with c3:
            # st.metric("❌Missing Values",0)
            st.metric("❌Missing Values",df.isna().sum().sum())
        with c4:
            st.metric("🔍Duplicate Rows",df.duplicated().sum())
        st.subheader("Dataset")
        st.dataframe(df)
        st.subheader("Column Names")
        # st.columns(df)
        st.dataframe(df.columns.tolist())
        # st.markdown(df.columns.tolist())

    with tab3:
        customer_id = df.groupby("Churn Category")["Customer ID"].count().reset_index()
        fig1 = px.treemap(data_frame= customer_id , path = ["Churn Category"], values = "Customer ID", color = "Churn Category", title = "Churn Category as per Age")
        st.plotly_chart(fig1)

        Offer_type = df.groupby("Offer")["Customer ID"].count().reset_index()
        fig2 = px.pie(data_frame= Offer_type , names = "Offer", values= "Customer ID", title = "Types Of Offers")
        st.plotly_chart(fig2)

        Offer_line = df.groupby("Payment Method")["Customer ID"].count().reset_index()
        fig3 = px.bar(data_frame= Offer_line , x = "Payment Method", y= "Customer ID", color = "Payment Method",title = "Payment Method as per Customer ID")
        st.plotly_chart(fig3)

        df["Monthly Charge Category"] = pd.cut(
            df["Monthly Charge"],
            bins=[0, 30, 60, 90, 120],
            labels=["0-30", "31-60", "61-90", "91-120"]
        )

        Offer_line_revenue = (
            df.groupby("Monthly Charge Category")["Customer ID"]
            .count()
            .reset_index()
        )

        fig4 = px.line(
            Offer_line_revenue,
            x="Monthly Charge Category",
            y="Customer ID",
            markers=True,
            title="Customer Count by Monthly Charge Category"
        )

        st.plotly_chart(fig4, use_container_width=True)


    # pd.cut
        Offer_line_revenue = df.groupby("Monthly Charge")["Total Revenue"].count().reset_index().nlargest(10, ["Total Revenue"])
        fig5 = px.area(data_frame= Offer_line_revenue , x = "Monthly Charge", y= "Total Revenue")
        st.plotly_chart(fig5)

        # fig6 = px.box(data_frame= df , x = "Gender" , y = "Monthly Charge" , color= "Gender")
        # ---->fig6 = px.box(data_frame= df , x = "Gender" , y = "Total Revenue" , color= "Gender")
        Gender_wise_total_revenue = df.groupby("Gender")["Total Revenue"].sum().reset_index()
        # st.dataframe(Gender_wise_total_revenue)
        fig6 = px.pie(data_frame= Gender_wise_total_revenue , names = "Gender" , values = "Total Revenue" , color= "Gender", hole = 0.5, title = "Total Revenue as per Gender")
        st.plotly_chart(fig6)

        city_wise_total_revenue = (
            df.groupby("City")["Total Revenue"]
            .sum()
            .reset_index()
            .sort_values("Total Revenue")
            .nlargest(10, "Total Revenue")
        )

        fig12 = px.bar(
            city_wise_total_revenue,
            x="Total Revenue",
            y="City",
            orientation="h",
            color="Total Revenue",
            title="Top 10 Cities by Total Revenue"
        )

        st.plotly_chart(fig12, use_container_width=True)

        fig13 = px.imshow(df.corr(numeric_only=True) , text_auto= True, title = "HeatMap")
        fig13.update_layout(width = 500, height = 700)
        st.plotly_chart(fig13)

        # fig14 = px.bar(data_frame= df, x = "Customer Status" , y = "Total Revenue", color = "Gender")
        fig14 = px.bar(data_frame= df, x = "Customer Status" , y = "Total Revenue" , color = "Customer Status")
        st.plotly_chart(fig14)

        fig15 = px.histogram(data_frame=df, x = "Monthly Charge", nbins = 30)
        st.plotly_chart(fig15)

        fig16 = px.histogram(data_frame=df, x = "Total Revenue", nbins = 25)
        st.plotly_chart(fig16)

        fig17 = px.box(data_frame=df, x = "Monthly Charge Category", y = "Total Revenue", color = "Monthly Charge Category", title = "Revenue by Monthly Charge Category")
        st.plotly_chart(fig17)

        df["Satisfaction Level"] = pd.cut(
            df["Satisfaction Score"],
            bins=[0, 2, 4, 5],
            labels=["Low", "Medium", "High"]
        )
        fig18 = px.bar(
            df,
            x="Satisfaction Level",
            y="Monthly Charge",
            color="Satisfaction Level",
            title="Monthly Charge by Satisfaction Level"
        )

        st.plotly_chart(fig18, use_container_width=True)

if opt == "Customer Demographics & Services":
    d2.dashboard2()
       
if opt == "Churn Analysis":
    d3.dashboard3()

if opt == "Revenue & Customer Lifetime Value":
    d4.dashboard4()

if opt == "About":
    ab.about()